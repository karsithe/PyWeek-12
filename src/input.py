"""Input module to store keypresses"""

import pyglet
from pyglet.window import key

class Input:
  def __init__(self, window):
    self.keys = key.KeyStateHandler()
    window.push_handlers(self.keys)

  def isDown(k):
    return self.keys[k]
    
  def isUp(k):
    return not self.keys[k]
    
    
