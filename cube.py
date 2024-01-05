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

        self.vertices = struct.pack('108f',
		    0.0, 1.0, 0.0,    0.0, 0.0, 0.0,    1.0, 1.0, 0.0,
		    0.0, 0.0, 0.0,    1.0, 1.0, 0.0,    1.0, 0.0, 0.0,
                                                                  
		    1.0, 1.0, 0.0,    1.0, 0.0, 0.0,    1.0, 1.0, 1.0,
		    1.0, 0.0, 0.0,    1.0, 1.0, 1.0,    1.0, 0.0, 1.0,
                                                                 
		    1.0, 1.0, 1.0,    1.0, 0.0, 1.0,    0.0, 1.0, 1.0,
		    1.0, 0.0, 1.0,    0.0, 1.0, 1.0,    0.0, 0.0, 1.0,
                                                            
		    0.0, 1.0, 1.0,    0.0, 0.0, 1.0,    0.0, 1.0, 0.0,
		    0.0, 0.0, 1.0,    0.0, 1.0, 0.0,    0.0, 0.0, 0.0,
                                                                   
		    0.0, 1.0, 0.0,    1.0, 1.0, 0.0,    0.0, 1.0, 1.0,
		    1.0, 1.0, 0.0,    0.0, 1.0, 1.0,    1.0, 1.0, 1.0,
                                                                
		    0.0, 0.0, 1.0,    1.0, 0.0, 1.0,    0.0, 0.0, 0.0,
		    1.0, 0.0, 1.0,    0.0, 0.0, 0.0,    1.0, 0.0, 0.0,
        )
        
        # self.center_of_mass = [-sum(p[0] for p in self.vertices) / len(self.vertices),
        #           -sum(p[1] for p in self.vertices) / len(self.vertices),
        #           -sum(p[2] for p in self.vertices) / len(self.vertices),
        #           1.0]
        
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')    
    
    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                    (1, 7, 2), (1, 6, 7),
                    (6, 5, 4), (4, 7, 6),
                    (3, 4, 5), (3, 5, 0),
                    (3, 7, 4), (3, 2, 7),
                    (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                                (0, 2, 3), (0, 1, 2),
                                (0, 1, 2), (2, 3, 0),
                                (2, 3, 0), (2, 0, 1),
                                (0, 2, 3), (0, 1, 2),
                                (3, 1, 2), (3, 0, 1),]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        # normals = [( 0, 0, 1) * 6,
        #             ( 1, 0, 0) * 6,
        #             ( 0, 0,-1) * 6,
        #             (-1, 0, 0) * 6,
        #             ( 0, 1, 0) * 6,
        #             ( 0,-1, 0) * 6,]
        
        # print(normals)
        # normals = np.array(normals, dtype='f4').reshape(36, 3)

        # vertex_data = np.hstack([normals, vertex_data])
        # vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data
    
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