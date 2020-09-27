# -*- coding:utf-8 -*-
import socket
HOST = '0.0.0.0'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定socket
s.bind((HOST, PORT))
#开始监听
s.listen(1)
print('Listening at port:',PORT)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('Received message:', data)
conn.close()
s.close()
