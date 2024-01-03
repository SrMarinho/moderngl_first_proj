import pygame as pg
import numpy as np
import struct

class Cube:
    def __init__(self) -> None:
        self.scale = 30
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0

        self.x = 0
        self.y = 0
        self.z = 0
        

        # cube = []
        # for z in range(2):
        #     for y in range(2):
        #         for x in range(2):
        #             # cube.append([-1 if x == 0 else 1, -1 if y == 0 else 1, -1 if z == 0 else 1, 1.0])
        #             cube.append([x, y, z, 1.0])

        # self.vertices = np.array(cube)

        # # [[0, 0, 0, 1.0], [1, 0, 0, 1.0], [0, 1, 0, 1.0], [1, 1, 0, 1.0], [0, 0, 1, 1.0], [1, 0, 1, 1.0], [0, 1, 1, 1.0], [1, 1, 1, 1.0]]
        # self.triangles = [
        #     [0, 2, 3], [0, 3, 1],
        #     [1, 3, 7], [1, 7, 5],
        #     [2, 6, 7], [2, 7, 3],
        #     [4, 2, 0], [4, 6, 2],
        #     [5, 6, 4], [5, 7, 6],
        #     [5, 0, 1], [5, 4, 0],
        # ]
        
        self.vertices = struct.pack('108f',
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
        )
        
        # self.center_of_mass = [-sum(p[0] for p in self.vertices) / len(self.vertices),
        #           -sum(p[1] for p in self.vertices) / len(self.vertices),
        #           -sum(p[2] for p in self.vertices) / len(self.vertices),
        #           1.0]
    
    def update(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.angleX += 1
        if keys[pg.K_DOWN]:
            self.angleX -= 1
        if keys[pg.K_LEFT]:
            self.angleY += 1
        if keys[pg.K_RIGHT]:
            self.angleY -= 1
            
        
        if keys[pg.K_a]:
            self.x -= 0.2
        if keys[pg.K_d]:
            self.x += 0.2
            
        if keys[pg.K_q]:
            self.y -= 0.2
        if keys[pg.K_e]:
            self.y += 0.2
            
        if keys[pg.K_w]:
            self.z -= 0.2
        if keys[pg.K_s]:
            self.z += 0.2