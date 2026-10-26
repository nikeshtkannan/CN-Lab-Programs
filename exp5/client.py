
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5000))

filename = input("Enter filename: ")
s.sendall(filename.encode())

while True:
    data = s.recv(1024)
    if not data:
        break
    print(data.decode(), end="")

s.close()
