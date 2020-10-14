# exemplo de servidor UDP
import socket


HOST = ''  # Endereço IP do servidor
PORT = 5002  # Porta que o servidor vai escutar
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)  # socket.SOCK_DGRAM -> USER DATAGRAM PROTOCOL (UDP)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)  # buffer size é 1024 bytes
    print(cliente, msg)

udp.close()

u"""
Na criação do Socket, o `socket.socket()` pode receber até 3 parâmetros: o primeiro é a família de protocolos, o segundo é o tipo de transmissão (TCP ou UDP) e o último é o protocolo de transmissão (IPv4, IPv6).
A função `bind`, em udp.bind(orig), está associando o endereço IP e porta para o processor servidor. Este recebe 3 parâmetros: socket associado para ser registrado, endereço local para vincular ao socket e tamanho do endereço em bytes.
Em `udp.recvfrom(1024)` contém os pacotes que o cliente envia e quem é o cliente, o parâmetro `1024` passado é o tamanho do buffer em bytes.
Por fim, em `udp.close()` é informado ao sistema operacional para terminar o
uso do Socket.
"""