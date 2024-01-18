import moderngl as mgl
import numpy as np
import pygame as pg

from operations import *


class BaseModel:
    def __init__(self, app, vao_name, pos=[0, 0, 0], rot=[0, 0, 0], scale=[1, 1, 1]):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = [np.radians(a) for a in rot]
        self.scale = scale
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.program['obj.axis'].value = [0, 0, 0]
        self.velocityX = 0.01
        self.velocityY = 0.01
        self.velocityZ = 0.01

    def update(self): ...

    def render(self):
        self.update()
        self.vao.render()
        
    def toJson(self):
        return {
            "vao_name": self.vao_name,
            "pos": self.pos,
            "rot": self.rot,
            "scale": self.scale
        }


class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, pos, rot, scale):
        super().__init__(app, vao_name, pos, rot, scale)
        self.on_init()

    def update(self): ...

    def on_init(self):
        # resolution
        self.program['u_resolution'].value = [self.app.width, self.app.height]
        self.program['m_proj'].value = create_perspective_matriz(self.app.fov,
                                                       self.app.aspect_ratio,
                                                       self.app.near,
                                                       self.app.far).reshape(16)

class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', pos=[0, 0, 0], rot=[0, 0, 0], scale=[0.5, 0.5, 0.5]):
        super().__init__(app, vao_name, pos, rot, scale)
        self.pos = list(pos)
        self.rot = list(rot)
        self.scale = list(scale)
        
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['obj.axis'].value = self.app.mesh.vao.vbo.vbos[self.vao_name].axis
        
        
    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rot[0] += 1
        if keys[pg.K_DOWN]:
            self.rot[0] -= 1
        if keys[pg.K_LEFT]:
            self.rot[1] += 1
        if keys[pg.K_RIGHT]:
            self.rot[1] -= 1
            
        
        if keys[pg.K_a]:
            self.pos[0] -= self.velocityX
        if keys[pg.K_d]:
            self.pos[0] += self.velocityX
            
        if keys[pg.K_q]:
            self.pos[1] -= self.velocityY
        if keys[pg.K_e]:
            self.pos[1] += self.velocityY
            
        if keys[pg.K_w]:
            self.pos[2] -= self.velocityZ
        if keys[pg.K_s]:
            self.pos[2] += self.velocityZ

        # self.rot[1] += 0.5
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time
        
class Sphere(ExtendedBaseModel):
    def __init__(self, app, vao_name='sphere', pos=[1, 0, 0], rot=[90, 0, 0], scale=[1, 1, 1]):
        super().__init__(app, vao_name, pos, rot, scale)
        self.pos = pos
        self.rot = rot
        self.scale = scale
        
        self.velocityX = 0.01
        self.velocityY = 0.01
        self.velocityZ = 0.01
        
        self.rotation_velocity = 1
        
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['obj.axis'].value = self.app.mesh.vao.vbo.vbos[self.vao_name].axis
        
    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rot[0] += 1
        if keys[pg.K_DOWN]:
            self.rot[0] -= 1
        if keys[pg.K_LEFT]:
            self.rot[1] += 1
        if keys[pg.K_RIGHT]:
            self.rot[1] -= 1
            
        
        if keys[pg.K_a]:
            self.pos[0] -= self.velocityX
        if keys[pg.K_d]:
            self.pos[0] += self.velocityX
            
        if keys[pg.K_q]:
            self.pos[1] -= self.velocityY
        if keys[pg.K_e]:
            self.pos[1] += self.velocityY
            
        if keys[pg.K_w]:
            self.pos[2] -= self.velocityZ
        if keys[pg.K_s]:
            self.pos[2] += self.velocityZ

        # self.rot[1] += 0.5
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time
        
class Teapot(ExtendedBaseModel):
    def __init__(self, app, vao_name='teapot', pos=[0, 0, 0], rot=[0, 0, 0], scale=[1, 1, 1]):
        super().__init__(app, vao_name, pos, rot, scale)
        self.pos = pos
        self.rot = rot
        self.scale = scale
        
        self.velocityX = 0.01
        self.velocityY = 0.01
        self.velocityZ = 0.01
        
        self.rotation_velocity = 1
        
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['obj.axis'].value = self.app.mesh.vao.vbo.vbos[self.vao_name].axis
        
        
    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rot[0] += 1
        if keys[pg.K_DOWN]:
            self.rot[0] -= 1
        if keys[pg.K_LEFT]:
            self.rot[1] += 1
        if keys[pg.K_RIGHT]:
            self.rot[1] -= 1
            
        
        if keys[pg.K_a]:
            self.pos[0] -= self.velocityX
        if keys[pg.K_d]:
            self.pos[0] += self.velocityX
            
        if keys[pg.K_q]:
            self.pos[1] -= self.velocityY
        if keys[pg.K_e]:
            self.pos[1] += self.velocityY
            
        if keys[pg.K_w]:
            self.pos[2] -= self.velocityZ
        if keys[pg.K_s]:
            self.pos[2] += self.velocityZ

        # self.rot[1] += 0.5
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time
            
            
class Floor(ExtendedBaseModel):
    def __init__(self, app, vao_name='teapot', pos=[0, 0, 0], rot=[0, 0, 0], scale=[1, 1, 1]):
        super().__init__(app, vao_name, pos, rot, scale)
        self.pos = pos
        self.rot = rot
        self.scale = scale
        
        self.velocityX = 0.01
        self.velocityY = 0.01
        self.velocityZ = 0.01
        
        self.rotation_velocity = 1
        
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['obj.axis'].value = self.app.mesh.vao.vbo.vbos[self.vao_name].axis
        
        
    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rot[0] += 1
        if keys[pg.K_DOWN]:
            self.rot[0] -= 1
        if keys[pg.K_LEFT]:
            self.rot[1] += 1
        if keys[pg.K_RIGHT]:
            self.rot[1] -= 1
            
        
        if keys[pg.K_a]:
            self.pos[0] -= self.velocityX
        if keys[pg.K_d]:
            self.pos[0] += self.velocityX
            
        if keys[pg.K_q]:
            self.pos[1] -= self.velocityY
        if keys[pg.K_e]:
            self.pos[1] += self.velocityY
            
        if keys[pg.K_w]:
            self.pos[2] -= self.velocityZ
        if keys[pg.K_s]:
            self.pos[2] += self.velocityZ

        # self.rot[1] += 0.5
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time