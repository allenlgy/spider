# 导入 socket 这个库
import socket

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 开始建立TCP链接
s.connect(("www.mzitu.com",80))

# 链接后发送请求
s.send(b"GET/HTTP/1.1\r\nHost : www.mzitu.com\r\nConnection: close\r\n\r\n")

# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# 吧字节链接起来
data = b''.join(buffer)

# 关闭链接
s.close()

# 把数据读出来
with open("mzitu.html","wb")as f:
    f.write(data)

