import urllib
import re
import urllib.request

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 将opener安装为全局
urllib.request.install_opener(opener)

search = input('输入你想搜索的作者（中文名）:')
search = urllib.parse.quote(search)
print('https://book.douban.com/tag/' + str(search))
data3 = urllib.request.urlopen('https://book.douban.com/tag/' + str(search)).read().decode("utf-8")

# 构建对应作者作品的正则表达式
bookwebPattern = '<h2 class="">\n\s\s\s\s\s\s\s\s\s\s\s\s\s\s<a href="(.*?)" title="'
bookweb = re.compile(bookwebPattern).findall(data3)

websOfBookReview = []
numsOfShortReview = []
booknameList = []
flag = '1'

print('该作者主要作品：')
# 依次打印每部作品名称及对应标签
for i in bookweb:
    data4 = urllib.request.urlopen(i).read().decode("utf-8")
    # 构建对应作者特定作品名称的正则表达式
    booknamePattern = 'v:itemreviewed">(.*?)<'
    bookname = re.compile(booknamePattern).findall(data4)
    booknameList.append(bookname)
    print('书名：', bookname, i)
    # 构建对应作者特定作品标签的正则表达式
    certainBookTagPattern = 'tag" href="/tag/(.*?)">'
    certainBookTag = re.compile(certainBookTagPattern).findall(data4)
    # 构建对应作者特定作品总标签数的正则表达式
    tagnumsPattern = '豆瓣成员常用的标签(.*?)<'
    tagnums = re.compile(tagnumsPattern).findall(data4)
    print('总标签数:', str(tagnums), '主要标签：', certainBookTag)
    # 构建对应作者特定作品评论网页的正则表达式
    readerPattern = '<a\shref="(.*?)">全部(.*?)条'
    reader = re.compile(readerPattern).findall(data4)
    # 将几部作品的读者评论网页记录在websOfBookReview列表，待呈现完作者及主要作品的主要情况后再据需统计某几部作品读者情况
    websOfBookReview.append(reader[0][0])
    numsOfShortReview.append(reader[0][1])
    if len(booknameList) % 10 and len(booknameList) > 10:
        flag = input('want to stop analysizing more users? press 0 to quit else press 1:')
        if flag == '0':
            break
    print('短评网页+数量:', reader[0][0], reader[0][1], '书评数量:', reader[1][1], '\n')
for i in range(len(websOfBookReview)):
    print(booknameList[i], '前20位评论者个人页面展示:')
    data5 = urllib.request.urlopen(websOfBookReview[i]).read().decode("utf-8")
    bookname = re.compile(booknamePattern).findall(data4)
    # 构建对应特定读者个人主页的正则表达式
    webOfCertainUserPattern = '<a title=".*?"\shref="(.*?)>\s*?<img'
    webOfCertainUser = re.compile(webOfCertainUserPattern).findall(data5)
    print(webOfCertainUser)

numOfCountedUsers = 0
addressList = []
bookcomment = []
num = '1'  # 停止标识符，当觉得时间等的够久了或收集的数据足够多了就可输入0以停止爬虫
print('以下为', booknameList[0], '读者情况的具体展示,要查看该作者其他书籍读者情况', \
      '请将源代码booknameList[0]与numsOfShortReview[0])//20中的0改为其他较小的数字。\n')
for i in range(int(numsOfShortReview[0]) // 20):  # ①评论绝大多数为短评，因爬虫时间有限只考虑短评。②每个评论页有20个用户
    # ③这里numsOfShortReview[0]指要对第一本书读者进行统计，事实上numsOfShortReview[1]也行（对第二本书读者进行统计）
    if num == '0':
        break
    data5 = urllib.request.urlopen(websOfBookReview[0] + 'hot?p=' + str(i)).read().decode("utf-8")
    bookname = re.compile(booknamePattern).findall(data5)
    # 构建对应特定作品读者评论的正则表达式
    commentPattern = '<p class="comment-content">\s.*?\n.*?<span class="short">(.*?)<\/span>'
    comment = re.compile(commentPattern).findall(data5)
    bookcomment.append(comment)
    # 构建对应特定读者个人主页的正则表达式
    webOfCertainUserPattern = '<a title=".*?"\shref="(.*?)">\s*?<img '
    webOfCertainUserTemp = re.compile(webOfCertainUserPattern).findall(data5)

    for j in webOfCertainUserTemp:
        data6 = urllib.request.urlopen(j).read().decode("utf-8")
        bookname = re.compile(booknamePattern).findall(data6)
        # 构建对应特定读者个人主页居住地及加入日期的正则表达式
        InfoUserPattern = '常居:&nbsp;<a href=".*?>(.*?)<\/a>.*?\n\n.*?class.*?>(.*?)<.*?>(.*?)<\/div>'
InfoUser = re.compile(InfoUserPattern).findall(data6)
print('读者个人页面:', j, '地址,nickname,加入时间(有些用户未填地址):', InfoUser)
if InfoUser != []:
    addressList.append(InfoUser[0][0])
    numOfCountedUsers += 1
if numOfCountedUsers % 10 == 0:
    num = input('want to stop analysizing more users? press 0 to quit else press 1:')
if num == '0':
    exit()
print("\n第二部分--已爬取读者的常住地分布:(因时间关系部分读者未爬故未统计)")
