"""WorldView module which shows a defined amount of worlds on the screen at once"""
from world import World
from pyglet.gl import *

class WorldView:
    def __init__(self):
        self.worlds = []
        self.visibleWorlds = []

    def init(self):
        # create 9 worlds and collect them
        for i in xrange(0,9):
            newWorld = World()
            newWorld.init(i)
            self.worlds.append(newWorld)

        # grab first 3 worlds
        self.visibleWorlds = self.worlds[:3]


    def draw(self):
        # save current matrix
        glPushMatrix();
        # enable scissoring
        glEnable(GL_SCISSOR_TEST)

        # push view up 200 px for first world
        glTranslatef(0,200,0)
        scissorBottom = 200;

        for world in self.visibleWorlds:
            glScissor(0, scissorBottom, 600, 100)
            world.draw()

            # push world view down each world
            glTranslatef(0,-100.0,0);
            scissorBottom = scissorBottom - 100

        glDisable(GL_SCISSOR_TEST);
        # return old matrix
        glPopMatrix();

    def update(self, dt):
        for world in self.worlds:
            world.update(dt)