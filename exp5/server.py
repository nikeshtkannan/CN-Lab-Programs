
import socket
import threading
import os

def handle_client(client):
    filename = client.recv(1024).decode().strip()

    pid = os.getpid()

    try:
        with open(filename, "r") as f:
            data = f.read()
        msg = f"PID: {pid}\nFile contents:\n{data}"
    except FileNotFoundError:
        msg = f"PID: {pid}\nFile not found"

    client.sendall(msg.encode())
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

print("Server is running. PID:", os.getpid())

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()
