# -*- coding:utf-8 -*-
import cv2
import os
import pandas as pd
def generate(name):
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
        if a==30:
            break
        cv2.imshow("Camera", frame)
      #q退出
        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
#将数据写入csv
def init_th():
    data = []
    data1 = []
    list1 = os.listdir(r'.\img')
    con = 0
    for i in list1:
        list2 = os.listdir(r'.\img\%s' % i)
        for j in list2:
            data1.append(".\img\{0}\{1}".format(i, j))
            data1.append(str(con))
            # print(data1)
            data.append(data1)
            data1 = []
        con += 1

    print(data)
    data = pd.DataFrame(data, index=None, columns=None)
    data.to_csv(r".\face_data.csv", header=False, index=False)
if __name__ == '__main__':
    name = input("请输入录入者姓名:")
    #创建录入者dir
    os.mkdir(r'.\img\%s' %str(name))
    generate(name)
    init_th()