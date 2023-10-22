import socket

#isso é um socket(criação)
#socket.AF_INET = IPv4
#socket.SOCK_STREAM = TCP
server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#endereço e porta ligados ao socket
server_socket.bind(("localhost",5555))

#agora o socket vai escutar
server_socket.listen(5)

#server aceita a conexão
connection,address=server_socket.accept()

server_socket.close()
