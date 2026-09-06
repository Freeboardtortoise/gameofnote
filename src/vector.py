# Vector2(0,0)
# [0,0]
# Vector2 + Vector2
# [v1[0] + v2[0], v1[1] + v2[1]]
class Vector2:
 def __init__(self, x,y):
   self.x = x
   self.y = y
 def __add__(self, other):
  return Vector2(self.x + other.x, self.y + other.y)
 def __sub__(self, other):
  return Vector2(self.x - other.x, self.y - other.y)
 def __mul__(self, other):
  if isinstance(other, (Vector2)):
   return Vector2(self.x * other.x, self.y * other.y)
  else:
   return Vector2(self.x * other, self.y * other)
 def __rmul__(self, scaler):
  return Vector2(self.x * scaler, self.y * scaler)
 def __truediv__(self, scaler):
  return Vector2(self.x / scaler, self.y / scaler)
 def __floordiv__(self, scaler):
  return Vector2(self.x // scaler, self.y // scaler)
 def __iadd__(self, other):
  self.x += other.x
  self.y += other.y
  return self
 def __isub__(self, other):
  self.x -= other.x
  self.y -= other.y
  return self
 def __eq__(self,other):
  if self.x == other.x and self.y == other.y:
   return True
 def __ne__(self, other):
  if self.x == other.x and self.y == other.y:
   return True
  else:
   return False
 def __lt__(self, other):
  if isinstance(other, Vector2):
   if self.x < other.x and self.y < other.y:
    return True
  else:
   if self.x < other and self.y < other:
    return True
  return False
 def __gt__(self, other):
  if isinstance(other, Vector2):
   if self.x > other.x and self.y > other.y:
    return True
  else:
   if self.x > other and self.y > other:
    return True
  return False

 def __repr__(self):
  return f"Vector2(x: {self.x},y: {self.y})"
 def dupl(self):
  return Vector2(self.x, self.y)
 def __abs__(self):
  return Vector2(abs(self.x), abs(self.y))
 def __hash__(self):
  return hash((self.x, self.y))
 def normalize(self):
  output = Vector2(self.x,self.y)
  length = math.sqrt(output.x**2 + output.y**2)
  if length == 0:
   return Vector2(0,0)
  output.x = output.x/length
  output.y = output.y/length
  return output


