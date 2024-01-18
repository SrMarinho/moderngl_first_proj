import socket
import threading
import json

class Server:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        
        self._thread_server = threading.Thread(target=self.create_server)
        self._thread_server.daemon = True
        self._thread_server.start()
        
        self.routes = {}
    
        self.clients = []
    def create_server(self):
        # Criação do socket do servidor
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Associa o socket ao endereço e à porta
        server_socket.bind((self.host, self.port))

        # Habilita o servidor para aceitar conexões
        server_socket.listen()

        print(f"Aguardando conexões em {self.host}:{self.port}...")

        while True:
            # Aguarda a conexão do cliente
            client_socket, client_address = server_socket.accept()
            print(f"Conexão estabelecida com {client_address}")

            # Adiciona o socket do cliente à lista
            self.clients.append(client_socket)
            # Inicia uma nova thread para lidar com o cliente
            client_thread = threading.Thread(target=self._handle_client, args=(client_socket,))
            client_thread.start()

    def _handle_client(self, client_socket):
        # Loop para receber e retransmitir mensagens do cliente
        while True:
            # Recebe a mensagem do cliente
            client_message = client_socket.recv(1024)
            if not client_message:
                break  # Se a mensagem estiver vazia, o cliente desconectou-se
            
            data = json.loads(client_message.decode())
            
            print(self.routes[data["msg"]["function"]]())
            # if data["msg"]["function"]:
            #     client_socket.sendall(self.routes(data["msg"]["function"])())
        # Fecha o socket do cliente
        self.clients.remove(client_socket)
        
    def broadcast_message(self, message):
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except socket.error:
                # Remove clientes que não podem ser alcançados
                self.clients.remove(client)
                
    def msg_watcher(self, msg):
        while True:
            self.broadcast_message(str(msg))
            
    def add_route(self, name, function):
        self.routes[name] = function