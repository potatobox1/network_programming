# TCP Chat Room Server

import socket
import threading

address = "127.0.0.1"
port = 47878

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen()

clients_names = {}

def handle_connection(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise ConnectionResetError  # treat empty recv as disconnect

            message_split = message.decode("utf-8").split(" ")

            if message_split[0] == "exit":
                if client in clients_names:
                    clients_names.pop(client)
                client.close()
                break

            elif message_split[0] == "name":
                receiver_sock = None
                for key in clients_names:
                    if clients_names[key] == message_split[1]:
                        receiver_sock = key
                        break

                if receiver_sock is None:
                    client.send("No such user is connected to the server".encode("utf-8"))
                else:
                    message_joined = " ".join(message_split[2:])
                    message_joined = clients_names[client] + ": " + message_joined
                    receiver_sock.send(message_joined.encode("utf-8"))

        except Exception as e:
            if client in clients_names:
                clients_names.pop(client)
            try:
                client.close()
            except:
                pass
            break

def accept_conns():
    while True:
        client, addr = server.accept()
        client.send("name".encode("utf-8"))
        name = client.recv(1024).decode("utf-8")
        clients_names[client] = name
        print(f"Connected with {addr}, Name: {name}")

        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()

accept_conns()
