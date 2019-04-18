# -*- coding: utf-8 -*-

'''
    配置文件
    *所有配置规定小写，以下划线连接单词
'''

# DEBUG 模式 : 开发模式 = True , 生产模式 = False
DEBUG = True

#-----------------------------------

# 数据库配置
host    = 'localhost'    #数据库地址
username = 'root'   #数据库用户名
password = 'root'   #数据库密码
dbname = 'xxxxxxx'     #数据库名称

# 开启的线程数
thread_sum = 10
# 每个分类最大抓取数量
max_spider = 100
# socket 超时时间
socket_time_out = 30
# http 请求超时时间
http_time_out = 30
# 请求头
user_agent = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.9'
}
# cookies 设置
cookies = {
    'language':'cn_CN',
    '91username':'xxxxxxxxx',
    'USERNAME':'c395poj7OxiKyVpcOcTghTDBQ%2FSfxyyGpnVqDrK1ThtyaNDB',
    'DUID':'4eed6MA5lbsgM8e1rRFwPjVXHO7bZon47wrDAHl12%2BrRtyjs',
    'CLIPSHARE':'oso155lcnujvsoeenantocjph4',
    '__cfduid':'dd51deb603cb7dd323335fbe6a1c376bd1512899301',
    '__dtsu':'2DE7B66BE9022D5AB22D00B502DF28CA'
}
# 日志文件文件名
log_name = 'running.log'
# 推送地址
server_put_url = 'http://xxxxxxxxx/server/put.php'

# 视频类型
vod_type = [
    'online',
    'download'
]
# 全局类型
movie_type = [
    'nocode',   #无码
    'code',     #有码
    'omei',     #欧美
    'selfie'    #自拍
]
# 播放类型
online_type = [
    'm3u8',     #m3u8
    'mp4'       #mp4 直连
]

# 爬取站点设置 ----------------------------
    # 格式 ： 爬虫名_配置名
#---------------------------------------
########################################
# 91配置
pron91_root = 'http://91.7h5.space'    #站点根域名
pron91_start_url = '/v.php?next=watch&page=1'    #爬取起始页面
# 91配置 END
########################################
# 桃隐社区
taoyin_root = 'http://v.taoy77.info'    #站点根域名
taoyin_start_urls = [                   #依次循环列表
    '/forum-69-1.html',  #在线中短片
    '/forum-72-1.html',  #中短日韩
    '/forum-73-1.html'   #日本AV
]
#加密地址 (前台显示进行解密)
def taoyin_video(vid):
    return 'http://120.52.72.21/adultvideo.science/media/videos/iphone/${0}$.mp4'.format(vid)
def taoyin_image(vid):
    return 'http://lu.shuiqingqing.net/media/videos/tmb/${0}$/default.jpg'.format(vid)
#AV加密地址
def taoyin_video_av(v_string):
    v_arr = v_string.split(',')
    return 'http://cdn.hkcdn.xyz/d/file/{0}.mp4'.format(v_arr[0])
def taoyin_image_av(v_string):
    v_arr = v_string.split(',')
    return 'http://www.uuge1.com/e/data/tmp/titlepic/{0}.jpg'.format(v_arr[1])
# 桃隐社区 END
########################################
# 啪啪社区
papax_root = 'http://www.papax.info'    # 站点根域名
papax_start_urls = [
    '/guochanzipai/index.html',      # 国产自拍
    '/hanguomeimei/index.html',      # 韩国美眉
    '/ribenAV/index.html',           # 日本AV
    '/oumeixingai/index.html'        # 欧美SEX
]
# 啪啪社区 END
########################################
# AV911
av911_root = 'http://av911.org'      # 站点根域名
av911_start_urls = [
    '/?m=vod-type-id-16.html',       # 日本无码
    '/?m=vod-type-id-17.html',       # 中文无码
    '/?m=vod-type-id-18.html',       # 中文有码
    '/?m=vod-type-id-19.html',       # 欧美无码
    '/?m=vod-type-id-20.html'        # 自拍视频
]
av911_video_api = 'http://98.126.68.82:81/b/cdn.php?vid='   # 视频API
# AV911 END
########################################
# 桃花族
taohuazu_root = 'http://thzthz.net'  # 站点根域名
taohuazu_start_urls = [
    '/forum-181-1.html',             # 亚洲无码
    '/forum-220-1.html',             # 亚洲有码
    '/forum-182-1.html',             # 欧美无码
]
taohuazu_bt_api = '/forum.php?mod=attachment&'  # bt API
# 桃花族 END
########################################
# 性吧
# 杏吧论坛.com
# https://www.momoim00.com
# https://www.luntan88qq.com
sex8_root = 'https://www.mm88qq.net'      # 网站根域名
sex8_start_urls = [
    '/forum-723-1.html',                        # 无码
    '/forum-280-1.html',                        # 无码 (图文并茂)
    '/forum-713-1.html',                        # 有码
    '/forum-525-1.html',                        # 欧美
]
# 性吧 END
########################################
