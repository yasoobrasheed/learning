import socket

HOST = '127.0.0.1'
PORT = '65432' # non priveleged ports are >1023

# IPv4 && TCP socket type passed to socket()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # hook up socket to HOST and PORT, IPv4 expects tuple
    s.listen()
    conn, addr = s.accept() # provides the client socket obj: conn
    with conn:
        print("Connected by {addr}")
        while True:
            data = conn.recv(1024) # reads data client sends
            if not data:
                break
            conn.sendall(data) # echoes back client data to client