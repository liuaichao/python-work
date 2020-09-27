# -*- coding:utf-8 -*
import cv2
import numpy as np
import pandas as pd
import time
import os
import sys
def read_image(path, sz=None):
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
def face_rec():
    name = ["liuaichao", "yangmi"]
    [X, y] = read_image(r".\face_data.csv")
    y = np.asarray(y, dtype=np.int32)
    model = cv2.face.EigenFaceRecognizer_create()
    model.train(np.asarray(X), np.asarray(y))
    camera = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
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
                cv2.putText(img, name[0], (x, y-20), cv2.FONT_HERSHEY_SIMPLEX,
                            1, 255, 2)


            except:
                continue
            # if params:
            #     #将打卡记录插入数据库
            #     sql = 'INSERT INTO card(name, time) values ("{0}", "{1}");'.format(name[params[0]], time.ctime())
            #     print(sql)
            #     exit()

        cv2.imshow("camera", img)

        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()
#服务器传数据

if __name__ == '__main__':

    face_rec()