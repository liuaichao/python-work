from bs4 import BeautifulSoup
import requests
from urllib import request
def qq():
    url = "https://hr.tencent.com/position.php?keywords=&tid=0&lid=2156"
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    soup1 = soup.select('tr[class="even"]')
    soup2 = soup.select('tr[class="odd"]')
    soups = soup1+soup2
    print(soups)

    for tr in soups:
        name = tr.select('td')[0].get_text()
        lei =tr.select('td')[1].get_text()
        number = tr.select('td')[2].get_text()
        city = tr.select('td')[3].get_text()
        time = tr.select('td')[4].get_text()
        print(name+"--"+lei+"--"+number+"--"+city+"--"+time)


if __name__ == '__main__':
    qq()