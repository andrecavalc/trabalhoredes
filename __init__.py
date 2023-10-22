# function to helps parallelism
def handle_client(connection):
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

        #simular erro de timeout
        # time.sleep(3)

        #envia confirmacao que a msg chegou
        msg_to_confirm = "\nChegou tudo certo aqui, visse servidor?!\n"
        #codifica msg de string para bytes
        msg_encoded = msg_to_confirm.encode("utf-8")
        connection.sendall(msg_encoded)

    #estamos encerrando a conexão
    connection.close()
