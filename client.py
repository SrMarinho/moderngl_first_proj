import socket
import threading
import json
import ast

class Client:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.hostname = socket.gethostname()
        # Criação do socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta ao servidor
        self.client_socket.connect((self.host, self.port))
        print(f"Conectado ao servidor em {self.host}:{self.port}")
        
        t1 = threading.Thread(target=self.recv)
        t1.daemon = True
        t1.start()
        
        self.data = None

    def connect(self):
        pass
    
    def send(self, msg):
        self.client_socket.sendall(json.dumps({"name": self.hostname, "msg": msg}).encode())
    
    # Fecha o socket do cliente
    def close(self):
        self.client_socket.close()
        
    def recv(self):
        server_msg = self.client_socket.recv(1024)
        self.data = ast.literal_eval(server_msg.decode())
        # self.data = server_msg.decode()