# -*- coding: utf-8 -*-
"""client.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/198M9BgtZBrSEzOYwc0hBQHHuyGTOb7sy
"""

import socket

SERVER_ADDRESS = ('', 9090)

sock = socket.socket()
sock.connect(SERVER_ADDRESS)

while True:
    msg = input()
    if msg == 'exit':
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    data_decode = data.decode()
    print(data_decode)

sock.close()