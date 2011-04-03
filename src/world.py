"""World module holding all entities in that world and drawing to its own tile"""

from pyglet.gl import *

class World:
    def __init__(self):
        """All member data handles instantiated here"""
        self.entityList = []
        self.scenery = []
        self.interactables = []
        
        self.position = 0;
        
    def init(self):
        """Load in level and prepare for use"""
        
        pass
    
    
    def update(self, dt):
        for entity in entityList:
            entity.update(dt)
        
        
        pass
    
    def draw(self):
        
        
        pass


    
    