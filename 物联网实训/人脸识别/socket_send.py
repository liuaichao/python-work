# -*- coding:utf-8 -*-
import socket
import cv2
import os
import pandas as pd
import numpy as np
import time
from mysql_demo import Mysql_demo
class Nb():
    def start(self):
        HOST = '47.105.142.252'
        PORT = 10000
        BUFSIZ =1024
        ADDR = (HOST,PORT)

        tcpCliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        print("成功连接服务器")
        while True:

             data1 = tcpCliSock.recv(BUFSIZ)
             data1 = data1.decode()
             print(data1)
             if int(data1[0]) == 1:
                 print("开始录入面部")
                 name = data1[1:len(data1)]
                 # name = "liuaichao"
                 # 创建录入者dir
                 try:
                    os.mkdir(r'.\img\%s' % str(name))
                 except Exception as a:
                     print(a)
                 self.generate(name)
                 self.init_th(name)
             if int(data1[0]) == 2:
                 print("监控")
                 self.face_rec()

        tcpCliSock.close()
    def generate(self, name):
        face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
        camera = cv2.VideoCapture(0)
        count = 0
        a = 0
        while True:
            ret, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                img = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                #裁剪图像，并把图像大小设置为200x200
                f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
                cv2.imwrite(r'.\img\{0}\{1}.png'.format(str(name), str(count)), f)
                count += 1
            a += 1
            if a == 40:
                break

            cv2.imshow("Camera", frame)
          #q退出
            if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()
    #将数据写入csv
    def init_th(self, name):
        data = []
        data1 = []
        list1 = os.listdir(r'.\img')
        #查重操作
        print("进行查重操作")
        sql = 'select * from zhu where name="{0}";'.format(name)
        n = Mysql_demo()
        x = n.search(sql)
        if x:
            print("你之前已经注册")
            return
        #查询剩余编号
        print("查询编号")
        sql = 'select * from zhu order by ids DESC limit 1;'
        n = Mysql_demo()
        data_con = n.search(sql)
        con = int(data_con[0][1]) +1
        for i in list1:
            list2 = os.listdir(r'.\img\%s' % i)
            for j in list2:
                data1.append(".\img\{0}\{1}".format(i, j))
                data1.append(str(con))
                # print(data1)
                data.append(data1)
                data1 = []

        # print(data)
        data = pd.DataFrame(data, index=None, columns=None)
        data.to_csv(r".\face_data.csv", header=False, index=False)
        sql = 'INSERT INTO zhu(idd, name) values ({0}, "{1}");'.format(con, name)
        n = Mysql_demo()
        n.insert(sql)
        print("恭喜{0}注册成功!!".format(name))
    def read_image(self, path, sz=None):
        c = 0
        X,y = [], []

        data = pd.read_csv(path)
        data = data.values
        print(data)
        for i,j in data:
            im = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
            if sz is not None:
                im = cv2.resize(im, (200, 200))
            X.append(np.asarray(im, dtype=np.uint8))
            y.append(j)
        return [X, y]
    #识别
    def face_rec(self):
        #查询姓名id对照表
        print("姓名id对照表")
        xx = Mysql_demo()
        sql = 'select name from zhu;'
        data_name = xx.search(sql)
        name = []
        for i in data_name:
            name.append(i[0])
        [X, y] = self.read_image(r".\face_data.csv")
        y = np.asarray(y, dtype=np.int32)
        model = cv2.face.EigenFaceRecognizer_create()
        model.train(np.asarray(X), np.asarray(y))
        camera = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
        n = []
        while True:
            read, img = camera.read()
            faces = face_cascade.detectMultiScale(img, 1.3, 5)
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img, (x,y), (w+w, y+h), (255,0,0),2)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                roi = gray[x:x+w, y:y+h]
                try:
                    roi = cv2.resize(roi, (200,200), interpolation=cv2.INTER_LINEAR)
                    params = model.predict(roi)
                    print(params)
                    cv2.putText(img, name[params[0]], (x, y-20), cv2.FONT_HERSHEY_SIMPLEX,
                                1, 255, 2)
                except:
                    continue

                if params[0] == n:
                    pass
                else:
                    n = params[0]
                    #将打卡记录插入数据库
                    sql = 'INSERT INTO card(name, time) values ("{0}", "{1}");'.format(name[params[0]], time.ctime())
                    my = Mysql_demo()
                    my.insert(sql)
                    print("打卡成功！！欢迎{0}".format(name[params[0]]))

                cv2.imshow("camera", img)

            if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
                break
        cv2.destroyAllWindows()
if __name__ == '__main__':
    m = Nb()
    m.start()