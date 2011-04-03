import pyglet
from pyglet.gl import *
from worldview import WorldView
from input import Input
from character import Character

window = pyglet.window.Window(600,300)
input = Input(window)
char = Character(input)
wView = WorldView()

def init():
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  char.init()
  wView.init()

@window.event
def on_draw():
  window.clear()
  char.draw()
  wView.draw()
 
def update(dt):
    char.update(dt)
 
init()
pyglet.clock.schedule_interval(update, 1.0/60.0)
pyglet.app.run()