# coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr = ('19.244.46.22', 8080)
s.bind(('19.244.46.22', 8888))
s.sendto(b'memory info', s_addr)
(data_b, addr) = s.recvfrom(1024)
if addr == s_addr:
    data_s = data_b.decode('utf-8')
    print('memory status is flowing...')
    data_list = data_s.split(',')
    for x in data_list:
        print(x)

s.close()



