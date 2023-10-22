import socket

#isso é um socket(criação)
client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#conectar ao servidor
client_socket.connect(("localhost",5555))

#receber mensagem do servidor
data_from_server=client_socket.recv(1024)
print(data_from_server.decode("utf-8"))

#se o usuario fizer algo de errado
#exemplo: ctrl+c
#entao exibe a msg da linha abaixo do except
try:
    # numero de sequencia do pacote
    seq = 0
    #envio dos pacotes
    while True:
        #sequência atual
        seq+=1
        #captura msg do usuario
        msg_inputed = input(f"{seq}º PACOTE A SER ENVIADO: ")
        #adiciona o numero de sequencia na msg
        msg_seq = f"[{seq}] {msg_inputed}"
        #codifica msg de string para bytes
        msg_encoded = msg_seq.encode("utf-8")
        #envia msg do cliente para o servidor
        data_from_server=client_socket.sendall(msg_encoded)

except KeyboardInterrupt:
    #####################################
    print("\n\nO cliente encerrou a conexao com o servidor!")
    #estamos encerrando a conexão
    client_socket.close()
