# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import xlwt

urls = ['http://list.iqiyi.com/www/1/4-------------11-{}-1-iqiyi--.html'.format(str(i)) for i in range(1, 2)]


def get_webData(url):
    data_info = []
    time.sleep(3)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.site-piclist_info > div.mod-listTitle_left > p > a')
    imgs = soup.select('div.site-piclist_pic > a > img')
    actors = soup.select('div.site-piclist_info > div.role_info')
    spans = soup.select('div.site-piclist_info > div.mod-listTitle_left > span')
    for title, img, actors, span in zip(titles, imgs, actors, spans):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'actors': list(actors.stripped_strings),
            'span': span.get_text()
        }
        # print(data)
        dataVal_list.append(data.values())
        data_info.append(data)
    # print(list(data.keys()))
    for m, n in enumerate(list(data.keys())):
        sheet.write(0, m, n)

    for i, p in enumerate(dataVal_list):
        for j, q in enumerate(p):
            # print(q)
            sheet.write(i + 1, j, q)
    return data_info


def main():
    for url in urls:
        data_info = get_webData(url)
        # print(data_info)
        print('---------------------------\n')


if __name__ == '__main__':
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet('Movies')
    dataVal_list = []
    main()
    f.save('Movies.xls')