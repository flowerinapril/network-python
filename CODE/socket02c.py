# coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('19.244.41.103', 8098))
print("i have connecting the server")
for x in ['aBch','f服务d','h7Tp','.']:
    s.send(x.encode('utf-8'))
    str1 = s.recv(1024)
    str2 = str(str1, encoding='utf-8')
    print("the original string is : ", x, '\t the processed string is: ', str2)
s.close()



