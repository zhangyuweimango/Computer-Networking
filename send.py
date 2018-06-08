# -*- coding=utf-8 -*-


import socket
import os
import sys
import struct

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建一个socket
        s.connect(('192.168.40.138', 6666))#连接服务器
    except socket.error as msg:
        print (msg)
        sys.exit(1)

    print (s.recv(1024))

    while 1:
        filepath = raw_input('please input file path: ')
        if os.path.isfile(filepath):      
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fhead = struct.pack('128sl', os.path.basename(filepath),os.stat(filepath).st_size)
            #将字符串的长度打包
            s.send(fhead)
            #发送数据
            print ('client filepath: {0}'.format(filepath))

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(filepath))
                    break
                s.send(data)
        s.close()#关闭客户端
        break


if __name__ == '__main__':
    socket_client()
