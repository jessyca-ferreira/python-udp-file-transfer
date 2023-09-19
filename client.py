import socket
import random
import threading
import rdt      # importa o canal rdt criado no aquivo rdt.py
import queue
import time


LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5000

destination = (LOCALHOST, PORT)  

host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host.bind((LOCALHOST, random.randint(8000, 9999)))

client = rdt.RDTChannel(host)
contatos = {}

handler = queue.Queue()
handler.put('receive')
lock = threading.Lock()

def receive():
    while True:
        try:    
            data, address = client.rdt_receive()     # tupla (ack, seq, data)
            message = data[2]            
            
            if isinstance(message, tuple):
                contato = message[0]
                client_address = message[1]
                message = message[2]
                            
                contatos[contato] = client_address
            
            print(message)
        except:
            pass
    
def get_input():
    while True:
        try:
            message = input()              
            print('\033[1A', end='\x1b[2K')     # código ansi que apaga a linha digitada para que apenas a mensagem enviada seja lida no console
            print('')
            if message == 'bye':
                exit()
            elif message == 'list':
                for name in contatos:
                    print(name)
            else:
                client.rdt_send(message, destination)
        except:
            pass

username = input('Bem vindo! Digite "hi, meu nome eh <nome_do_usuario>" para se conectar\n')
while not username.startswith('hi, meu nome eh'):
    username = input()
    
client.rdt_send(username, destination)    

t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=get_input)

t1.start()
t2.start()





        
    