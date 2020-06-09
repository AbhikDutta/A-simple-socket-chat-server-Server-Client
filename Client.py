while True:

    import socket

    c = socket.socket()

    c.connect(('192.168.15.94', 9999))

    print(c.recv(1024).decode())

    name = input("Write Something :       ")

    c.send(bytes(name, 'utf-8'))
