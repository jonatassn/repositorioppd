import socket

if __name__ == '__main__':
    HOST = input("Digite o endereco servidor: ")
    PORT = input("Digite a porta do servidor: ")
    BUFSIZ = 4096
    ADDR = (HOST, int(PORT))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    continua = True
    try:
        while(continua):
            dados = input("Digite uma mensagem: ")
            client_socket.send(dados.encode('utf-8'))
            resposta = client_socket.recv(BUFSIZ)
            print(resposta)
            continuar = input("Continuar[s/n]?")
            if continuar.lower() == "n":
                client_socket.send(b"END")
                continua = False
    except KeyboardInterrupt:
        print("Ok, Saindo...")

    client_socket.close()

