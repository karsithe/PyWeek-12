import pyglet
from pyglet.gl import *
from input import Input
from character import Character

window = pyglet.window.Window(600,250)
input = Input(window)
char = Character(input)

def first():
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  char.init()

@window.event
def on_draw():
  window.clear()
  char.draw()
  
first()
pyglet.app.run()