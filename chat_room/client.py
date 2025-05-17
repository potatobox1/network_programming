# TCP Chatroom Client side code
# Only simple functionality, send another user message
# Message format: name <name of reciever> <msg>
# e.g name john Hello John, whats up bro
# Reciever side message e.g Potatobox: Hello John, whats up bro

import sys
import socket
import threading

def listener():
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            message_split = message.split(" ")
            if not message:
                break
            if message == "name":
                sock.send(name.encode("utf-8"))
            elif message_split[0] == "server":
                print("Server:", message)
            else:
                print(f"\r{message}\nEnter Message: ", end="", flush=True)
        except:
            print("Disconnected from server.")
            break

def sender():
    while True:
        try:
            message = input("Enter Message: ")
            sock.send(message.encode("utf-8"))
        except:
            print("Cannot send message. Disconnected?")
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Usage python client.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    address = "127.0.0.1"
    port = 47878

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))
        print(f"Connected to {address}:{port} as {name}")

        # Start listener and sender threads
        threading.Thread(target=listener, daemon=True).start()
        sender()

    except Exception as e:
        print("Connection Failed:", e)
    finally:
        sock.close()
