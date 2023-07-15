import socket

BUFFER_SIZE = 1024
HOST = 'localhost'   # Endereço IP do servidor
PORT = 3000          # Porta do servidor
dest = (HOST, PORT)  # Origem para recebimento dos pacotes

# Instancia um socket UDP
server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Associa o socket ao endereço IP e porta do servidor
server.bind(('localhost', 5000))


with open("server-files/answer.bin", "wb") as file:
    while True:
        packet, _ = server.recvfrom(BUFFER_SIZE)
        if not packet or packet == b'\x18':
            break
        file.write(packet)

server.close()  # Fecha a conexão do socket