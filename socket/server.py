#!python3

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("localhost", 9473))
socket.listen()

conn, addr = socket.accept()

print("Aguardando mensagem do Client..")

while True:
    data = conn.recv(1024)
    if not data:
         break
    print("Nova mensagem do Host %s: %s" % (addr, data.decode()))

conn.close()