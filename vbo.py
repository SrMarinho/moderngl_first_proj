import numpy as np
import moderngl as mgl


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['sphere'] = SphereVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None
        
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '6f'
        self.attribs = ['in_normal_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(0, 0, 1), ( 1, 0,  1), (1,  1,  1), (0, 1,  1),
                    (0, 1, 0), (0, 0, 0), (1, 0, 0), ( 1, 1, 0)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)
    
        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        
        return vertex_data
    
class SphereVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '6f'
        self.attribs = ['in_normal_position']

    def get_vertex_data(self):
        vertices = []
        normals = []
        
        radius = 1
        lengthInv = 1.0 / radius
        
        sectorCount = 10
        stackCount = 10
        sectorStep = 2 * np.pi / sectorCount
        stackStep = np.pi / stackCount

        for i in range(len(stackCount) + 1):
            stackAngle = np.pi / 2 - i * stackStep
            xy = radius * np.cos(stackAngle)
            z = radius * np.sin(stackAngle)

            for j in range(len(sectorCount) + 1):
                sectorAngle = j * sectorStep 
                
                x = xy * np.cos(sectorAngle) 
                y = xy * np.sin(sectorAngle) 
                vertices.append(x)
                vertices.append(y)
                vertices.append(z)

                nx = x * lengthInv
                ny = y * lengthInv
                nz = z * lengthInv
                normals.append(nx)
                normals.append(ny)
                normals.append(nz)
                
        vertex_data = vertices
        vertex_data = np.hstack(vertex_data, normals)
        
        return vertex_data











