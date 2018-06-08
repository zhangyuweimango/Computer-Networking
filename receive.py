# -*- coding=utf-8 -*-


import socket
import threading
import time
import sys
import os
import struct


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建一个socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 6666))#监听的端口地址
        s.listen(10)#每次允许接入的客户端数量为10
    except socket.error as msg:
        print (msg)
        sys.exit(1)
    print ('Waiting connection...')

    while 1:
        conn, addr = s.accept()#接收客户端连接
        t = threading.Thread(target=deal_data, args=(conn, addr))
        # 建立一个线程用来监听收到的数据
        t.start()#线程运行
        
def deal_data(conn, addr):
    print ('Accept new connection from {0}'.format(addr))
    conn.send('Hi, Welcome to the server!')

    while 1:
        fileinfo_size = struct.calcsize('128sl')
        buf = conn.recv(fileinfo_size)#接收报头的长度
        if buf:
            filename, filesize = struct.unpack('128sl', buf)#解析出报头的字符串大小
            fn = filename.strip('\00')
            new_filename = os.path.join('./', 'new_' + fn)
            print ('file new name is {0}, filesize if {1}'.format(new_filename,filesize))

            recvd_size = 0  # 定义已接收文件的大小
            fp = open(new_filename, 'wb')
            print ('start receiving...')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print ('end receive...')
        conn.close()#关闭客户端
        break


if __name__ == '__main__':
    socket_service()
