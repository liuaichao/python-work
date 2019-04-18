# -*- coding:utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("192.168.43.242", 7852))

sock.listen()
skt, addr = sock.accept()
msg = skt.recv(100)
print(type(msg))
print(msg.decode())
msg = "i love yanglinlin"
skt.send(msg.encode())

skt.close()
sock.close()
