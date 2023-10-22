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

#vamos dizer ao cliente que o sever aceitou a conexão(mandar mensagem)
mensagem= "conexão aceita"
connection.sendall(mensagem.encode("utf-8"))

#recebimento dos pacotes
while True:
    #recebe msg do cliente
    msg_received = connection.recv(1024)
    #decodifica a msg de bytes para string
    msg_decoded = msg_received.decode("utf-8")
    #verifica se a msg ta vazia (ctrl+c)
    if msg_decoded == "":
        print("\nO cliente encerrou a conexao com o servidor!")
        break
    #printa msg decodificada
    print(msg_decoded)

#estamos encerrando a conexão
server_socket.close()
connection.close()
