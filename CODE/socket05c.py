# coding: utf-8
import socket
s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr = ('192.168.1.2',8080)
s.sendto(b'cup_info', s_addr)
(data_b, addr) = s.recvfrom(1024)
if addr == s_addr:
    data_s = data_b.decode('utf-8')
    data_list = data_s.split('\n')
    print('cpu usage rate is ', data_list[0])
    