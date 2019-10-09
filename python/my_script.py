import socket

print ("Servidor funcionando!")
print ("Aguardado conexão do cliente...")
def server_program():
    # Obtém o nome do host
    host = socket.gethostname()
    port = 5000  # inicia em uma porta acima de 1024

    server_socket = socket.socket()  # Obtem a instancia
    
    server_socket.bind((host, port))  #liga o endereço e a porta do host juntos

    # configurar quantos clientes o servidor pode escutar simultaneamente
    server_socket.listen(2)
    conn, address = server_socket.accept()  # Aceita novas conexões
    print("Conectando de: " + str(address))
    
    while True:
        data = conn.recv(1024).decode() # receber fluxo de dados. não aceita pacote de dados com mais de 1024 bytes
        if not data:
            # se os dados não forem recebidos pausa
            break
        print("Conexão do cliente: " + str(data))
        #data = input(' -> ')
        #conn.send(data.encode())  # Envia dados para o cliente

    conn.close()  # Termina a conexão


if __name__ == '__main__':
    server_program()

