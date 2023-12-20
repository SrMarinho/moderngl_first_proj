import sys
import struct
import pygame
import moderngl
import numpy as np


def surf_to_texture(surf):
    tex = ctx.texture(surf.get_size(), 4)
    tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
    tex.swizzle = 'BGRA'
    tex.write(surf.get_view('1'))
    return tex


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

fNear = 0.1
fFar = 10000.0
fFov = 90.0
fAspectRatio = height / width
fFovRad = 1 / np.tan(fFov *  0.5 / 180.0 * np.pi)

matProj = np.zeros((4, 4))

matProj[0][0] = fAspectRatio * fFovRad
matProj[1][1] = fFovRad
matProj[2][2] = fFar / (fFar - fNear)
matProj[3][2] = (-fFar * fNear) / (fFar - fNear)
matProj[2][3] = 1.0

prog['matProj'].value =  matProj.reshape((16))

cube = ctx.buffer(struct.pack('108f',
	0.0, 0.0, 0.0,    0.0, 1.0, 0.0,    1.0, 1.0, 0.0,
	0.0, 0.0, 0.0,    1.0, 1.0, 0.0,    1.0, 0.0, 0.0,
                                                      
	1.0, 0.0, 0.0,    1.0, 1.0, 0.0,    1.0, 1.0, 1.0,
	1.0, 0.0, 0.0,    1.0, 1.0, 1.0,    1.0, 0.0, 1.0,
                                                     
	1.0, 0.0, 1.0,    1.0, 1.0, 1.0,    0.0, 1.0, 1.0,
	1.0, 0.0, 1.0,    0.0, 1.0, 1.0,    0.0, 0.0, 1.0,
                                                      
	0.0, 0.0, 1.0,    0.0, 1.0, 1.0,    0.0, 1.0, 0.0,
	0.0, 0.0, 1.0,    0.0, 1.0, 0.0,    0.0, 0.0, 0.0,
                                                       
	0.0, 1.0, 0.0,    0.0, 1.0, 1.0,    1.0, 1.0, 1.0,
	0.0, 1.0, 0.0,    1.0, 1.0, 1.0,    1.0, 1.0, 0.0,
                                                    
	1.0, 0.0, 1.0,    0.0, 0.0, 1.0,    0.0, 0.0, 0.0,
	1.0, 0.0, 1.0,    0.0, 0.0, 0.0,    1.0, 0.0, 0.0,
))

# Put everything together
vao = ctx.vertex_array(prog, [(cube, '3f', 'vert')])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ctx.clear(0, 0, 0)
    prog['iTime'].value =  pygame.time.get_ticks()/1000
    # prog['iFrame'].value +=  1
    # prog['iMouse'].value =  (pygame.mouse.get_pos()[0] / width, pygame.mouse.get_pos()[1] / height, 0, 0)
    vao.render(moderngl.LINE_LOOP)
    
    pygame.display.flip()

    clock.tick(60)
    