import sys
import threading
import pygame as pg
import moderngl
import numpy as np
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer
import dearpygui.dearpygui as dpg
import server
from pygame._sdl2 import Window
import sys
import subprocess

class GraphicsEngine:
    def __init__(self, width=1280, height=720) -> None:
        pg.init()

        self.width, self.height = width, height

        self.screen = pg.display.set_mode((width, height), pg.OPENGL | pg.DOUBLEBUF | pg.NOFRAME, display=1)
        self.display = pg.Surface((self.width, self.height))
        self.ctx = moderngl.create_context()
        self.ctx.front_face = 'ccw'
        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.time = pg.time.get_ticks()/1000
        self.delta_time = 0
        
        self.render_mode = moderngl.TRIANGLES
        
        self.fov = 90
        self.aspect_ratio = width / height
        self.near = 0.1
        self.far = 1000
        
        self.mesh = Mesh(self)
        
        self.scene = Scene(self)
        
        self.scene_renderer = SceneRenderer(self)
        
        self.running = True
        # self.socket_server(self)
        
    
    def events(self):
        for event in pg.event.get():
            key = pg.key.get_pressed()
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                
            if key[pg.K_8]:
                self.render_mode = moderngl.LINES
            if key[pg.K_9]:
                self.render_mode = moderngl.TRIANGLES
            
    def update(self):
        self.time = pg.time.get_ticks()/1000
        self.scene.update()
    
    def render(self):
        self.ctx.clear(70/255, 70/255, 70/255)
        
        self.scene_renderer.render()
        
        pg.display.flip()
        
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    def run(self):
        while self.running:
            self.get_time()
            self.events()
            self.update()
            self.render()
            self.delta_time = self.clock.tick(self.FPS)
            pg.display.set_caption("FPS: " + str(round(self.clock.get_fps(), 2)))
    
    def get_scene(self):
        return self.scene.toJson()
    
    def set_obj(self, params):
        return app.scene.objects[params['obj']]
    
    def set_obj_pos(self, params):
        try:
            obj = list(filter(lambda x: x.name == params['obj_name'], app.scene.objects))
            obj = obj[0] if obj else None
            field = list(params)[1]
            index = list(params[field])
            value = params[field][index[0]]
            obj_attrib = getattr(obj, field)
            obj_attrib[int(index[0])] = value
            return True
        except:
            return False
        
    def get_win_setting(self):
        return {'size': [app.width, app.height], 'position': Window.from_display_module().position}
    
    def get_render_mode(self):
        if self.render_mode == moderngl.LINES:
            return 1
        return 0

    def set_render_mode(self, mode):
        try:
            if mode == '1':
                self.render_mode == moderngl.LINES 
            else:
                self.render_mode == moderngl.TRIANGLES
            return True
        except:
            return False
    
    def exit(self):
        self.running = False
        
    def gui(self):
        subprocess.call('.\opengl\Scripts\python.exe gui.py')

if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 12345
    
    app = GraphicsEngine(200, 200)
    
    server = server.Server(HOST, PORT)
    server.add_route("get_scene", app.get_scene)
    server.add_route("set_obj", app.set_obj)
    server.add_route("set_obj_pos", app.set_obj_pos)
    server.add_route("get_win_setting", app.get_win_setting)
    server.add_route("exit", app.exit)
    
    t1 = threading.Thread(target=app.gui)
    t1.daemon = True
    t1.start()
    
    app.run()
    
    sys.exit()