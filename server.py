#-*-coding:utf-8-*-


from socket import *
from time import ctime

BUFSIZE = 1024              #缓冲区大小1K
ADDR = ('',15116) #地址和端口号
tcpSerSock = socket(AF_INET, SOCK_STREAM)   #建立一个地址家族为Internet面向连接的套接字
tcpSerSock.bind(ADDR)       #绑定地址到套接字
tcpSerSock.listen(3)        #监听 最多同时3个连接进来
while True:                 #无限循环等待连接到来
    print ('Waiting for connection ....')
    tcpCliSock, addr = tcpSerSock.accept()  #被动接受客户端连接
    print ('Connected client from : ', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()     #接受客户端数据
        if not data:
            break
        else:
            print ('Client: ',data)
        tcpCliSock.send(('[%s] %s' %(ctime(),data)).encode()) #发送时间戳到客户端
tcpSerSock.close()          #关闭服务器
