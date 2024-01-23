import socket
import threading
import json
import ast
import sys

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
        
        self.data = {}

    def connect(self):
        pass
    
    def send(self, *args):
        self.data = {}
        if len(args) > 1:
            self.client_socket.sendall(json.dumps({"hostname": self.hostname, "function": args[0], "params": args[1]}).encode())
        else:
            self.client_socket.sendall(json.dumps({"hostname": self.hostname, "function": args[0]}).encode())
        if args[0] == 'exit':
            self.close()
            sys.exit()
        return self.recv()
    
    # Fecha o socket do cliente
    def close(self):
        self.client_socket.close()
        
    def recv(self):
        server_msg = None
        while server_msg == None:
            server_msg = self.client_socket.recv(1024)
            server_msg = ast.literal_eval(server_msg.decode())
        return server_msg