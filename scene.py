from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        
    def add_object(self, obj):
        obj.name = obj.vao_name + str(sum(isinstance(i, type(obj)) for i in self.objects))
        self.objects.append(obj)
        
    def load(self):
        app = self.app
        add = self.add_object

        # add(Cube(app, pos=(0, 0, -1)))
        # sphere = Sphere(app, pos=[0, 0, -2.5], scale=[1.5, 1.5,1.5])
        # sphere.velocityX = 0.04
        # sphere.velocityY = 0.04
        # sphere.velocityZ = 0.04
        # add(sphere)
        add(Teapot(app, pos=[0, 0, -4]))
        
    def update(self):
        for obj in self.objects:
            obj.update()
            
    def toJson(self):
        data = {}
        scene = {}
        for i in range(len(self.objects)):
            scene[self.objects[i].name] = self.objects[i].toJson()
        data["scene"] = scene
        return str(data)