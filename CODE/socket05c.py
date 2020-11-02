# coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr = ('19.244.46.22', 8080)
s.sendto(b'cup_info', s_addr)
(data_b, addr) = s.recvfrom(1024)

if addr == s_addr:
    data_s = data_b.decode('utf-8')
    data_list = data_s.split('\n')
    print('cpu usage rate is ', data_list[0])
    print('Top 10 process are flowing...')
    print('%-20s%-5s%-10s'% ('name', 'PID', 'cpu usage'))
    data_list = data_list[1:-1]
    for x in data_list:
        y = x.split(',')
        print('%-20s%-5s%-10s'% (y[0], y[1], y[2]))
s.close()


