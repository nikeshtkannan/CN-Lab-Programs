
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5000))

while True:
    msg, addr = s.recvfrom(1024)
    t = time.ctime()
    s.sendto(t.encode(), addr)
