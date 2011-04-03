"""Character module for player controllable character"""
from pyglet.window import key
from sprite import AnimSprite
from input import Input

class Character:
  def __init__(self, input):
    self.sprite = AnimSprite()
    self.input = input
    self.walkSpeed = 1.0
  
  def init(self):
    self.sprite.addAnim("walkleft", ["../assets/walkleft0.png","../assets/walkleft1.png"], 0.25)
    self.sprite.addAnim("walkright", ["../assets/walkright0.png","../assets/walkright1.png"], 0.25)
    self.sprite.playAnim("walkleft")
  
  def update(self, dt):
    self.handleInput()
  
  def draw(self):
    self.sprite.draw()
    pass
 
  def handleInput(self):
    if self.input.isDown(key.A) or self.input.isDown(key.LEFT):
      self.sprite.playAnim("walkleft")
    if self.input.isDown(key.D) or self.input.isDown(key.RIGHT):
      self.sprite.playAnim("walkright")
    
  