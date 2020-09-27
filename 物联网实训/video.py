# -*- coding:utf-8 -*-
import socket
import time
import cv2
import numpy as np
#
# filename = r'.\img\timg.jpg'
# def detect(filename):
#     face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
#     img = cv2.imread(filename)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
#         cv2.namedWindow('人脸检测')
#         cv2.imshow('人脸检测', img)
#         cv2.waitKey(0)
# detect(filename)

#视频中人脸检测
def detect():
    face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            # roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(gray, 1.2, 5, 0, (5, 5))
            # eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40,40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
            cv2.imshow("Camera", frame)
            #裁剪图像中人脸部分
            img2 = img[y:y+h, x:x+w]
            # 获取到人脸之后进行图片保存
            cv2.imwrite(r'./img/01.jpg', img2, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

        if cv2.waitKey(1000 // 12) & 0xff==ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    detect()