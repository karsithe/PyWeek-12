"""WorldView module which shows a defined amount of worlds on the screen at once"""


class WorldView:
    def __init__(self):
        worlds = []
        
    def draw(self):
        for i in xrange(0,3):
            # push world matrix down
            worlds[i].draw()
    