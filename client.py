import socket

#isso é um socket(criação)
client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#conectar ao servidor
client_socket.connect(("localhost",5555))




client_socket.close()
