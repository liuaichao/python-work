# -*- coding:utf-8 -*-
#小程序控制树莓派 ****
import socket
import cv2
import os
class WebServer():
    def __init__(self):

        self.ip = '0.0.0.0'
        self.ip2 = '0.0.0.0'
        self.port = int(9999)
        self.port2 = int(9998)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, int(self.port)))
        self.sock2.bind((self.ip2, self.port2))
        self.sock.listen(2)
        self.sock2.listen(2)
        print("webserver1 正在运行")
        print("webserver2 正在运行")
    def start(self):
        while True:
            #先于树莓派建立连接
            skt, addr = self.sock.accept()
            if skt:
                print("树莓派已连接")
            #接收小程序来的数据
            skt2, addr2 = self.sock2.accept()
            print(self.get_data(skt2))

            # print("show data")
            #
            # if int(skt2[0]) == 1:
            #     #录入操作
            #     send_data = '1'+ skt2[1:len(skt2)-1]
            #     skt.send(send_data.encode())
            # if int(skt2) == 2:
            #     #识别状态
            #     send_data = '2'
            #     skt.send(send_data.encode())



    #得到数据
    def get_data(self, skt):
        msg = skt.recv(50)
        msg = msg.decode()
        return msg
    #返回数据
    def sendRsp(self, skt, content):
        # 构建返回头
        rsp1 = "HTTP/1.1 200 OK \r\n"
        rsp2 = "Date: 20191223\r\n"
        len_value = len(content)
        rsp3 = "Content-Length:{0}\r\n".format(len_value)
        rsp4 = "\r\n"
        rep_content = content
        # 合起来
        rsp = rsp1 + rsp2 + rsp3 + rsp4 + rep_content
        skt.send(rsp.encode())
if __name__ == "__main__":
    ws = WebServer()
    ws.start()


