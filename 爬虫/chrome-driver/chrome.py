from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
text = driver.find_element_by_id('wrapper').text
print(text)
driver.save_screenshot('index.png')
driver.find_element_by_id('kw').send_keys(u"大熊猫")
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('大熊猫.png')
print(driver.get_cookies())
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.find_element_by_id('kw').send_keys(u"航空母舰")
time.sleep(5)
driver.save_screenshot('航空母舰.png')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(5)
driver.save_screenshot('航空母舰2.png')
driver.find_element_by_id('kw').clear()
driver.quit()