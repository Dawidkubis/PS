import socket

with socket.socket() as s:

    PORT = 65432
    s.bind(('127.0.0.1', PORT))
    s.listen()

    client, addr = s.accept()
    info = ''
    while info != 'quit'.encode():

        info = client.recv(1024)
        print(f'recieved : {info}')

        if not info:
            break
