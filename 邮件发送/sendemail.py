# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
def sendmail():
    msg = MIMEText("Hello", 'plain', 'utf-8')
    #编写头
    header_from = Header("从Anonymous的邮箱发出去的<Anonymous@qq.com>", 'utf-8')
    msg['From'] = header_from
    #编写接收者信息
    header_to = Header("去Dos的地方<Dos@qq.com>", 'utf-8')
    msg['To'] = header_to

    header_sub = Header('这是Anonymous', 'utf-8')
    msg['Subject'] = header_sub

    #构建发送者地址和登录信息
    from_addr = '1395900558@qq.com'
    from_pwd = 'xbtwxnpunjieihig'
    #构建接收者信息
    to_addr = '418033532@qq.com'

    smtp_srv = 'smtp.qq.com'

    try:
        srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
        #使用账号跟SMTP协议码进行登录
        srv.login(from_addr, from_pwd)
        #发送
        srv.sendmail(from_addr, [to_addr], msg.as_string())
        #关闭
        srv.quit()
    except Exception as e:
        print(e)

if __name__ =='__main__':
    i = 1
    while 1:
        sendmail()
        print(i)
        i += 1
        time.sleep(20)
