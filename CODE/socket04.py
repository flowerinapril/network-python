# coding: utf-8
'''
用于扫描主机端口
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
ip = "19.244.46.22"
for port in range(5000,9000):
    result = s.connect_ex((ip, port))
    if result == 0:
        print('port %d is opened' % port)
s.close()
