from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def xiaomi(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id('username').send_keys('17861404961')
    driver.find_element_by_id('pwd').send_keys('lac981215lac')
    driver.find_element_by_id('login-button').click()
    time.sleep(5)
    driver.save_screenshot('xiaomi.jpg')
    driver.close()


if __name__ == '__main__':
    url = "https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"
    xiaomi(url)