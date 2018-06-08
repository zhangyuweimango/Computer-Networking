# -*- coding: utf-8 -*-


from socket import *

HOST = '192.168.40.138'          #访问的主机IP
PORT =  15116               #端口号 与服务器一致
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)   #建立一个地址家族为Internet面向连接的套接字
tcpCliSock.connect(ADDR)    #连接服务器
while True:                 #无限循环等待连接到来
    data = input('Input >')
    if not data:
        break
    tcpCliSock.send(data.encode())           #发送数据
    data = tcpCliSock.recv(BUFSIZE).decode()  #接受服务器端时间戳数据
    if not data:
        break
    print ('Server: ', data)
tcpCliSock.close()          #关闭客户端
