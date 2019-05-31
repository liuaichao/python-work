# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:56:43 2017

@author: Quantum Liu
"""

import re
import requests
from multiprocessing import Pool,cpu_count,freeze_support
import traceback
import time
from PIL import Image
import pickle
import os
class site():
#对于pornhub全站的抽象，拥有多个视频类别（categories）;
#An abstraction of pornhub website,has a list of categories and videos.
    def __init__(self):
        self.category_params,self.category_name_list=list_categories()
        self.category_dict={}.fromkeys(self.category_name_list)
        print('There are '+str(len(self.category_name_list))+' categories.\n',self.category_name_list)
        self.video_list={}
        self.id2title_dict={}
        self.category_id=1
        self.title2id_dict={}
    def init_category(self,name_list=[''],num_category=0):
        if num_category and name_list:
            name_list=name_list[:min(num_category,len(name_list)-1)]
        elif not name_list and num_category:
            name_list=self.category_list[:min(num_category,len(self.category_list))]
        clist=init_categories_p(self.category_params,(name_list if name_list else self.category_name_list))
        for c in clist:
            self.category_dict[c.name]=c
        return self
    def iterate_videos(self,category_name='',num_page=0,start_page=1,iterate_all=False):
        for v in self.category_dict[category_name].iterate_videos_p(num_page,start_page,iterate_all):
            self.video_list[v.video_id]=v
            self.title2id_dict[v.title]=v.video_id
            self.id2title_dict[v.video_id]=v.title
        return self
#==============================================================================
#     
#==============================================================================
class category():
#对于视频分类(category)的抽象，拥有一系列视频
#An abstration of "categories", has a list of viseos
    def __init__(self,name='',url='',num_video=0,category_id=1):
        self.name=name
        self.url=url
        self.num_video=num_video
        self.max_page=self.max_page()
        self.videos=[]
        self.category_id=category_id
    def max_page(self):
        try:
            headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
            page=int(self.num_video/44)
            r_max=r'<li class="page_smoothing.*?<a class="greyButton" href=".*?">(.*?)</a></li>[\s\t\n]*?<li class="page_next'
            result=[]
            t=0
            while not (bool(result) or t>10):
                page-=50
                page=max(page,1)
                params={'page':(page)}
                html_text=requests.get(self.url,headers=headers,params=params).text
                result=re.findall(r_max,html_text)
                t+=1
            if not result:
                page=1
                t=0
                while not (bool(result) or t>10):
                    params={'page':(page)}
                    html_text=requests.get(self.url,headers=headers,params=params).text
                    result=re.findall(r_max,html_text)
                    page+=15
                    t+=1
            max_page=(int(result[0]) if result else 1)
            print('The max page of category '+self.name+' is :',max_page)
        except ConnectionError:
            max_page=1
            traceback.print_exc()
            print('Got connection error, return 1 for default.')
        return max_page
    def iterate_videos_p(self,num_page=0,start_page=1,iterate_all=False):
        start_page=max(start_page,1)
        freeze_support()
        pool=Pool(cpu_count())
        param_results=[]
        for p in range(start_page,((start_page+num_page if num_page else max(start_page+100,self.max_page)) if not iterate_all else self.max_page)):
            param_results.append(pool.apply_async(get_videoadd,(self.url,p,self.category_id)))
        pool.close()
        pool.join()
        pool=Pool(cpu_count())
        video_results=[]
        for params in [p for l in [result.get() for result in param_results] for p in l]:
            video_results.append(pool.apply_async(video,params))
        pool.close()
        pool.join()
        self.videos+=[result.get() for result in video_results]
        return self.videos
#==============================================================================
#         
#==============================================================================
class video():
#对视频的抽象，属性包括所在网页、封面、不同质量MP4文件的链接，时长，评价，所属分类
#An abstraction of video, attributes contain the web page, .MP4 files' urls of different qualities, duration, grade, categories
    def __init__(self,title='',page='',cover='',video_id=''):
        self.page=page
        self.cover=cover
        self.title=title
        self.video_id=video_id
        print('Crawling video:'+title)
        self.mp4add,self.duration,self.info='',0,''
    def update(self):
        try:
            self.mp4add,self.duration,self.info=get_video(self.page)
        except:
            self.mp4add,self.duration,self.info='',0,''
            print('Got error, failed instantiating viedo: '+self.title)
            traceback.print_exc()
        return self
    def show_info(self,pic_dir='',show_pic=False):
#显示视频信息和封面图片
#Show infomations and the cover oicture of the video
        if show_pic:
            headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
            if not pic_dir:
                self.pic_dir='./'+self.info['categories'][0]
            else:
                self.pic_dir=pic_dir
            if not os.path.exists(self.pic_dir):
                os.mkdir(self.pic_dir)
            self.pic_path=self.pic_dir+'/'+self.title+'.jpg'
            with open(self.pic_path,'wb') as f:
                f.write(requests.get(self.cover,headers=headers).content)
            with Image.open(self.pic_path) as img:
                img.show()
        print('Video: ID '+self.video_id+' '+self.title,self.mp4add,self.info)
#==============================================================================
#         
#==============================================================================
def list_categories(root='https://www.pornhub.com'):
#列举Pornhub所有的视频分类，返回一个键名为类名的字典和一个属于类名的list，字典的值是tuple，包含入口URL，视频数，赋予的ID
#Enumerate all categories of PornHub,return a dictionary whose keys are names of categories and a list of categories names, the values of the dics is a tuple,contain entrance url, number of videos, a given ID
    headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    cate_root=root+'/categories'
    r_class=r'<div class="category-wrapper">\n\t\t\t\t\t\t<a href=".*?" alt="(.*?)" class="js-mxp"'
    r_url=r'<div class="category-wrapper">\n\t\t\t\t\t\t<a href="(.*?)" alt=".*?" class="js-mxp"'
    r_num=r'<span>.<var>(\d*?)</var>.</span></a>'
    res=requests.get(cate_root,headers=headers)
    html_text=res.text
    class_list=re.findall(r_class,html_text)
    url_list=re.findall(r_url,html_text)
    num_list=re.findall(r_num,html_text)
    category_params={c:(root+u,int(n),ID+1) for c,u,n,ID in zip(class_list,url_list,num_list,range(len(class_list)))}
    return category_params,class_list
def init_categories_p(category_params={},name_list=['']):
    #实例化category的并行实现
    #A parallel implemention of instantiating categories
    freeze_support()
    pool=Pool(cpu_count())
    results=[]
    for name in name_list:
        results.append(pool.apply_async(category,(name,)+category_params.get(name)))
    pool.close()
    pool.join()
    return [result.get() for result in results]
def init_categories_s(category_params={},name_list=['']):
    return [category(*(name,)+category_params.get(name)) for name in name_list]
def get_videoadd(url='',page=0,category_id=0):
    #从视频列表网页抓取视频名称、封面和播放页的地址
    #Getting name,cover,and the url of play page of the video from a list page.
    r_u=r'<li class="videoblock videoBox[\s\S]*?\t<a href="(.*?)" title=".*?" class="img"'
    r_t=r'<li class="videoblock videoBox[\s\S]*?\t<a href=".*?" title="(.*?)" class="img"'
    r_c=r'\tdata-mediumthumb="(.*?)"\n'
    headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    t=requests.get(url,params={'page':page},headers=headers).text
    t_body=t[t.find('<ul class="nf-videos videos search-video-thumbs">'):]
    t_l=re.findall(r_t,t_body)
    return [(title,add,cover,'.'.join([str(category_id),str(page),str(ID+1)])) for title,add,cover,ID in zip(t_l,re.findall(r_u,t_body),re.findall(r_c,t_body),range(len(t_l)))]
def get_video(videopage):
    #从播放页抓取视频详情，返回一个图片来了包括不同质量的MP4文件地址的一个字典，时长(秒)，一个包含浏览数、赞/踩比率和数量以及所属分类的字典。可单独使用。
    #Crawling detail of the video, return a tuple which has a dict of MP4 file's address of different qualities, the duration(second),a dict contains number of views, the rate and number of votes Up/Down.
    
    headers={'use-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    r_v=r'"quality":".*?","videoUrl":"(.*?)"}'
    r_quality=r'quality":"(\d*?)","videoUrl":".*?"}'
    r_duration=r'"video_duration":"(\d.*?)"'
    r_view=r'<div class="views"><span class="count">(.*?)</span>'
    r_percent=r'<span class="percent">(.*?)</span>'
    r_up=r'<span class="votesUp">(.*?)</span>'
    r_down=r'<span class="votesDown">(.*?)</span>'
    r_cate=r'<a href="/video.*?" onclick="ga.*?;">(.*?)</a>'
    html_text=requests.get('https://www.pornhub.com'+videopage,headers=headers).text
    l_v=list(map(lambda x:x.replace('\\',''),re.findall(r_v,html_text)))
    l_q=re.findall(r_quality,html_text)
    add={q:v for q,v in zip(l_q,l_v)}
    duration=int(re.findall(r_duration,html_text)[0])
    info={'views':re.findall(r_view,html_text)[0],'percent':re.findall(r_percent,html_text)[0],'up':re.findall(r_up,html_text)[0],'down':re.findall(r_down,html_text)[0],'categories':re.findall(r_cate,html_text)}
    return (add,duration,info)
