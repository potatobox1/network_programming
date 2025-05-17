# This a port scanner used to identify open ports for a particular service
# Usefull for identifying security vulnerabilities or hacking

import socket
import os
from dotenv import load_dotenv
import threading
from queue import Queue

load_dotenv()

# IP of the service we want to scan, localhost server from server.py in this case
SERVICE_IP = "127.0.0.1"
NUM_THREADS = 500

# Or domain url
url = os.getenv("URL")
SERVICE_IP = socket.gethostbyname(url)

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((SERVICE_IP, port)) 
        sock.close()
        return True
    except:
        return False

queue = Queue()
# Scanning Reserved HTTP, FTP, SSH ports etc
for port_num in range(1, 10240):
    queue.put(port_num)

open_ports = []
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("port {} is open".format(port))
            open_ports.append(port)

threads = []
for t in range(NUM_THREADS):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Open Ports:", open_ports)