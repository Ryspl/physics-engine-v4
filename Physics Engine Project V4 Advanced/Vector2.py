#physics project sim V4

#Vector2 class
import math


class Vector2():
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.normal = Vector2(-self.y, self.x)
    self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
  
  def __add__(self, Vb):
    return Vector2(self.x + Vb.x, self.y + Vb.y)
  
  def __sub__(self, Vb):
    return Vector2(self.x - Vb.x, self.y - Vb.y)
  
  def __mul__(self, scal):
    return Vector2(self.x * scal, self.y * scal) if type(scal) == float else Vector2(self.x * scal.x, self.y * scal.y)

  def __truediv__(self, scal):
    return Vector2(self.x / scal, self.y / scal) if type(scal) == float else Vector2(self.x / scal.x, self.y / scal.y)
  
  def __neg__(self):
    return Vector2(-self.x, -self.y)
  
  def __eq__(self, Vb):
    return self.x == Vb.x and self.y == Vb.y
  
  # def Equals(self, Vb):
  #   pass

  def dotProduct(self, Vb):
    return self.magnitude * Vb.magnitude * math.cos()
  


