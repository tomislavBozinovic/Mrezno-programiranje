from socket import *

s = socket(type=SOCK_DGRAM)
s.sendto(b'Hello World! TB',('localhost',5000))
data,addr = s.recvfrom(1024)
print(data,addr)