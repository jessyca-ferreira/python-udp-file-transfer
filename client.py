import socket
import os
import math
from pathlib import Path

BUFFER_SIZE = 1024
HOST = 'localhost'
PORT = 5000
FOLDER_PATH = Path('client-files/')
TIMEOUT = 10

dest = (HOST, PORT)             # endereco de destino (servidor)
origin = ('localhost', 3000)    # endereco do cliente

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_file(file_name):
    file_path = str(FOLDER_PATH / file_name)        # caminho onde se encontra o arquivo, localizado na pasta client-filess
    client.sendto(file_name.encode(), dest)         # envio do nome do arquivo ao servidor
    packets = packet_amount(file_path)              # quantidade de pacotes que serão enviados
    client.sendto(packets.encode(), dest)           # informa ao servidor quantos pacotes o client enviará
    
    with open(file_path, 'rb') as file:
        data = file.read(BUFFER_SIZE)
        for i in range(int(packets)):
            if client.sendto(data, dest):
                data = file.read(BUFFER_SIZE)
       
        # o cliente recebe de volta o arquivo enviado ao servidor
        # esse arquivo é salvo em client-files com nome modificado         
        try:
            received_data, server_address = client.recvfrom(BUFFER_SIZE)
            print(received_data.decode())
            receive_file(received_data.decode(), int(packets))
        except:
            pass
        
        
def receive_file(file_name, packets):
    with open(str(FOLDER_PATH / file_name), 'wb') as file:
        for i in range(packets):
            data, server_address = client.recvfrom(BUFFER_SIZE)
            file.write(data)

            
def packet_amount(file_path):
    file_size = os.path.getsize(file_path)
    packet_amount = str(math.ceil(file_size / BUFFER_SIZE))
    return packet_amount

print('Para sair, user CTRL+X\n')

sending = True
while sending:
    file_name = input()         # nome do arquivo a ser enviado, lido pelo console
    if file_name == '\x18':     # condição para fechar a conexão (CTRL+X)
        client.sendto(file_name.encode(), dest)
        sending = False
    else:
        send_file(file_name)
        
client.close()

