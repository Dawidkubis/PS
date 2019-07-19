from socket import socket

with socket() as s:

    PORT = 65432
    s.connect(('127.0.0.1', PORT))

    info = ''
    while info != 'exit':
        info = input('info : ')
        s.sendall(info.encode())
