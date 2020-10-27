# coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('19.244.41.103', 8098))
filename = "autumn.jpg"
print('i want to get the file %s' % filename)
s.send(filename.encode('utf-8'))
str1 = s.recv(1024)
str2 = str1.decode('utf-8')
if str2 == 'no':
    print("fail to get the file")
else:
    s.send(b'i am ready')
    temp = filename.split('/')
    myname = 'my_'+temp[len(temp)-1]
    size = 1024
    with open(myname, 'wb') as f:
        while True:
            data = s.recv(1024)
            f.write(data)
            if len(data)<size:
                break
    print('the download file is %s' % myname)
s.close()


