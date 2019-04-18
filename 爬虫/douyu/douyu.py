from selenium import webdriver
import time

def dou(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    lei = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li/div/a/div/div/span[@class="DyListCover-zone"]')
    redu = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li/div/a/div/div/span[@class="DyListCover-hot"]')
    title = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li/div/a/div/div/h3')
    name = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li/div/a/div/div/h2')
    for i in range(len(name)):
        print(lei[i].text+'--'+title[i].text+'--'+name[i].text+'--'+redu[i].text)
    driver.close()




if __name__ == '__main__':
    url = "https://www.douyu.com/directory/all"
    dou(url)
