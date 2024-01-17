import socket

# Configurações do cliente
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345         # Porta do servidor

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((host, port))
print(f"Conectado ao servidor em {host}:{port}")

# Recebe a mensagem de boas-vindas do servidor
welcome_message = client_socket.recv(1024)
print(f"Servidor diz: {welcome_message.decode()}")

# Loop para enviar mensagens para o servidor
while True:
    # Obtém a mensagem do usuário
    message_to_send = input("Digite sua mensagem (ou 'exit' para sair): ")

    # Envia a mensagem para o servidor
    client_socket.sendall(message_to_send.encode())

    # Verifica se o usuário quer sair
    if message_to_send.lower() == 'exit':
        break

# Fecha o socket do cliente
client_socket.close()
