# coding: utf-8
import socket
import os


def sendfile(conn):
    str1 = conn.recv(1024)
    filename = str1.decode('utf-8')
    print("the client requests my file:", filename)
    if os.path.exists(filename):
        print("i have %s, begin to download!" % filename)
        conn.send(b'yes')
        conn.recv(1024)
        size = 1024
        with open(filename, 'rb') as f:
            while True:
                data = f.read(size)
                conn.send(data)
                if len(data) < size:
                    break
        print('%s is downloaded successfully!' % filename)
    else:
        print('sorry, i have no %s' % filename)
        conn.send(b"no")
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('19.244.41.103', 8098))
s.listen(1)
print("wait for connecting ...")
while True:
    (conn, addr) = s.accept()
    sendfile(conn)
