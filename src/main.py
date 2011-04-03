import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(600,300)

#@window.event
#def on_mouse_drag(x, y, dx, dy, button, modifiers):


#@window.event
#def on_mouse_release(x, y, button, modifiers):

@window.event
def on_draw():
  window.clear()
  #bg.blit(0,0)
  glEnable(GL_BLEND)
  #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  #symbols.output.blit(200,0)
  #glDisable(GL_BLEND)
        
pyglet.app.run()