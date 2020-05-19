#Servidor UDP
import socket
HOST = ''  # Endereço IP do servidor
PORT = 5002  # Porta que o servidor vai escutar
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.SOCK_DGRAM -> USER DATAGRAM PROTOCOL (UDP)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg)
udp.close()
