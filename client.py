import socket

#isso é um socket(criação)
client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#conectar ao servidor
client_socket.connect(("localhost",5555))

#receber mensagem do servidor
data_from_server=client_socket.recv(1024)
print(data_from_server.decode("utf-8"))

#estamos encerrando a conexão
client_socket.close()
