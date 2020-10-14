# Servidor TCP
import socket


HOST = ''  # Endereco IP do Servidor
PORT = 5005  # Porta que o Servidor vai escutar
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# o primeiro parâmetro socket.AF_INET especifíca família de endereços da internet, que é a IPv4
# o segundo parâmetro define qual tipo de protocolo de conexão client-server será disponibilizada, socket.SOCK_STREAM é do tipo TCP
orig = (HOST, PORT)
tcp.bind(orig)  # o valor passado no bind depende da família de endereço do socket, o socket.AF_INET espera uma tupla com o host e a porta

tcp.listen(1)
# o tcp.listen especifica o número de conexões não aceitas que o sistema permitirá antes de recusar novas conexões
while True:
    con, cliente = tcp.accept()
    # tcp.accept aguarda ou bloquei uma nova conexão
    # quando um cliente se conecta é retornado um novo objeto socket
    print ('Conectado por ', cliente)
    while True:
        data = con.recv(1024)
        # con.recv(1024) lê todos os dados que o cliente envia
        if not data: break
        print(data)
    print('Finalizando conexao do cliente', cliente)
    con.close()


u"""
Na criação do Socket, o socket.socket() pode receber até 3 parâmetros: o primeiro é a família de protocolos, o segundo é o tipo de transmissão, podendo ser TCP ou UDP; e o último parâmetro é o protocolo de transmissão (IPv4 ou IPv6). <br>
O método `tcp.bind(orig)` é utilizada apenas pelo servidor, uma vez que associa um determinado endereço IP e porta TCP para o processo servidor. <br>
Em `tcp.listen(1)` indica ao SO para colocar o socket em modo de espera para aguardar conexões de clientes, o valor `1` passado ao método define o número de conexões não aceitas que o sistema permitirá antes de recusar novas conexões. <br>
O `tcp.accept()` aguarda ou bloquei uma nova conexão, uando um cliente se conecta é retornado um novo socket. <br>
Ainda, em `con.recv(1024)` é lido os dados que o cliente envia, e o o parâmetro 1024 passado é o tamanho do buffer em bytes.
"""