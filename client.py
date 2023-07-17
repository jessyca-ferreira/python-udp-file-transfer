import socket
import select
from pathlib import Path

BUFFER_SIZE = 1024
HOST = 'localhost'
PORT = 5000
FOLDER_PATH = Path('client-files/')
TIMEOUT = 3

dest = (HOST, PORT)     # endereco de destino (servidor)
origin = ('localhost', 3000)    # endereco do cliente

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(origin)     # associa o cliente a um endereco

def send_file(file_name):
    file_path = str(FOLDER_PATH / file_name)
    client.sendto(file_name.encode(), dest)
    
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            if client.sendto(data, dest):
                data = file.read(BUFFER_SIZE)
        try:
            received_data, server_adress = client.recvfrom(BUFFER_SIZE)
            print(received_data.decode())
            receive_file(received_data.decode())
        except:
            pass
        
        
def receive_file(file_name):
    with open(str(FOLDER_PATH / file_name), 'ab') as file:
        while True:
            selection = select.select([client], [], [], TIMEOUT)
            if selection[0]:
                data, client_address = client.recvfrom(BUFFER_SIZE)
                file.write(data)
            else:
                break

print('Para sair, user CTRL+X\n')

sending = True
while sending:
    data = input()
    if data == '\x18':
        client.sendto(data.encode(), dest)
        sending = False
    else:
        send_file(data)
        



 

client.close()

