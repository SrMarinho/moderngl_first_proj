import sys
import struct
import pygame
import moderngl
import numpy as np


def perspective_matrix(fov, aspect_ratio, near, far):
    fov_rad = np.radians(fov)
    f = 1.0 / np.tan(fov_rad / 2.0)
    z_range = near - far

    perspective_matrix = np.array([
        [f / aspect_ratio, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / z_range, 2 * far * near / z_range],
        [0, 0, -1, 0]
    ])

    return perspective_matrix

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

fFar = 1000.0
fNear = 1
fFov = 90.0
fAspectRatio = height / width

matProj = perspective_matrix(fFov, fAspectRatio, fNear, fFar)

# nMatProj = []
# for y in range(len(matProj)):
#     for x in range(len(matProj[y])):
#         nMatProj.append(matProj[y][x]) 

prog['matProj'].value = matProj.reshape((16))

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
	1.0, 0.0, 1.0,    0.0, 0.0, 0.0,    1.0, 0.0, 0.0
))

cubeAngle = 0

# cube = ctx.buffer(struct.pack('12f',
# 	0.5, -0.5, -0.5,
#     0.5, -0.5, 0.5,
#     -0.5, 0.5, -0.5,
#     -0.5, 0.5, 0.5
# ))

# Put everything together
vao = ctx.vertex_array(prog, [(cube, '3f', 'vert')])

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
    vao.render(moderngl.LINE_STRIP)
    
    pygame.display.flip()

    clock.tick(60)
    