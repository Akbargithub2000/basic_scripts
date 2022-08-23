import socket
import os

buffer = 1024
client_host = "Ip Address"
port = 9001
filename = 'image.jpg'
size = os.path.getsize(filename)
sock = socket.socket()

print(f'Connecting with {client_host} : {port}')
sock.connect((client_host, port))
sock.send(f'{filename} with size: {size}'.encode())

with open(filename, 'rb') as f:
  while True:
    reading_byte = f.read(buffer)
    if not reading_byte:
       break
    sock.sendall(reading_byte)
sock.close()

server_host = 'Ip Address'
port = 5001
buffer = 1024

sock = socket.socket()
sock.bind((server_host, port))
sock.listen(10)
print(f'Waiting for Connection {server_host} : {port}')
client,addr = sock.accept()
print(f'{addr} is connected.')

recieved = client.recv(buffer).decode()
name, size = recieved.split("-")
name = os.path.basename(name)

with open(name, 'wb') as f:
  while True:
    reading_true = client.recv(buffer)
    if not reading_byte:
       break
    f.write(reading_true)

client.close()
sock.close()
