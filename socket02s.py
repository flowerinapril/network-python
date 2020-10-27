# coding:utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.3.13", 8088))
s.listen(1)
print("wait for connecting ...")
(conn, addr) = s.accept()
print('conn=', conn)
print("addr=", addr)
while True:
    str1 = conn.recv(1024)
    str2 = str(str1, encoding="utf-8")
    print("i received a string is: ", str2)
    str3 = str2.upper()
    conn.send(str3.encode('utf-8'))
    if str2 == '.':
        break
conn.close()
s.close()

