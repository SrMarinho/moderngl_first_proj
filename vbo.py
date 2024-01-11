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
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']        

    def get_vertex_data(self):
        # np.set_printoptions(threshold=np.inf)
        radius = 1
        vertices = []
        
        normals = []
        texCoords = []

        sectorCount = 3
        stackCount = 3

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

            # add (sectorCount+1) self.vertices per stack
            # first and last self.vertices have the same position and normal, but different tex coords
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
                # 2 triangles per sector excluding first and last stacks
                # k1 => k2 => k1+1
                indices.append([k1, k2, k1 + 1])
                indices.append([k2, k2 + 1, k1 + 1])


                k1 += 1
                k2 += 1

        # Convert lists to NumPy arrays
        indices = np.array(indices, dtype=np.int32)
        
        center_of_mass = [-sum(p[0] for p in vertices) / len(vertices),
                  -sum(p[1] for p in vertices) / len(vertices),
                  -sum(p[2] for p in vertices) / len(vertices),
                  1.0]
        
        vertex_per_triangle = self.get_data(vertices, indices)
 
        normal_per_triangle = self.get_data(normals, indices)

        vertex_data = np.hstack([normal_per_triangle, vertex_per_triangle])
        
        return vertex_data