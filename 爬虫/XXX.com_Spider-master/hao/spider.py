# -*- coding: utf-8 -*-

try:
    from hao.setting import *
    from hao.util import *
    from hao.database import insert,is_url
    import requests, re, time, socket, os,threading
    from requests.adapters import HTTPAdapter
    from queue import Queue
    from bs4 import BeautifulSoup
except ImportError as e:
    print("模块导入 Error ==> spider.py [{0}]".format(e))
    exit()

# socket 超时
socket.setdefaulttimeout(socket_time_out)

# 获取网页源码
def download_html(url,result_type=None):
    try:
        try:
            res = requests.session()
            res.mount('http://', HTTPAdapter(max_retries=3))
            res.mount('https://', HTTPAdapter(max_retries=3))
            request = requests.get(url=url, headers=user_agent,timeout=http_time_out,cookies=cookies)
            if request.status_code == 200:
                if result_type=='content':
                    return request.content.decode('utf-8')
                elif result_type=='sex8':
                    return unzip_html(request.content)
                else:
                    return request.text
            else:
                return ""
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, socket.timeout,
                requests.packages.urllib3.exceptions.ReadTimeoutError, requests.exceptions.ReadTimeout) as e:
            if DEBUG:
                error("获取源码超时 Error ===> [ {0} ] 暂停后重启 {1}".format(url, e))
            time.sleep(10)
            download_html(url=url)
    except Exception:
        return ""
# 线程类
class Thread(threading.Thread):

    def __init__(self,func):
        super(Thread,self).__init__()
        self.do = func

    def run(self):
        self.do()

#-------------strat---爬虫源代码-------------
'''
    一个站点一个爬虫（一个类）
'''
# 最大爬取数
MAX_RUNSUM = 0
# 重置队列
QULIST = Queue()
# 下一页链接
NEXT_URL = ''
# 爬取总数
RUN_COUNT = 0

# 在线------------------------------------------------------------------------------------------------------------------

# 91porn
class Pron91:

    def pron91_do(self):
        global QULIST
        global RUN_COUNT
        while not QULIST.empty():
            vinfo = QULIST.get()
            play_html = download_html(vinfo['yuan_url'])
            if play_html != '' and len(play_html) > 0:
                v_url = re.findall(r'<source src="(.*?)" type=\'video\/mp4\'>', play_html, re.S)
                if v_url:
                    vinfo['play_url'] = v_url[0]
                    vinfo['description'] = "暂无简介"
                    # 插入数据
                    sql = get_sql(vinfo, vod_type[0])
                    insert(sql=sql)
                    RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()


    # 获取列表
    def get_list(self,url):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        html = download_html(url=url)
        if html != '' and len(html) > 0:
            soup = BeautifulSoup(html,'lxml')
            # 匹配下一页链接
            next_html = soup.find('div',class_='pagingnav')
            next_url = '/v.php'+re.findall(r'<a href="(.*?)">',str(next_html),re.S)[-1]
            NEXT_URL = pron91_root + unhtml(next_url)
            # 匹配下一页链接 END
            # 视频列表源码
            list_html = soup.find_all('div',class_='listchannel')
            threads = []
            for item in list_html:
                vinfo = {}
                try:
                    info = re.findall(r'<img src="(.*?)" title="(.*?)" width="120"/>', str(item), re.S)
                    if info:
                        info = info[0]
                        try:
                            time_long = re.findall(r'<span class="info">时长:</span>(.*?)<br/>', str(item), re.S)
                        except Exception as e:
                            if DEBUG:
                                error("[pron91] 匹配时长Error ==> [spider.py get_list() ({0})]".format(e))
                            time_long = '暂无时长'
                        finally:
                            # 视频播放页链接
                            try:
                                link = re.findall(r'<a href="(.*?)" target="blank">', str(item), re.S)

                                if link and time_long and info:
                                    vinfo['vkey'] = ikey()
                                    vinfo['title'] = info[1]
                                    vinfo['en_title'] = en(vinfo['title'])
                                    vinfo['images'] = info[0]
                                    vinfo['vod_long'] = strip(time_long[0])
                                    vinfo['yuan_url'] = unhtml(link[0])
                                    vinfo['play_type'] = online_type[1]
                                    vinfo['movie_type'] = movie_type[3]
                                    vinfo['inputtime'] = getTime()

                                    # 如果当前链接没有采集过，加入队列
                                    if not is_url(vinfo['yuan_url'],vod_type[0]):
                                        # 没采集过,加入队列 , 并且没有超过最大爬取数
                                        if MAX_RUNSUM < max_spider:
                                            QULIST.put(vinfo)
                                            MAX_RUNSUM += 1  # 最大爬取数递增
                                        else:
                                            is_collection = True
                                    else:
                                        is_collection = True
                            except Exception as e:
                                if DEBUG:
                                    error("[pron91] 播放页匹配Error ==> [spider.py get_list() ({0})]".format(e))

                except Exception as e:
                    if DEBUG:
                        error("[pron91] 匹配信息Error ==> [spider.py get_list() ({0})]".format(e))

            # 开启线程
            for v in range(thread_sum):
                t = Thread(self.pron91_do)
                t.setDaemon(True)
                t.start()
                threads.append(t)
                # 线程
            for tobj in threads:
                tobj.join()

            # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.get_list(NEXT_URL)
            else:
                # 重置
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置
            MAX_RUNSUM = 0
            NEXT_URL = ''

    def main(self):
        self.get_list(pron91_root + pron91_start_url)


# 91porn---END

# 桃隐社区
class Taoyin:

    def vod_list(self,url=None,video_type=None):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        list_html = download_html(url=url)
        if list_html != '':
            soup = BeautifulSoup(list_html,'lxml')
            #解析下一页
            next_url = soup.find('a',class_="nxt")
            if next_url:
                NEXT_URL = taoyin_root + '/' + unhtml(next_url['href'])
            else:
                NEXT_URL = ''
            #解析下一页 END

            #解析列表
            ul_list = soup.find_all('ul',id="waterfall")
            soup = BeautifulSoup(str(ul_list), 'lxml')
            li_list = soup.find_all('li')
            threads = []
            for v in li_list:
                vinfo = {}
                soup = BeautifulSoup(str(v), 'lxml')
                v_url = soup.a['href']
                # 将v_url加入队列
                if not is_url(url=v_url,t=vod_type[0]):
                    # 链接没有采集过
                    if MAX_RUNSUM < max_spider:
                        QULIST.put(v_url)
                        MAX_RUNSUM += 1  # 最大爬取数递增
                    else:
                        is_collection = True
                else:
                    is_collection = True

            # 开启多线程
            for v in range(thread_sum):
                if video_type =='av':
                    t = Thread(self.get_vod_av)
                else:
                    t = Thread(self.get_vod)
                t.setDaemon(True)
                t.start()
                threads.append(t)
            # 线程
            for tobj in threads:
                tobj.join()

            # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.vod_list(url=NEXT_URL,video_type=video_type)
            else:
                # 重置爬取数量
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置爬取数量
            MAX_RUNSUM = 0
            NEXT_URL = ''


    def get_vod(self):
        global QULIST
        global RUN_COUNT
        while not QULIST.empty():
            vinfo = {}
            vod_url = QULIST.get()
            url = taoyin_root + '/' + vod_url
            # 解析单个视频
            html = download_html(url=url)
            if html:
                soup = BeautifulSoup(html,'lxml')
                vid_html1 = soup.find_all('div',id="tylongvideo")
                vid = 0
                if vid_html1:
                    vid = vid_html1[0]['datav']
                else:
                    vid_html2 = soup.find_all('div', id="tylongvideo")
                    if vid_html2:
                        vid = vid_html2[0]['datav']
                title_html = soup.find_all(id="thread_subject")
                if title_html and vid != 0:
                    vinfo['vkey'] = ikey()
                    vinfo['title'] = title_html[0].get_text()
                    vinfo['en_title'] = en(vinfo['title'])
                    vinfo['description'] = "暂无简介"
                    vinfo['images'] = taoyin_image(vid)
                    vinfo['vod_long'] = ""
                    vinfo['yuan_url'] = vod_url
                    vinfo['play_url'] = taoyin_video(vid)
                    vinfo['play_type'] =  online_type[1]
                    vinfo['movie_type'] = movie_type[3]
                    vinfo['inputtime'] = getTime()

                    # 插入数据
                    sql = get_sql(vinfo,vod_type[0])
                    insert(sql=sql)
                    RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()

    def get_vod_av(self):
        global QULIST
        global RUN_COUNT
        while not QULIST.empty():
            vinfo = {}
            vod_url = QULIST.get()
            url = taoyin_root + '/' + vod_url
            # 解析单个视频
            html = download_html(url=url)
            if html:
                soup = BeautifulSoup(html, 'lxml')
                vid_html1 = soup.find_all('div', id="tylongvideo")
                vid = 0
                if vid_html1:
                    vid = vid_html1[0]['datav']
                else:
                    vid_html2 = soup.find_all('div', id="tylongvideo")
                    if vid_html2:
                        vid = vid_html2[0]['datav']
                title_html = soup.find_all(id="thread_subject")
                if title_html and vid != 0:
                    vinfo['vkey'] = ikey()
                    vinfo['title'] = title_html[0].get_text()
                    vinfo['en_title'] = en(vinfo['title'])
                    vinfo['description'] = "暂无简介"
                    vinfo['images'] = taoyin_image_av(vid)
                    vinfo['vod_long'] = ""
                    vinfo['yuan_url'] = vod_url
                    vinfo['play_url'] = taoyin_video_av(vid)
                    vinfo['play_type'] = online_type[1]
                    vinfo['movie_type'] = movie_type[3]
                    vinfo['inputtime'] = getTime()

                    # 插入数据
                    sql = get_sql(vinfo,vod_type[0])
                    insert(sql=sql)
                    RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()

    def main(self):
        global MAX_RUNSUM
        for v in taoyin_start_urls:
            if v != taoyin_start_urls[-1]:
                MAX_RUNSUM = 0
                self.vod_list(taoyin_root + v)
            else:
                # 单独处理
                MAX_RUNSUM = 0
                self.vod_list(taoyin_root + v,video_type='av')

# 桃隐社区---END

# 啪啪社区
class Papax:

    def vod_list(self,url,movie_type=None):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        list_html = download_html(url=url,result_type='content')
        if list_html:
            soup = BeautifulSoup(list_html,'lxml')
            # 提取下一页
            next_html = soup.find('li',class_="next-page")
            if next_html:
                next_url = papax_root + next_html.a['href']
                NEXT_URL = next_url
            else:
                NEXT_URL = ''
            # 提取下一页 END

            # 解析列表
            vod_list = soup.find_all('article',class_="excerpt")
            threads = []
            for v in vod_list:
                vinfo = {}
                soup = BeautifulSoup(str(v),'lxml')
                vinfo['yuan_url'] = soup.a['href']
                if not is_url(vinfo['yuan_url'],vod_type[0]):
                    vinfo['title'] = soup.img['alt']
                    vinfo['images'] = papax_root + soup.img['src']
                    vinfo['movie_type'] = movie_type
                    # 链接没有采集过
                    if MAX_RUNSUM < max_spider:
                        QULIST.put(vinfo)
                        MAX_RUNSUM += 1  # 最大爬取数递增
                    else:
                        is_collection = True
                else:
                    is_collection = True

            # 开启多线程
            for v in range(thread_sum):
                t = Thread(self.get_vod)
                t.setDaemon(True)
                t.start()
                threads.append(t)
            # 线程
            for tobj in threads:
                tobj.join()

            # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.vod_list(url=NEXT_URL,movie_type=movie_type)
            else:
                # 重置爬取数量
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置爬取数量
            MAX_RUNSUM = 0
            NEXT_URL = ''

    def get_vod(self):
        global QULIST
        global RUN_COUNT
        while not QULIST.empty():
            vinfo = QULIST.get()
            vod_url = papax_root + vinfo['yuan_url']
            html = download_html(vod_url)
            if html:
                soup = BeautifulSoup(html,'lxml')
                vod_iframe = soup.find('iframe')
                if vod_iframe:
                    play_iframe_url = papax_root + vod_iframe['src']
                    play_iframe_html = download_html(play_iframe_url)
                    if play_iframe_html:
                        soup = BeautifulSoup(play_iframe_html,'lxml')
                        video_url = soup.find('video')
                        if video_url:
                            video_url = video_url['src']
                            video_url = papax_root + video_url.replace('../../..','')

                            vinfo['vkey'] = ikey()
                            vinfo['play_url'] = video_url
                            vinfo['play_type'] = online_type[1]
                            vinfo['en_title'] = en(vinfo['title'])
                            vinfo['description'] = "暂无简介"
                            vinfo['vod_long'] = ''
                            vinfo['inputtime'] = getTime()

                            sql = get_sql(vinfo, vod_type[0])
                            # 插入到数据库
                            insert(sql=sql)
                            RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()

    def main(self):
        global MAX_RUNSUM
        for v in papax_start_urls:
            if v == papax_start_urls[0] or v == papax_start_urls[1]:
                MAX_RUNSUM = 0
                self.vod_list(papax_root + v , movie_type[-1])

            if v == papax_start_urls[2]:
                MAX_RUNSUM = 0
                self.vod_list(papax_root + v , movie_type[1])

            if v == papax_start_urls[-1]:
                MAX_RUNSUM = 0
                self.vod_list(papax_root + v , movie_type[-2])

# 啪啪社区---END

# AV911
class Av911:

    def vod_list(self,url,mov_type=None):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        list_html = download_html(url=url)
        if list_html:
            soup = BeautifulSoup(list_html,'lxml')
            # 匹配下一页
            next_html = soup.find('a',class_="pagelink_a")
            if next_html:
                NEXT_URL = av911_root + next_html['href']
            else:
                NEXT_URL = ''
            # 匹配下一页 END
            # 解析列表页
            list_arr = soup.find_all('li',class_="thumb item")
            threads = []
            for i in list_arr:
                vinfo = {}
                soup = BeautifulSoup(str(i),'lxml')
                vinfo['yuan_url'] = soup.a['href']
                if not is_url(vinfo['yuan_url'],vod_type[0]):
                    vinfo['title'] = soup.find('span', class_="title").get_text()
                    vinfo['images'] = soup.img['data-original']
                    vinfo['movie_type'] = mov_type
                    # 链接没有采集过
                    if MAX_RUNSUM < max_spider:
                        # 添加到队列
                        QULIST.put(vinfo)
                        MAX_RUNSUM += 1  # 最大爬取数递增
                    else:
                        is_collection = True
                else:
                    is_collection = True

            # 开启多线程
            for v in range(thread_sum):
                t = Thread(self.get_vod)
                t.setDaemon(True)
                t.start()
                threads.append(t)
            # 线程
            for tobj in threads:
                tobj.join()

            # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.vod_list(url=NEXT_URL,mov_type=mov_type)
            else:
                # 重置爬取数量
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置爬取数量
            MAX_RUNSUM = 0
            NEXT_URL = ''

    def get_vod(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            video_url = av911_root + vinfo['yuan_url']
            video_html = download_html(video_url)
            if video_html:
                soup = BeautifulSoup(video_html,'lxml')
                video_script = soup.find('div',id="playview")
                video_id = re.findall(r'mac_url=unescape\(\'(.*?)\'\)',str(video_script),re.S)
                if video_id:
                    video_url = av911_video_api + video_id[0]
                    # vinfo['play_url'] = location(video_url)
                    vinfo['play_url'] = video_url
                    vinfo['en_title'] = en(vinfo['title'])
                    vinfo['vkey'] = ikey()
                    vinfo['description'] = "暂无简介"
                    vinfo['vod_long'] = ''
                    vinfo['play_type'] = online_type[1]
                    vinfo['inputtime'] = getTime()

                    # 插入到数据库
                    sql = get_sql(vinfo,vod_type[0])
                    insert(sql)
                    RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()

    def main(self):
        global MAX_RUNSUM
        for v in av911_start_urls:

            if v == av911_start_urls[0] or v == av911_start_urls[1]:
                MAX_RUNSUM = 0
                self.vod_list(av911_root + v , movie_type[0])

            if v == av911_start_urls[2]:
                MAX_RUNSUM = 0
                self.vod_list(av911_root + v , movie_type[1])

            if v == av911_start_urls[3]:
                MAX_RUNSUM = 0
                self.vod_list(av911_root + v , movie_type[2])

            if v == av911_start_urls[-1]:
                MAX_RUNSUM = 0
                self.vod_list(av911_root + v , movie_type[-1])


# AV911---END


# 下载------------------------------------------------------------------------------------------------------------------

# Taohuazu
class Taohuazu:

    def vod_list(self,url,mov_type=None):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        list_html = download_html(url=url)
        if list_html:
            soup = BeautifulSoup(list_html, 'lxml')
            # 匹配下一页
            next_html = soup.find('a', class_="nxt")
            if next_html:
                NEXT_URL = taohuazu_root + '/' + next_html['href']
            else:
                NEXT_URL = ''
            # 匹配下一页 END

            # 解析列表页
            list_arr = soup.find_all('tbody',attrs={'id':re.compile('normalthread_[0-9]*')})
            threads = []
            for v in list_arr:
                vinfo = {}
                soup = BeautifulSoup(str(v),'lxml')
                vodbt_url = soup.find('a')['href']
                if not is_url(vodbt_url , vod_type[1]):
                    if MAX_RUNSUM < max_spider:
                        # 添加到队列
                        vinfo['yuan_url'] = vodbt_url
                        vinfo['movie_type'] = mov_type
                        QULIST.put(vinfo)
                        MAX_RUNSUM += 1  # 最大爬取数递增
                    else:
                        is_collection = True
                else:
                    is_collection = True

            # 开启多线程
            for v in range(thread_sum):
                t = Thread(self.get_vodbt)
                t.setDaemon(True)
                t.start()
                threads.append(t)
            # 线程
            for tobj in threads:
                tobj.join()

            # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.vod_list(url=NEXT_URL,mov_type=mov_type)
            else:
                # 重置爬取数量
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置爬取数量
            MAX_RUNSUM = 0
            NEXT_URL = ''

    def get_vodbt(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            vodbt_url = taohuazu_root + '/' + vinfo['yuan_url']
            vodbt_html = download_html(vodbt_url)
            if vodbt_html:
                soup = BeautifulSoup(vodbt_html,'lxml')
                vinfo['title'] = soup.find('span', id="thread_subject").get_text()
                vodbt_html = str(soup.find('div',class_="t_fsz"))
                soup = BeautifulSoup(vodbt_html,'lxml')
                vinfo['vkey'] = ikey()
                vinfo['en_title'] = en(vinfo['title'])
                description = re.findall(r'<td class="t_f" id="postmessage_[0-9]*">(.*?)<ignore_js_op>',vodbt_html,re.S)
                if description:
                    vinfo['description'] = html(strip(description[0]))
                else:
                    vinfo['description'] = '暂无简介'
                # 预览图片
                vinfo['images'] = ''
                images_arr = soup.find_all('img',attrs={'class':'zoom'})
                for img in images_arr:
                    vinfo['images'] += img['file'] + '$'

                # bt 种子链接
                bt_html = soup.find_all("dl", class_="tattl")
                vinfo['bt_url'] = ''
                for item_bt in bt_html:
                    soup = BeautifulSoup(str(item_bt), "lxml")
                    aid = str(soup.find("a")['href']).split('?')[1]
                    vinfo['bt_url'] += taohuazu_bt_api + aid + "$"

                vinfo['inputtime'] = getTime()
                # 插入到数据库
                sql = get_sql(vinfo, vod_type[1])
                insert(sql)
                RUN_COUNT += 1

            time.sleep(1)
            QULIST.task_done()

    def main(self):
        global MAX_RUNSUM
        for v in taohuazu_start_urls:
            if v == taohuazu_start_urls[0]:
                MAX_RUNSUM = 0
                self.vod_list(taohuazu_root + v , movie_type[0])

            if v == taohuazu_start_urls[1]:
                MAX_RUNSUM = 0
                self.vod_list(taohuazu_root + v , movie_type[1])

            if v == taohuazu_start_urls[2]:
                MAX_RUNSUM = 0
                self.vod_list(taohuazu_root + v , movie_type[2])

# Taohuazu---END

# Sex8
class Sex8:

    def get_vodbt_1(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            vodbt_url = sex8_root + '/' + vinfo['yuan_url']
            vodbt_html = download_html(vodbt_url,result_type='sex8')
            if vodbt_html:
                soup = BeautifulSoup(vodbt_html, 'lxml')
                vinfo['title'] = soup.find('span', id="thread_subject").get_text()
                vodbt_html = str(soup.find('td',attrs={'id':re.compile('postmessage_[0-9]*')}))
                description = re.findall(r'【影片(.*?)<img',vodbt_html,re.S)
                if description:
                    vinfo['description'] = html("【影片{0}".format(description[0]))
                else:
                    vinfo['description'] = '暂无简介'

                # 预览图片
                vinfo['images'] = ''
                images_arr = soup.find_all('img', attrs={'class':'zoom','lazyloadthumb':'1'})[:-1]
                if images_arr:
                    try:
                        for img in images_arr:
                            vinfo['images'] += img['file'] + '$'

                        # bt 种子
                        vinfo['bt_url'] = soup.find('span',attrs={'id':re.compile('attach_[0-9]*')}).a['href']

                        vinfo['vkey'] = ikey()
                        vinfo['en_title'] = en(vinfo['title'])
                        vinfo['inputtime'] = getTime()

                        # 插入到数据库
                        sql = get_sql(vinfo, vod_type[1])
                        insert(sql)
                        RUN_COUNT += 1

                    except KeyError as e:
                        pass

            time.sleep(1)
            QULIST.task_done()


    def get_vodbt_2(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            vodbt_url = sex8_root + '/' + vinfo['yuan_url']
            vodbt_html = download_html(vodbt_url,result_type='sex8')
            if vodbt_html:
                soup = BeautifulSoup(vodbt_html, 'lxml')
                vinfo['title'] = soup.find('span', id="thread_subject").get_text()
                vodbt_html = str(soup.find('td',attrs={'id':re.compile('postmessage_[0-9]*')}))
                description = re.findall(r'【影片(.*?)</div>',vodbt_html,re.S)
                if description:
                    vinfo['description'] = html("【影片{0}".format(description[0]))
                else:
                    vinfo['description'] = '暂无简介'

                #预览图片
                vinfo['images'] = ''
                images_arr = soup.find_all('img', attrs={'class':'zoom','lazyloadthumb':'1'})[0:-2]
                if images_arr:
                    if len(images_arr) > 0:
                        try:
                            for img in images_arr:
                                vinfo['images'] += img['file'] + '$'

                            # bt 种子
                            vinfo['bt_url'] = soup.find('span',attrs={'id':re.compile('attach_[0-9]*')})
                            if vinfo['bt_url']:
                                vinfo['bt_url'] = vinfo['bt_url'].a['href']
                                vinfo['vkey'] = ikey()
                                vinfo['en_title'] = en(vinfo['title'])
                                vinfo['inputtime'] = getTime()

                                # 插入到数据库
                                sql = get_sql(vinfo, vod_type[1])
                                insert(sql)
                                RUN_COUNT += 1

                        except KeyError as e:
                            pass

            time.sleep(1)
            QULIST.task_done()

    def get_vodbt_3(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            vodbt_url = sex8_root + '/' + vinfo['yuan_url']
            vodbt_html = download_html(vodbt_url,result_type='sex8')
            if vodbt_html:
                soup = BeautifulSoup(vodbt_html, 'lxml')
                vinfo['title'] = soup.find('span', id="thread_subject").get_text()
                vodbt_html = str(soup.find('div',class_="t_fsz"))
                description = re.findall(r'【影片(.*?)<img',vodbt_html,re.S)
                if description:
                    vinfo['description'] = html("【影片{0}".format(description[0]))
                else:
                    vinfo['description'] = '暂无简介'

                #预览图片
                vinfo['images'] = ''
                images_arr = soup.find_all('img', attrs={'class':'zoom','lazyloadthumb':'1'})
                if images_arr:
                    try:
                        for img in images_arr:
                            vinfo['images'] += img['file'] + '$'

                        # bt 种子
                        vinfo['bt_url'] = soup.find('a', attrs={'id': re.compile('aid[0-9]*')})['href']
                        #
                        vinfo['vkey'] = ikey()
                        vinfo['en_title'] = en(vinfo['title'])
                        vinfo['inputtime'] = getTime()

                        # 插入到数据库
                        sql = get_sql(vinfo, vod_type[1])
                        insert(sql)
                        RUN_COUNT += 1

                    except KeyError as e:
                        pass

            time.sleep(1)
            QULIST.task_done()

    def get_vodbt_4(self):
        global QULIST
        global RUN_COUNT
        vinfo = {}
        while not QULIST.empty():
            vinfo = QULIST.get()
            vodbt_url = sex8_root + '/' + vinfo['yuan_url']
            vodbt_html = download_html(vodbt_url,result_type='sex8')
            if vodbt_html:
                soup = BeautifulSoup(vodbt_html, 'lxml')
                vinfo['title'] = soup.find('span', id="thread_subject").get_text()
                vodbt_html = str(soup.find('div',class_="t_fsz"))
                description = re.findall(r'【影片(.*?)<img',vodbt_html,re.S)
                if description:
                    vinfo['description'] = html("【影片{0}".format(description[0]))
                else:
                    vinfo['description'] = '暂无简介'

                #预览图片
                vinfo['images'] = ''
                images_arr = soup.find_all('img', attrs={'class':'zoom','lazyloadthumb':'1'})
                if images_arr:
                    if len(images_arr) > 0:
                        try:
                            for img in images_arr:
                                vinfo['images'] += img['file'] + '$'

                            # bt 种子
                            vinfo['bt_url'] = soup.find('a', attrs={'id': re.compile('aid[0-9]*')})['href']
                            #
                            vinfo['vkey'] = ikey()
                            vinfo['en_title'] = en(vinfo['title'])
                            vinfo['inputtime'] = getTime()

                            # 插入到数据库
                            sql = get_sql(vinfo, vod_type[1])
                            insert(sql)
                            RUN_COUNT += 1

                        except KeyError as e:
                            pass

            time.sleep(1)
            QULIST.task_done()


    def vod_list(self,url,mov_type=None,sex_type=None):
        is_collection = False
        global NEXT_URL
        global QULIST
        global MAX_RUNSUM
        list_html = download_html(url=url)
        if list_html:
            soup = BeautifulSoup(list_html,'lxml')
            # 匹配下一页
            next_html = soup.find('a', class_="nxt")
            if next_html:
                NEXT_URL = sex8_root + '/' + next_html['href']
            else:
                NEXT_URL = ''
            # 匹配下一页 END

            # 解析列表页
            list_arr = soup.find_all('tbody', attrs={'id': re.compile('normalthread_[0-9]*')})
            threads = []
            for v in list_arr:
                vinfo = {}
                soup = BeautifulSoup(str(v), 'lxml')
                vodbt_url = soup.find('a')['href']
                if not is_url(vodbt_url, vod_type[1]):
                    if MAX_RUNSUM < max_spider:
                        # 添加到队列
                        vinfo['yuan_url'] = vodbt_url
                        vinfo['movie_type'] = mov_type
                        QULIST.put(vinfo)
                        MAX_RUNSUM += 1  # 最大爬取数递增
                    else:
                        is_collection = True
                else:
                    is_collection = True

                    # 开启多线程
            for v in range(thread_sum):
                if sex_type == 1:
                    t = Thread(self.get_vodbt_1)
                elif sex_type == 2:
                    t = Thread(self.get_vodbt_2)
                elif sex_type == 3:
                    t = Thread(self.get_vodbt_3)
                else:
                    t = Thread(self.get_vodbt_4)
                t.setDaemon(True)
                t.start()
                threads.append(t)
                # 线程
            for tobj in threads:
                tobj.join()

                # 等待队列为空 在执行其他操作
            QULIST.join()

        # 检测是否要采集下一页
        if not is_collection:
            if NEXT_URL != '':
                self.vod_list(url=NEXT_URL, mov_type=mov_type,sex_type=sex_type)
            else:
                # 重置爬取数量
                MAX_RUNSUM = 0
                NEXT_URL = ''
        else:
            # 重置爬取数量
            MAX_RUNSUM = 0
            NEXT_URL = ''



    def main(self):
        global MAX_RUNSUM
        for v in sex8_start_urls:
            # 无码
            if v == sex8_start_urls[0]:
                MAX_RUNSUM = 0
                print("无码")
                self.vod_list(sex8_root + v , mov_type=movie_type[0],sex_type=1)
            # 无码 图文并茂
            if v == sex8_start_urls[1]:
                MAX_RUNSUM = 0
                print("图文并茂")
                self.vod_list(sex8_root + v, mov_type=movie_type[0], sex_type=2)
            # 有码
            if v == sex8_start_urls[2]:
                MAX_RUNSUM = 0
                print("有码")
                self.vod_list(sex8_root + v , mov_type=movie_type[1],sex_type=3)
            # 欧美
            if v == sex8_start_urls[-1]:
                MAX_RUNSUM = 0
                print("欧美")
                self.vod_list(sex8_root + v , mov_type=movie_type[2],sex_type=4)

# Sex8---END

#-------------strat---爬虫源代码--END-----------


'''
    启动入口
    执行每一个爬虫类 main() 方法
'''
def run():
    error("--Spider--Start--\n")

    Pron91().main()

    Taoyin().main()

    Papax().main()

    Av911().main()

    Taohuazu().main()

    Sex8().main()

    error("\n--Spider--end--")
