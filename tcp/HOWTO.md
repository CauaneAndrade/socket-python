# Socket - conexão Transmission Control Protocol

## Características
- comunicação começa com o cliente
- comunicação em três etapas (THREE-WAY HANDSHAKE)
    - O cliente envia pacote com a flag **SYN** (Synchronize)
        - Cliente: "Servidor, estou enviando uma mensagem. Dá pra sincronizar (**SYN**)?"
    - O servidor responde com um pacote com as flags **SYN** + **ACK** (Acknowledgement)
        - Servidor: "Claro, sincroniza a mensagem 200 (n° de sequência do servidor) que estou enviando (**SYN**). Prossiga com a mensagem 101 (**ACK**)."
    - O cliente responde com um pacote **ACK**
        - Cliente: "OK, estou enviando a mensagem 101. Prossiga com a mensagem 201 (**ACK**)"
    
    ![Exemplo Three-Way Handshake](../images/tcp_three_way_handshake.png)
- Encerramento da conexão ocorre em 4 etapas
    ![Exemplo de fechamento de conexão TCP](../images/tcp_fechamento.png)
    
- é mais lento que o protocolo UDP, pois tem mecanismos de verificação de integridade mais complexo
    - Confiabilidade -> Origem e destino

- Full duplex
    - servidor e cliente podem se comunicar simultâneamente (`que loucura, né`)

## Executando servidor TCP
```Python
python server_tcp.py 
```

## Executando o cliente TCP
Em um novo shell e execute o cliente
```Python
python client_tcp.py
```
---
Nota: Observe que apenas um cliente pode se conectar ao servidor por vez.

---