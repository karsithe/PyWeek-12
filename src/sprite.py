"""Animated sprite module"""

import pyglet

class AnimSprite:
  def __init__(self):
    self.anims = {}
    self.currentAnim = ""
  
  def init(self):
    pass
  
  def draw(self):
    if not self.currentAnim == "":
      self.anims[self.currentAnim].draw()
  
  def addAnim(self, name, imageNames, time, loop=True):
    images = []
    for i in imageNames:
      images.append(pyglet.image.load(i))
    anim = pyglet.image.Animation.from_image_sequence(images,time,loop)
    sprite = pyglet.sprite.Sprite(anim)
    self.anims[name] = sprite
    
  def playAnim(self, name):
    if not self.anims[name] == None: 
      self.currentAnim = name