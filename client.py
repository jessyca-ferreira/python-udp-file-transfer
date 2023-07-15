import socket

BUFFER_SIZE = 1024
folderPath  = "client-files\\"
HOST = 'localhost'   # Endereço IP do servidor
PORT = 5000          # Porta do servidor
dest = (HOST, PORT)  # Destino para envio dos pacotes

def send(fileName):
    filePath = folderPath + fileName
    try:
        with open(filePath, 'rb') as file:
            while True:
                packet = file.read(BUFFER_SIZE)
                if not packet:
                    break
                client.sendto(packet, dest)
    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")
    except:
        print("Error")

# Instancia um socket UDP
client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Associa o socket ao endereço IP e porta do cliente
client.bind(('localhost', 3000))

print('Para sair use CTRL+X\n')

while True:
    fileName = input()
    if (fileName == '\x18'):
        client.sendto(fileName.encode(), dest)
        break
    
    send(fileName)

client.close()  # Fecha a conexão do socket