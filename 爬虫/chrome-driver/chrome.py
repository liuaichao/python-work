from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys



#概率分布函数
def random_index(rate):
    # """随机变量的概率函数"""
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index
for i in range(20):

        #打开网页
        driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        url = "https://www.wjx.cn/m/59810893.aspx"
        driver.get(url)
        print(driver.title)


        #第一题
        tem = random_index([25, 38.46, 26.92, 9.62])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div1"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
            time.sleep(10)
            driver.find_element_by_id("ctlNext").click()
            driver.quit()
            continue
        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div1"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div1"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()

        elif tem == 3:
            driver.find_element_by_xpath('//div[@id="div1"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()
            time.sleep(10)
            driver.find_element_by_id("ctlNext").click()
            driver.quit()
            continue
        #第二题
        tem = random_index([52, 48])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div2"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div2"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
        #第三题
        tem = random_index([29, 50])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div3"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div3"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        #第四题
        tem = random_index([26, 21, 35, 18])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div4"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div4"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div4"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()

        elif tem == 3:
            driver.find_element_by_xpath('//div[@id="div4"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()
        #第五题
        driver.find_element_by_id("q5").send_keys(u"无")
        #第六题
        tem = random_index([26, 15, 41, 18])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div6"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div6"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div6"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()

        elif tem == 3:
            driver.find_element_by_xpath('//div[@id="div6"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()

        #第七题
        tem = random_index([47, 18, 9, 26])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div7"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div7"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div7"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()

        elif tem == 3:
            driver.find_element_by_xpath('//div[@id="div7"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()
        #第八题
        tem = random_index([21, 41, 38])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div8"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div8"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div8"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()
            #跳转到12题
            tem = random_index([59, 3, 38])
            if tem == 0:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 15
                driver.find_element_by_id("q15").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 1:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
                # 13
                driver.find_element_by_id("q13").send_keys(u"无")
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 2:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 15
                driver.find_element_by_id("q15").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            #14题
            driver.find_element_by_id("q14").send_keys(u"无")
            #16题
            driver.find_element_by_id("q16").send_keys(u"无")
            #提交
            time.sleep(10)
            driver.find_element_by_id("ctlNext").click()
            driver.quit()
            continue
        #第九题
        tem = random_index([81, 19, 33, 52])
        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div9"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()

        elif tem == 1:
            driver.find_element_by_xpath('//div[@id="div9"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()

        elif tem == 2:
            driver.find_element_by_xpath('//div[@id="div9"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()

        elif tem == 3:
            driver.find_element_by_xpath('//div[@id="div9"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()

        #第十题
        tem = random_index([24, 76])

        if tem == 0:
            driver.find_element_by_xpath('//div[@id="div10"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
            # 第十一题,全选

            driver.find_element_by_xpath('//div[@id="div11"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
            driver.find_element_by_xpath('//div[@id="div11"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
            driver.find_element_by_xpath('//div[@id="div11"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()
            driver.find_element_by_xpath('//div[@id="div11"]/div[@class="ui-controlgroup"]/div[4]/span/a').click()

            # 跳转到12题
            tem = random_index([59, 3, 38])
            print(tem)
            if tem == 0:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
                #跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                #15
                driver.find_element_by_id("q15").send_keys(u"无")
                #16
                driver.find_element_by_id("q16").send_keys(u"无")
                #提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 1:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
                #13
                driver.find_element_by_id("q13").send_keys(u"无")
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 2:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 15
                driver.find_element_by_id("q15").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
        elif tem == 1:

            driver.find_element_by_xpath('//div[@id="div10"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
            # 跳转到12题
            tem = random_index([59, 3, 38])
            if tem == 0:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[1]/span/a').click()
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 15
                driver.find_element_by_id("q15").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 1:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[2]/span/a').click()
                # 13
                driver.find_element_by_id("q13").send_keys(u"无")
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue
            elif tem == 2:
                driver.find_element_by_xpath('//div[@id="div12"]/div[@class="ui-controlgroup"]/div[3]/span/a').click()
                # 跳转14
                driver.find_element_by_id("q14").send_keys(u"无")
                # 15
                driver.find_element_by_id("q15").send_keys(u"无")
                # 16
                driver.find_element_by_id("q16").send_keys(u"无")
                # 提交
                time.sleep(10)
                driver.find_element_by_id("ctlNext").click()
                driver.quit()
                continue

            # 14题
            driver.find_element_by_id("q14").send_keys(u"无")
            #15
            driver.find_element_by_id("q15").send_keys(u"无")
            # 16题
            driver.find_element_by_id("q16").send_keys(u"无")
            # 提交
            time.sleep(10)
            driver.find_element_by_id("ctlNext").click()
            driver.quit()
            continue






        time.sleep(5)
        driver.quit()




