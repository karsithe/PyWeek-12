"""World module holding all entities in that world and drawing to its own tile"""
import pyglet
from pyglet.gl import *

class World:
    def __init__(self):
        """All member data handles instantiated here"""
        self.entityList = []
        self.scenery = []
        self.interactables = []
        
        self.player = None
        
    
    def init(self):
        """Load in level and prepare for use"""
        blobImage = pyglet.image.load("../assets/testasset.png")
        blob = pyglet.sprite.Sprite(blobImage, x = 50, y = 0)
        self.entityList.append(blob)
    
    
    def update(self, dt):
        # update everything in this world
        for entity in self.entityList:
            entity.update(dt)
        
        #update player if it exists
        
        
    
    def draw(self):
        # maybe convert to batches later
        for drawable in self.entityList:
            drawable.draw()
        
    
    