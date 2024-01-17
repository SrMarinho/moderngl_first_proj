import sys
import pygame as pg
import moderngl
import numpy as np
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer
import dearpygui.dearpygui as dpg
import socket
import threading


class GraphicsEngine:
    def __init__(self, width=1280, height=720) -> None:
        pg.init()

        self.width, self.height = width, height

        self.screen = pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF, display=1)
        self.display = pg.Surface((self.width, self.height))
        self.ctx = moderngl.create_context()
        self.ctx.front_face = 'ccw'
        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.FPS = 60
        
        self.time = pg.time.get_ticks()/1000
        self.delta_time = 0
        
        self.fov = 90
        self.aspect_ratio = width / height
        self.near = 0.1
        self.far = 1000
        
        self.mesh = Mesh(self)
        
        self.scene = Scene(self)
        
        self.scene_renderer = SceneRenderer(self)
        
        # self.socket_server(self)
        
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def update(self):
        self.time = pg.time.get_ticks()/1000
        self.scene.update()
    
    def render(self):
        self.ctx.clear(30/255, 30/255, 60/255)
        
        self.scene_renderer.render()
        
        pg.display.flip()
        
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    def run(self):
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Aguardando conexão na porta {PORT}...")
        t1 = threading.Thread(target=server.accept)
        t1.start()
        # conn, addr = server.accept()
        # print(f"Conectado por {addr}")
        while True:
            self.get_time()
            self.events()
            self.update()
            self.render()
            self.delta_time = self.clock.tick(self.FPS)
            
            # data = "Dados a serem enviados"
            # conn.send(data.encode())
            # received_data = conn.recv(1024).decode()
            
            pg.display.set_caption("FPS: " + str(round(self.clock.get_fps(), 2)))
                    

    # def socket_server(self, app):
    #     HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    #     PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #         s.bind((HOST, PORT))
    #         s.listen()
    #         conn, addr = s.accept()
    #         with conn:
    #             print(f"Connected by {addr}")
    #             while True:
    #                 data = conn.recv(1024)
    #                 if not data:
    #                     break
    #                 conn.sendall(data)
if __name__ == '__main__':
    app = GraphicsEngine(200, 200)