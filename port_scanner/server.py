# Local Host Server to test the DoS script

import socket

HOST = '127.0.0.1'  # Localhost only
PORT = 8080         # You can pick any free port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    client, addr = server.accept()
    print(f"[CONNECTION] From {addr}")
    client.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!\n")
    client.close()
