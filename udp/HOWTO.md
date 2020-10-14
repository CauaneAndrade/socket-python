# Socket - conexão User Datagram Protocol

## Características
- não é um protocolo voltado a conexão
    - não estabelece conexão entre origem e o destino
- não há verificação de integridade
- serve para serviços que a perda de algum pacote não comprometa o conteúdo
    - trasmissão de áudio, transmissão de vídeo
- 1 -> n
    - um servidor consegue transmitir pacotes para vários clientes
    - capaz de enviar grande massa de dado em pequeno espaço de tempo


## Características comuns entre TCP e UDP
- usam 16 bits -> porta 0 até 65535
porta de origem e destino

ex:
- ssh, porta padrão 22
- http, porta padrão 80
- https, porta padrão 443

---
Nota: 
se o serviço precisa garantir integridade: TCP, se não precisa UDP.

TCP tem maior custo de infraestrutura de rede

---

## Executando servidor UDP
```Python
python server_udp.py 
```

## Executando o cliente UDP
Em um novo shell e execute o cliente
```Python
python client_udp.py
```