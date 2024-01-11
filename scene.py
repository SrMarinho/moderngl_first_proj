from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def load(self):
        app = self.app
        add = self.add_object

        add(Cube(app, pos=(0, 0, 0)))
        # sphere = Sphere(app, pos=[0, 0, -2.5], scale=[1.5, 1.5,1.5])
        # sphere.velocityX = 0.04
        # sphere.velocityY = 0.04
        # sphere.velocityZ = 0.04
        # add(sphere)
        
    def update(self):
        for obj in self.objects:
            obj.update() 