# exemplo de cliente UDP
import socket


SERVER = '127.0.0.1'  # endereço IP do servidor local
PORT = 5002  # porta que o servidor local esta escutando

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # associa o socket à uma porta
dest = (SERVER, PORT)

print ('Para sair use CTRL+X\n')
msg = input()
ctrl_x_bitecode = '\x18'
while msg != ctrl_x_bitecode:
    udp.sendto(msg.encode(), dest)
    msg = input()

udp.close()

u'''
Na criação do Socket, o `socket.socket()` pode receber até 3 parâmetros: o primeiro é a família de protocolos, o segundo é o tipo de transmissão (TCP ou UDP) e o último é o protocolo de transmissão (IPv4, IPv6).
Em `udp.sendto(msg.encode(), dest)` é enviado ao servidor a mensagem do cliente; recebe como parâmetro a mensagem em bytecode e uma tupla que representa o endereço IP e a porta do servidor local.
Ao fim, `udp.close()` informa ao SO para finalizar o uso do Socket.
'''