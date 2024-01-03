import sys
import struct
import pygame
import moderngl
import numpy as np
from cube import Cube


def create_perspective_matriz(fov, aspect_ratio, near_plane, far_plane):
    aspect_ratio = height/width
    tan_half_fovy = np.tan(np.radians(fov * 0.5))
    return np.array([
        [1 / (aspect_ratio * tan_half_fovy), 0.0, 0.0, 0.0],
        [0.0, 1 / (tan_half_fovy), 0.0, 0.0],
        [0.0, 0.0, (far_plane) / (far_plane - near_plane), -1],
        [0.0, 0.0, -(far_plane * near_plane) / (far_plane - near_plane), 0.0]
    ])


pygame.init()

width, height = 400, 400

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF, display=1)
display = pygame.Surface((width, height))
ctx = moderngl.create_context()

clock = pygame.time.Clock()

with open(f'./programs/vertex_shader.glsl', 'r') as vert_file:
    vert_shader = vert_file.read()
    
with open(f'./programs/fragment_shader.glsl', 'r') as frag_file:
    frag_shader = frag_file.read()

prog = ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)

prog['iResolution'].value = (width, height)
prog['iTime'].value =  pygame.time.get_ticks()/1000
# prog['iFrame'].value =  0
# prog['iMouse'].value =  (0, 0, 0, 0)

fFar = 1000.0
fNear = 0.1
fFov = 90.0
fAspectRatio = height / width

matProj = create_perspective_matriz(fFov, fAspectRatio, fNear, fFar)

prog['matProj'].value = matProj.reshape((16))

cube = Cube()

# Put everything together
vao = ctx.vertex_array(prog, [(ctx.buffer(cube.vertices), '3f', 'vert')])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ctx.clear(30/255, 30/255, 60/255)
    prog['iTime'].value = pygame.time.get_ticks()/1000
    prog['angle'].value = pygame.time.get_ticks()/1000
    # prog['iFrame'].value +=  1
    # prog['iMouse'].value =  (pygame.mouse.get_pos()[0] / width, pygame.mouse.get_pos()[1] / height, 0, 0)
    vao.render(moderngl.LINE_LOOP)
    
    pygame.display.flip()

    clock.tick(60)
    