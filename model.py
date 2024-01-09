import moderngl as mgl
import numpy as np
import glm

from operations import *


class BaseModel:
    def __init__(self, app, vao_name, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program

    def update(self): ...

    def render(self):
        self.update()
        self.vao.render()


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
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        
    def update(self):
        self.rot[0] += 0.6
        self.rot[1] += 0.4
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time
        
class Sphere(ExtendedBaseModel):
    def __init__(self, app, vao_name='sphere', pos=[0, 0, 0], rot=[0, 0, 0], scale=[1.0, 1.0, 1.0]):
        super().__init__(app, vao_name, pos, rot, scale)
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        
    def update(self):
        self.program['obj.position'].value = self.pos
        self.program['obj.rotation'].value = self.rot
        self.program['obj.scale'].value = self.scale
        self.program['iTime'].value = self.app.time
        
        