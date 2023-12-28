import pygame as pg
import numpy as np

class Cube:
    def __init__(self) -> None:
        self.scale = 60
        self.angleX = 45
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
            self.x += 1
        if keys[pg.K_d]:
            self.x -= 1
            
        if keys[pg.K_q]:
            self.y -= 1
        if keys[pg.K_e]:
            self.y += 1
            
        if keys[pg.K_w]:
            self.angleZ += 1
        if keys[pg.K_s]:
            self.angleZ -= 1
    
    def render(self, screen):
        translationm = Transform.translation((width / 2) + self.x, (height / 2) + self.y, self.z)
        scalem = Transform.scale(cube.scale)
        rotatexm = Transform.rotateX(np.radians(cube.angleX))
        rotateym = Transform.rotateY(np.radians(cube.angleY))
        getXYZWm = Transform.getXYZW()

        for triangle in range(len(cube.triangles)):
            p1 = cube.vertices[cube.triangles[triangle][0]]
            p2 = cube.vertices[cube.triangles[triangle][1]]
            p3 = cube.vertices[cube.triangles[triangle][2]]
            
            p1 = np.matmul(rotatexm, p1)
            p2 = np.matmul(rotatexm, p2)
            p3 = np.matmul(rotatexm, p3)
            
            p1 = np.matmul(rotateym, p1)
            p2 = np.matmul(rotateym, p2)
            p3 = np.matmul(rotateym, p3)

            
            # p1 = multM4V4(projection, p1)
            # p2 = multM4V4(projection, p2)
            # p3 = multM4V4(projection, p3)
            
                
            p1 = np.matmul(scalem, p1)
            p2 = np.matmul(scalem, p2)
            p3 = np.matmul(scalem, p3)
            
            p1 = np.matmul(translationm, p1)
            p2 = np.matmul(translationm, p2)
            p3 = np.matmul(translationm, p3)
            
            # p1 = p1 + [self.x + width / 2, self.y + height  / 2, self.z, 0]
            # p2 = p2 + [self.x + width / 2, self.y + height  / 2, self.z, 0]
            # p3 = p3 + [self.x + width / 2, self.y + height  / 2, self.z, 0]
            
            if triangle == 7: print(p1)
            # break
            Draw.triangle(screen, (255, 255, 255), p1, p2, p3, 1)

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
        fovRad = 1.0 / np.tan(np.radians(fov / 2.0))
        return np.array([
            [aspect_ratio * fovRad, 0.0, 0.0, 0.0],
            [0.0, fovRad, 0.0, 0.0],
            [0.0, 0.0, (-far_plane + near_plane) / (far_plane - near_plane), -1],
            [0.0, 0.0, (-2 * far_plane * near_plane) / (far_plane - near_plane), 0.0]
        ])
    
    @staticmethod
    def getXYZW():    
        return [1, 1, 1, 1]
    
    
        
def MultiplyMatrixVector(m, i):
    o = np.zeros((4))
    o[0] = i[0] * m[0][0] + i[1] * m[1][0] + i[2] * m[2][0] + i[3] * m[3][0]
    o[1] = i[0] * m[0][1] + i[1] * m[1][1] + i[2] * m[2][1] + i[3] * m[3][1]
    o[2] = i[0] * m[0][2] + i[1] * m[1][2] + i[2] * m[2][2] + i[3] * m[3][2]
    o[3] = i[0] * m[0][3] + i[1] * m[1][3] + i[2] * m[2][3] + i[3] * m[3][3]
    
    if (o[3] != 0):
        o[0] /= o[3]
        o[1] /= o[3]
        o[2] /= o[3]

    return o

def multM4V4(m, i):
    o = np.zeros((4))
    o[0] = i[0] * m[0][0] + i[1] * m[0][1] + i[2] * m[0][2] + i[3] * m[0][3]
    o[1] = i[0] * m[1][0] + i[1] * m[1][1] + i[2] * m[1][2] + i[3] * m[1][3]
    o[2] = i[0] * m[2][0] + i[1] * m[2][1] + i[2] * m[2][2] + i[3] * m[2][3]
    o[3] = i[0] * m[3][0] + i[1] * m[3][1] + i[2] * m[3][2] + i[3] * m[3][3]
    
    if (o[2] != 0):
        o[0] /= o[2]
        o[1] /= o[2]

    return o

pg.init()

width, height = 400, 400

screen = pg.display.set_mode((width, height), display=1)
display = pg.Surface((width, height))

clock = pg.time.Clock()

cube = Cube()

fov = 90
near = 0.1
far = 1000.0
aspect_ratio = height / width

projection = Transform.perspective_projection_matriz(fov, aspect_ratio, near, far)

# print(projection)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            
    screen.fill((40, 40, 50))
    

    cube.update()
    
    cube.render(screen)

    pg.display.flip()

    clock.tick(60)
