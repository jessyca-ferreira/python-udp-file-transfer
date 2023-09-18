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
        if handler.queue[0] == 'receive':
            try:    
                data, address = client.rdt_receive()     # tupla (ack, seq, data)
                message = data[2]            
                
                if isinstance(message, tuple):
                    contato = message[0]
                    client_address = message[1]
                    message = message[2]
                                
                    contatos[contato] = client_address
                
                if message != 'ACK':    
                    print(message)
            except:
                pass
            finally:
                handler.queue[0] = 'send'
    
def get_input():
    while True:
        if handler.queue[0] == 'send':
            input_timer = threading.Timer(2.0, set_receive)
            input_timer.start()
            try:
                message = input()              
            except:
                pass
            finally:
                input_timer.cancel()    
                print('\033[1A', end='\x1b[2K')     # código ansi que apaga a linha digitada para que apenas a mensagem enviada seja lida no console
                print('')
                if message == 'bye':
                    exit()
                elif message == 'list':
                    for name in contatos:
                        print(name)
                else:
                    client.rdt_send(message, destination)
                handler.queue[0] = 'receive'
        
def set_receive():
    handler.queue[0] = 'receive'
    
    


username = input('Bem vindo! Digite "hi, meu nome eh <nome_do_usuario>" para se conectar\n')
while not username.startswith('hi, meu nome eh'):
    username = input()

client.rdt_send(username, destination)    

t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=get_input)

t1.start()
t2.start()





        
    