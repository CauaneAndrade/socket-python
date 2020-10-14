# Cliente TCP
import socket


SERVER = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5005  # Porta que o Servidor esta escutando
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# o primeiro parâmetro socket.AF_INET especifíca família de endereços da internet, que é a IPv4
# o segundo parâmetro define qual tipo de protocolo de conexão client-server será disponibilizada, socket.SOCK_STREAM é do tipo TCP
dest = (SERVER, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')

data = input()
ctrl_x = '\x18'
while data != ctrl_x:
    tcp.send(data.encode())
    data = input()
tcp.close()


u"""
Em tcp.connect(dest), o método connect recebe o IP e a porta do servidor que vai se conectar.
E em tcp.send(data.encode()) o send envia os pacotes que o cliente envia para o servidor.
"""