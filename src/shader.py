# shader for remap
class Shader:
 def __init__(self, amount):
  self.x = 0

  self.rays = [Vector2(0,1), Vector2(0,-1), Vector2(1,0), Vector2(-1,0), Vector2(1,1), Vector2(-1,1), Vector2(-1,-1), Vector2(1,-1),
               Vector2(1,2),Vector2(1,-2), Vector2(-1,2), Vector2(-1,-2), Vector2(2,1), Vector2(2,-1), Vector2(-2,1), Vector2(-2,-1)]


 def calculate(self, playerPos):
  # calculating vision
  rays = self.rays
  playerTile = playerPos // 8
  self.visable = set()
  self.visable.add(playerTile)
  
  for ray in rays:
   currentItteration = 0
   itterationLimit = 10
   current = playerTile.dupl()
   stillVisable = True
   while stillVisable == True and currentItteration < itterationLimit:
    currentItteration += 1
    current += ray
    if mget(int(current.x), int(current.y)) not in walkable_blocks:
     stillVisable = False
    self.visable.add(current)
    # adding a radius

    RAD = 2
    for y in range (-RAD, RAD):
     for x in range (-RAD, RAD):
      curr = Vector2(x,y) + current
      self.visable.add(curr)


 def shader(self,x,y):
  t = mget(x,y)
  orig = t
  if Vector2(x,y) not in self.visable:
   return (0,x,y)
  if orig not in walkable_blocks:
   if mget(x+1, y) not in walkable_blocks and mget(x-1, y) not in walkable_blocks and mget(x, y+1) not in walkable_blocks and mget(x, y-1) not in walkable_blocks:
    t = 0
  return (t,x,y)


