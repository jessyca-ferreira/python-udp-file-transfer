import socket
import select
from pathlib import Path

BUFFER_SIZE = 1024
HOST = 'localhost'
PORT = 5000
FOLDER_PATH = Path('client-files/')
TIMEOUT = 10

dest = (HOST, PORT)     # endereco de destino (servidor)
origin = ('localhost', 3000)    # endereco do cliente

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_file(file_name):
    file_path = str(FOLDER_PATH / file_name)
    
    client.sendto(file_name.encode(), dest)
    
    with open(file_path, 'rb') as file:
        data = file.read(BUFFER_SIZE)
        while data:
            if client.sendto(data, dest):
                data = file.read(BUFFER_SIZE)
        try:
            received_data, server_address = client.recvfrom(BUFFER_SIZE)
            print(received_data.decode())
            receive_file(received_data.decode())
        except:
            pass
        
        
def receive_file(file_name):
    with open(str(FOLDER_PATH / file_name), 'wb') as file:
        while True:
            selection = select.select([client], [], [], TIMEOUT)
            if selection[0]:
                data, server_address = client.recvfrom(BUFFER_SIZE)
                file.write(data)
            else:
                break

print('Para sair, user CTRL+X\n')

sending = True
while sending:
    file_name = input()
    if file_name == '\x18':
        client.sendto(file_name.encode(), dest)
        sending = False
    else:
        send_file(file_name)
        
client.close()

