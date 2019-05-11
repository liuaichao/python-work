# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import random
list_zi = ['666','这一波可以','牛逼','可以带粉吗','可以可以','别怂']
def start():
    url = 'https://www.douyu.com/435504'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_xpath('//div[@class="MuteStatus is-noLogin"]/span').click()
    #获取弹幕
    time.sleep(30)
    try:
        danmu = driver.find_elements_by_class_name('Barrage-content')
        danmu = danmu[-2].text
    except:
        danmu = random.choice(list_zi)
    if danmu=='':
        danmu = random.choice(list_zi)
    driver.find_element_by_class_name('ChatSend-txt ').send_keys(danmu)
    time.sleep(2)
    driver.find_element_by_class_name('ChatSend-button ').click()

    time.sleep(2)
    return driver
def co(driver):
    for i in range(10):
        time.sleep(60)
        try:
            danmu = driver.find_elements_by_class_name('Barrage-content')
            danmu = danmu[-2].text
        except:
            danmu = random.choice(list_zi)
        if danmu=='':
            danmu = random.choice(list_zi)
        driver.find_element_by_class_name('ChatSend-txt ').send_keys(danmu)
        time.sleep(2)
        driver.find_element_by_class_name('ChatSend-button ').click()
    return driver
def tuichu(driver):
    driver.quit()

if __name__=='__main__':
    a = start()
    b = co(a)
    tuichu(b)


