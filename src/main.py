import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse
from sprite import AnimSprite

window = pyglet.window.Window(600,250)
char = AnimSprite()

def first():
  glEnable(GL_BLEND)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  char.addAnim("walkleft", ["../assets/walkleft0.png","../assets/walkleft1.png"], 0.25)
  char.playAnim("walkleft")

#@window.event
#def on_mouse_drag(x, y, dx, dy, button, modifiers):

#@window.event
#def on_mouse_release(x, y, button, modifiers):

@window.event
def on_draw():
  window.clear()
  char.draw()
  

first()
pyglet.app.run()