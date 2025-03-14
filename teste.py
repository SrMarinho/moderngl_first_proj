import pygame as pg
import numpy as np

class Engine:
    def __init__(self):
        self.fov = None
        self.viewport_width = None
        self.viewport_height = None
        self.zNear = None
        self.zFar = None
        self.perspective_matrix = None
        
        self.render_list = []
    
    def update(self):
        for obj in self.render_list:
            obj.update()
    
    def render(self, screen):
        for obj in self.render_list:
            translationm = Transform.translation(obj.x, obj.y, obj.z)
            obj_centeredm = Transform.translation(obj.center_of_mass[0], obj.center_of_mass[1], obj.center_of_mass[2])
            centerm = Transform.translation(width / 2, height / 2, 0)
            scalem = Transform.scale(obj.scale)
            rotatexm = Transform.rotateX(np.radians(obj.angleX))
            rotateym = Transform.rotateY(np.radians(obj.angleY))
            rotatezm = Transform.rotateZ(np.radians(obj.angleZ))

            for triangle in range(len(obj.triangles)):
                p1 = obj.vertices[obj.triangles[triangle][0]]
                p2 = obj.vertices[obj.triangles[triangle][1]]
                p3 = obj.vertices[obj.triangles[triangle][2]]
                
                #ajustando centro de massa para que o eixo de rotação desejado
                p1 = multM4V4(obj_centeredm, p1)
                p2 = multM4V4(obj_centeredm, p2)
                p3 = multM4V4(obj_centeredm, p3)
                
                #rotação no eixo x
                p1 = multM4V4(rotatexm, p1)
                p2 = multM4V4(rotatexm, p2)
                p3 = multM4V4(rotatexm, p3)
                
                #rotação no eixo y
                p1 = multM4V4(rotateym, p1)
                p2 = multM4V4(rotateym, p2)
                p3 = multM4V4(rotateym, p3)
                
                #rotação no eixo z
                p1 = multM4V4(rotatezm, p1)
                p2 = multM4V4(rotatezm, p2)
                p3 = multM4V4(rotatezm, p3)
                
                #Transladando para a posição no mundo
                p1 = multM4V4(translationm, p1)
                p2 = multM4V4(translationm, p2)
                p3 = multM4V4(translationm, p3)
                    
                #Projetando
                p1 = multM4V4(self.perspective_matrix, p1)
                p2 = multM4V4(self.perspective_matrix, p2)
                p3 = multM4V4(self.perspective_matrix, p3)
                
                if p1[3] != 0:
                    p1 /= p1[3] 
                if p2[3] != 0:
                    p2 /= p2[3]
                if p3[3] != 0:
                    p3 /= p3[3]
                
                #Aumentando escala para a desejada
                p1 = multM4V4(scalem, p1)
                p2 = multM4V4(scalem, p2)
                p3 = multM4V4(scalem, p3)
                
                #Centralizando na tela
                p1 = multM4V4(centerm, p1)
                p2 = multM4V4(centerm, p2)
                p3 = multM4V4(centerm, p3)

                Draw.triangle(screen, (255, 255, 255), p1, p2, p3, 1)
            
    def add_obj(self, obj):
        self.render_list.append(obj)
        
    def perspective(self, fov, width, height, near, far):
        self.fov = fov
        self.viewport_width = width
        self.viewport_height = height
        self.zNear = near
        self.zFar = far
        
        aspect_ratio = height/width
        tan_half_fovy = np.tan(np.radians(fov * 0.5))
        self.perspective_matrix = np.array([
            [1 / (aspect_ratio * tan_half_fovy), 0.0, 0.0, 0.0],
            [0.0, 1 / (tan_half_fovy), 0.0, 0.0],
            [0.0, 0.0, (far) / (far - near), -1],
            [0.0, 0.0, -(far * near) / (far - near), 0.0]
        ])
        
        return self.perspective_matrix
    

class Cube:
    def __init__(self) -> None:
        self.scale = 30
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0

        self.x = 0
        self.y = 0
        self.z = 0
        

        cube = []
        for z in range(2):
            for y in range(2):
                for x in range(2):
                    # cube.append([-1 if x == 0 else 1, -1 if y == 0 else 1, -1 if z == 0 else 1, 1.0])
                    cube.append([x, y, z, 1.0])

        self.vertices = np.array(cube)

        # [[0, 0, 0, 1.0], [1, 0, 0, 1.0], [0, 1, 0, 1.0], [1, 1, 0, 1.0], [0, 0, 1, 1.0], [1, 0, 1, 1.0], [0, 1, 1, 1.0], [1, 1, 1, 1.0]]
        self.triangles = [
            [0, 2, 3], [0, 3, 1],
            [1, 3, 7], [1, 7, 5],
            [2, 6, 7], [2, 7, 3],
            [4, 2, 0], [4, 6, 2],
            [5, 6, 4], [5, 7, 6],
            [5, 0, 1], [5, 4, 0],
        ]
        
        self.center_of_mass = [-sum(p[0] for p in self.vertices) / len(self.vertices),
                  -sum(p[1] for p in self.vertices) / len(self.vertices),
                  -sum(p[2] for p in self.vertices) / len(self.vertices),
                  1.0]
    
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


class Sphere:
    def __init__(self) -> None:
        self.scale = 25
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0

        self.x = 0
        self.y = 0
        self.z = 0
        

        radius = 1
        
        self.vertices = []
        normals = []
        texCoords = []

        sectorCount = 10
        stackCount = 5

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
                self.vertices.append([round(x, 3), round(y, 3), round(z, 3), 1])

                # normalized vertex normal (nx, ny, nz)
                nx = x * lengthInv
                ny = y * lengthInv
                nz = z * lengthInv
                normals.append([round(nx, 3), round(ny, 3), round(nz, 3)] * 6)

                # vertex tex coord (s, t) range between [0, 1]
                s = float(j) / sectorCount
                t = float(i) / stackCount
                texCoords.append([s, t])

        # Convert lists to NumPy arrays
        self.vertices = np.array(self.vertices, dtype=np.float32)
        normals = np.array(normals, dtype=np.float32).reshape(len(normals) * 6, 3)
        texCoords = np.array(texCoords, dtype=np.float32)

        self.triangles = []
        k1, k2 = 0, 0

        for i in range(stackCount):
            k1 = i * (sectorCount + 1)  # beginning of current stack
            k2 = k1 + sectorCount + 1  # beginning of next stack

            for j in range(sectorCount):
                self.triangles.append([k1, k2, k1 + 1])

                self.triangles.append([k2, k1 + 1, k2 + 1])

                k1 += 1
                k2 += 1

        # Convert lists to NumPy arrays
        self.triangles = np.array(self.triangles, dtype=np.int32)
        print(len(self.triangles))
        
        self.center_of_mass = [-sum(p[0] for p in self.vertices) / len(self.vertices),
                  -sum(p[1] for p in self.vertices) / len(self.vertices),
                  -sum(p[2] for p in self.vertices) / len(self.vertices),
                  1.0]
        
    
    def update(self):
        pass

class Draw:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def triangle(screen, color, p1, p2, p3, width=0):
        pg.draw.polygon(screen, color, [p1[:2], p2[:2], p3[:2]], width)
        # pg.draw.line(screen, color, p1[:2], p2[:2], width)
        # pg.draw.line(screen, color, p2[:2], p3[:2], width)
        
class Transform:
    def __init__(self) -> None:
        pass

    @staticmethod
    def rotateX(angle):
        return [
            [1,             0,              0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle),  np.cos(angle), 0],
            [0,             0,              0, 1]
        ]
    
    @staticmethod
    def rotateY(angle):
        return [
            [np.cos(angle), 0, np.sin(angle), 0],
            [0,             1,              0, 0],
            [-np.sin(angle), 0, np.cos(angle), 0],
            [0,             0,              0, 1]
        ]
        
    @staticmethod
    def rotateZ(angle):
        return [
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0,             0,              1, 0],
            [0,             0,              0, 1]
        ]
    
    @staticmethod
    def scale(x, y=None, z=None):
        if y == None:
            y = x
        if z == None:
            z = x

        return [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
            ]
        
    @staticmethod
    def translation(x, y, z):
        return [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
            ]
        
    @staticmethod
    def perspective_projection_matriz(fov, aspect_ratio, near_plane, far_plane):
        tan_half_fovy = np.tan(np.radians(fov * 0.5))
        return np.array([
            [1 / (aspect_ratio * tan_half_fovy), 0.0, 0.0, 0.0],
            [0.0, 1 / (tan_half_fovy), 0.0, 0.0],
            [0.0, 0.0, (far_plane) / (far_plane - near_plane), -1],
            [0.0, 0.0, -(far_plane * near_plane) / (far_plane - near_plane), 0.0]
        ])

def multM4V4(m, v):
    o = np.zeros((4))
    
    for row in range(4):
        for col in range(4):
            o[row] += m[row][col] * v[col]
    return o

pg.init()

width, height = 400, 400

screen = pg.display.set_mode((width, height), display=1)
display = pg.Surface((width, height))

clock = pg.time.Clock()


fov = 90
near = 0.1
far = 5.0

engine = Engine()
engine.perspective(fov, width, height, near, far)

sphere = Sphere()
sphere.z = -4
sphere.x -= 1

cube = Cube()
cube.z = -4
cube.x += 1

engine.add_obj(sphere)
engine.add_obj(cube)

while True:
    # break
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    screen.fill((40, 40, 50))

    engine.update()

    sphere.angleX += 1
    sphere.angleY += 1
    
    cube.angleX -= 1
    cube.angleY -= 1

    engine.render(screen)
    

    pg.display.flip()
    clock.tick(60)
