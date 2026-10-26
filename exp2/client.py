
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter a sentence: ")

s.sendto(msg.encode(), ("127.0.0.1", 8080))

result, server = s.recvfrom(2048)

print("Translated sentence:", result.decode())

s.close()
