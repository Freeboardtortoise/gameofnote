# shader for remap


class Shader:
 def __init__(self, amount):
  self.x = 0
  import math

  self.rays = []

  for angle in range(0, 360, 1):
   rad = math.radians(angle)

   self.rays.append(
    Vector2(
     math.cos(rad),
     math.sin(rad)
    )
   )

 def calculate(self, playerPos):
  # calculating vision
  rays = self.rays
  playerTile = playerPos // 8
  self.visable = set()
  self.visable.add(playerTile)
  
  for ray in rays:
   currentItteration = 0
   itterationLimit = 20
   current = playerTile.dupl()
   stillVisable = True
   while stillVisable == True and currentItteration < itterationLimit:
    currentItteration += 1
    current += ray
    if mget(int(current.x), int(current.y)) not in walkable_blocks:
     stillVisable = False
    self.visable.add(Vector2(int(current.x), int(current.y)))
    # adding a radius




 def shader(self,x,y):
  t = mget(x,y)
  orig = t
  if Vector2(x,y) not in self.visable:
   return (0,x,y)
  if orig not in walkable_blocks:
   if mget(x+1, y) not in walkable_blocks and mget(x-1, y) not in walkable_blocks and mget(x, y+1) not in walkable_blocks and mget(x, y-1) not in walkable_blocks:
    t = 0
  return (t,x,y)


