import sys
import pygame as pg
import moderngl
import numpy as np
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer

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
        while True:
            self.get_time()
            self.events()
            self.update()
            self.render()
            self.delta_time = self.clock.tick(self.FPS)
            pg.display.set_caption("FPS: " + str(round(self.clock.get_fps(), 2)))
    

if __name__ == '__main__':
    app = GraphicsEngine(600, 600)
    app.run()