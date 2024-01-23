import numpy as np
import moderngl as mgl
import pywavefront


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['sphere'] = SphereVBO(ctx)
        self.vbos['teapot'] = TeapotVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None
        self.axis: list = None
        
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
    
    @staticmethod
    def get_axis(vertex_data):
        if isinstance(vertex_data[0], float):
            vertices = []
            for i in range(3, len(vertex_data), 3):
                aux = []
                aux.append(vertex_data[i])
                aux.append(vertex_data[i + 1])
                aux.append(vertex_data[i + 2])
                vertices.append(aux)
        elif isinstance(vertex_data[0], list) or isinstance(vertex_data[0], tuple) or isinstance(vertex_data[0], np.ndarray):
            return [-sum(p[3] for p in vertex_data) / len(vertex_data),
                    -sum(p[4] for p in vertex_data) / len(vertex_data),
                    -sum(p[5] for p in vertex_data) / len(vertex_data)]
        else:
            return [0, 0, 0]


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']
        self.axis = self.get_axis(self.get_vertex_data())

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
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']
        self.axis = self.get_axis(self.get_vertex_data())

    def get_vertex_data(self):
        # np.set_printoptions(threshold=np.inf)
        radius = 1
        vertices = []
        
        normals = []
        texCoords = []

        sectorCount = 30
        stackCount = 20

        x, y, z, xy = 0.0, 0.0, 0.0, 0.0  # vertex position
        nx, ny, nz, lengthInv = 0.0, 0.0, 0.0, 1.0 / radius  # vertex normal
        s, t = 0.0, 0.0  # vertex texCoord

        sectorStep = 2 * np.pi / sectorCount
        stackStep = np.pi / stackCount
        sectorAngle, stackAngle = 0.0, 0.0

        for i in range(stackCount + 1):
            stackAngle = np.pi / 2 - i * stackStep  # starting from pi/2 to -pi/2
            xy = radius * np.cos(stackAngle)  # r * cos(u)
            z = radius * np.sin(stackAngle)  # r * sin(u)

            for j in range(sectorCount + 1):
                sectorAngle = j * sectorStep  # starting from 0 to 2pi

                # vertex position (x, y, z)
                x = xy * np.cos(sectorAngle)  # r * cos(u) * cos(v)
                y = xy * np.sin(sectorAngle)  # r * cos(u) * sin(v)
                vertices.append([round(x, 3), round(y, 3), round(z, 3)])

                # normalized vertex normal (nx, ny, nz)
                nx = x * lengthInv
                ny = y * lengthInv
                nz = z * lengthInv
                normals.append([round(nx, 3), round(ny, 3), round(nz, 3)])

                # vertex tex coord (s, t) range between [0, 1]
                s = float(j) / sectorCount
                t = float(i) / stackCount
                texCoords.append([s, t])
        # Convert lists to NumPy arrays
        vertices = np.array(vertices, dtype=np.float32)
        normals = np.array(normals, dtype=np.float32)
        texCoords = np.array(texCoords, dtype=np.float32)

        indices = []
        k1, k2 = 0, 0

        for i in range(stackCount):
            k1 = i * (sectorCount + 1)  # beginning of current stack
            k2 = k1 + sectorCount + 1  # beginning of next stack

            for j in range(sectorCount):
                indices.append([k1, k2, k1 + 1])                
                indices.append([k2, k2 + 1, k1 + 1])

                k1 += 1
                k2 += 1

        indices = np.array(indices, dtype=np.int32)
        
        vertex_per_triangle = self.get_data(vertices, indices)
 
        normal_per_triangle = self.get_data(normals, indices)
        
        
        vertex_data = np.hstack([normal_per_triangle, vertex_per_triangle])
        
        return vertex_data
    
class TeapotVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']
        self.axis = self.get_axis(self.get_vertex_data())
        

    @staticmethod
    def get_vertex_data():
        objs = pywavefront.Wavefront('objects/teapot.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')

        return vertex_data