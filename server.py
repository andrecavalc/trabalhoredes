import socket
import time
import threading

from __init__ import handle_client

#isso é um socket(criação)
#socket.AF_INET = IPv4
#socket.SOCK_STREAM = TCP
server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#endereço e porta ligados ao socket
server_socket.bind(("localhost",5555))

#agora o socket vai escutar
server_socket.listen(5)


#se o usuario fizer algo de errado
#exemplo: ctrl+c
#entao exibe a msg da linha abaixo do except
try:
    while True:
    #server aceita a conexão
        connection,address=server_socket.accept()

        # Cria uma thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(connection,))
        client_handler.start()

except KeyboardInterrupt:
    print("\n\nO servidor foi descontinuado!")
    #estamos encerrando a conexão
    server_socket.close()
