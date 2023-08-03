import socket
from pathlib import Path

BUFFER_SIZE = 1024
HOST = 'localhost'          # endereço ip do servidor
PORT = 3000                 # porta do servidor
FOLDER_PATH = Path('server-files/')
TIMEOUT = 3

dest = (HOST, PORT)
origin = ('localhost', 5000)     # endereco de origem do servidor


def receive_file(file_name):
    file_path = str(FOLDER_PATH / file_name)
    packets, client_address = server.recvfrom(BUFFER_SIZE)     # packets = tamanho do arquivo enviado em num de pacotes
    packets = int(data.decode())
    
    with open(file_path, 'wb+') as file:
        for i in range(packets):
            data, client_address = server.recvfrom(BUFFER_SIZE)
            file.write(data)
            
def send_file(file_name, client_address):
    file_path = str(FOLDER_PATH / file_name)
    with open(file_path, 'rb') as file:
        data = file.read(BUFFER_SIZE)
        while data:
            if server.sendto(data, client_address):
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
        server.sendto(('received' + file_name).encode(), client_address)
        send_file(file_name, client_address)
    
server.close()
        

