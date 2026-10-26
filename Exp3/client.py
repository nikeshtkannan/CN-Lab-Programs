
import socket
import threading

def receive():
    while True:
        try:
            msg = s.recv(1024)
            if not msg:
                break
            print("\nReceived:", msg.decode())
        except:
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

print("Connected to chat server")

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input("Enter message: ")
    s.send(msg.encode())
