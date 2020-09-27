# -*- coding:utf-8 -*-
import cv2

face_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'.\cascades\haarcascade_eye.xml')
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
while True:
    ret, frame = camera.read()
    if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
        break
    camera.release()