
import socket
import threading

clients = []

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break

            for c in clients:
                if c != client:
                    c.send(msg)

        except:
            break

    clients.remove(client)
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(10)

print("Chat server started")

while True:
    client, addr = server.accept()
    clients.append(client)

    threading.Thread(target=handle, args=(client,), daemon=True).start()
