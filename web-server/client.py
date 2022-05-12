import socket

HOST = "127.0.0.1" # server's hostname / IP
PORT = 65432 # port used by server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)
    print("Received {data}!")