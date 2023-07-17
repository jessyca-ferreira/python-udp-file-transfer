import socket
import select
from pathlib import Path

BUFFER_SIZE = 1024
HOST = 'localhost'          # endereço ip do servidor
PORT = 3000                 # porta do servidor
FOLDER_PATH = Path('server-files/')

dest = (HOST, PORT)
origin = ('localhost', 5000)     # endereco de origem do servidor

TIMEOUT = 3

def receive_file(file_name):
    with open(str(FOLDER_PATH / file_name), 'ab') as file:
        while True:
            selection = select.select([server], [], [], TIMEOUT)
            if selection[0]:
                data, client_address = server.recvfrom(BUFFER_SIZE)
                file.write(data)
            else:
                server.sendto(('received' + file_name).encode(), client_address)
                send_file(file_name)
                break
            
def send_file(file_name):
    file_path = str(FOLDER_PATH / file_name)
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            if server.sendto(data, dest):
                data = file.read(BUFFER_SIZE)
            

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(origin)

finished = False

while not finished:
    data, client_address = server.recvfrom(BUFFER_SIZE)
    if (data.decode() == '\x18'):
        finished = True
    else:
        file_name = data.decode()
        receive_file(file_name)
    
server.close()
        

