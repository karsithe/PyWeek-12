"""WorldView module which shows a defined amount of worlds on the screen at once"""


class WorldView:
    def __init__(self):
        self.worlds = []
        self.visibleWorlds = []
        
    def draw(self):
        for world in self.visibleWorlds:
            world.draw()
    