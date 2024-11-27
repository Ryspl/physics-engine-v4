#physics project sim V4
import Vector2
#shapes classes

class Ball():

  def __init__(self, center, radius, color, mass, VelX, VelY):
    self.center = center
    self.radius = radius
    self.color = color
    self.mass = mass
    self.inertia = 1/4 * self.mass * (self.radius ** 2)   #2/3 for sphere
    self.angle = 0
    self.acceleration = 0
    self.velocity = Vector2(0,0)
  



