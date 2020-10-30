import socket
import Tool

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Tool.fence()
print("s=", s)
Tool.fence()
# s.connect(('https://www.baidu.com/', 80))
s.connect(('www.lzu.edu.cn', 80))
s.settimeout(5.2)
timeout = s.gettimeout()
print("timeout =", timeout)

Tool.fence()
print("s=", s)
Tool.fence()
s.send(b"GET / HTTP/1.1\r\nHost:www.lzu.edu.cn\r\nConnection: close\r\n\r\n")
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()
data = b"".join(buffer)
header, html = data.split(b"\r\n\r\n", 1)
Tool.fence()
print(header.decode("utf-8"))
Tool.fence()
with open("lzu.html","wb") as f:
    f.write(html)
f.close()