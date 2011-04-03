"""Animated sprite module"""

import pyglet

class AnimSprite:
  def __init__(self):
    self.anims = {}
    self.currentAnim = ""
  
  def init(self):
    pass
  
  def draw(self, x, y):
    if not self.currentAnim == "":
      self.anims[self.currentAnim].x = x
      self.anims[self.currentAnim].y = y
      self.anims[self.currentAnim].draw()
  
  def addAnim(self, name, imageNames, time, scale=1.0, loop=True):
    images = []
    for i in imageNames:
      images.append(pyglet.image.load(i))
    anim = pyglet.image.Animation.from_image_sequence(images,time,loop)
    sprite = pyglet.sprite.Sprite(anim)
    sprite.scale = scale
    self.anims[name] = sprite
    
  def playAnim(self, name):
    if not self.anims[name] == None: 
      self.currentAnim = name