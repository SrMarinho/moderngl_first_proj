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

        # add(Cube(app, pos=(0, 0, 0)))
        add(Sphere(app, pos=(0, 0, 0), scale=(0.2, 0.2, 0.2)))
        
    def update(self):
        for obj in self.objects:
            obj.update() 