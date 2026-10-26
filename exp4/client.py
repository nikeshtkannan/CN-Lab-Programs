
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("127.0.0.1", 5000)

s.sendto(b"time", server)
msg, addr = s.recvfrom(1024)

print("Server Time:", msg.decode())

s.close()
