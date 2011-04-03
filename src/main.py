import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from sprite import AnimSprite
from worldview import WorldView

window = pyglet.window.Window(600,300)


wView = WorldView()


def init():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    wView.init()



@window.event
def on_draw():
    window.clear()
    #bg.blit(0,0)
    glEnable(GL_BLEND)
    wView.draw()
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #symbols.output.blit(200,0)
    #glDisable(GL_BLEND)


def update(dt):
    pass

init()
pyglet.clock.schedule_interval(update, 1.0/60.0)


pyglet.app.run()