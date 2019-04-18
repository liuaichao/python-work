import requests
from bs4 import BeautifulSoup

url = "https://www.cnblogs.com/cate/python/"
rep = requests.get(url)
soup = BeautifulSoup(rep.text, 'html.parser')
content = soup.select("div[class='post_item_body']")
# print(content)
for i in content:
     i = i.get_text()
     print(i)