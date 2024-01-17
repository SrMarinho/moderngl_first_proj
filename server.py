import socket
import threading

# Configurações do servidor
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345         # Porta do servidor

# Lista para armazenar os sockets dos clientes
clients = []

# Função para lidar com as mensagens de um cliente específico
def handle_client(client_socket):
    # Envia uma mensagem de boas-vindas para o cliente
    welcome_message = "Bem-vindo ao servidor! Você pode enviar mensagens."
    client_socket.sendall(welcome_message.encode())

    # Loop para receber e retransmitir mensagens do cliente
    while True:
        # Recebe a mensagem do cliente
        client_message = client_socket.recv(1024)
        if not client_message:
            break  # Se a mensagem estiver vazia, o cliente desconectou-se

        # Imprime a mensagem recebida
        print(f"Cliente diz: {client_message.decode()}")

        # Retransmite a mensagem para todos os outros clientes
        for other_client in clients:
            if other_client != client_socket:
                try:
                    other_client.sendall(client_message)
                except socket.error:
                    # Remove clientes que não podem ser alcançados
                    clients.remove(other_client)

    # Fecha o socket do cliente
    clients.remove(client_socket)
    client_socket.close()

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e à porta
server_socket.bind((host, port))

# Habilita o servidor para aceitar conexões
server_socket.listen()

print(f"Aguardando conexões em {host}:{port}...")

while True:
    # Aguarda a conexão do cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    # Adiciona o socket do cliente à lista
    clients.append(client_socket)

    # Inicia uma nova thread para lidar com o cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
