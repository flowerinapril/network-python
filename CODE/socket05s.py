# coding: utf-8

import socket
import psutil


def do_cpu():
    data = str(psutil.cpu_percent(0)) + '%\n'
    count = 0
    for process in psutil.process_iter():
        data = data + process.name()
        data = data + ',' + str(process.pid)
        cpu_usage_rate_process = str(process.cpu_percent(0)) + "%"
        data = data + ',' + cpu_usage_rate_process + '\n'
        count += 1
        if count == 10:
            break
    return data


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('19.244.46.22', 8080))
print('bind udp on 8080')
while True:
    (info, addr) = s.recvfrom(1024)
    print(info)
    data = do_cpu()
    s.sendto(data.encode('utf-8'), addr)
    print('the client is ', addr)
    print('sended cpu data is :', data)
