# title:   gameofnote
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
# this is a test
import random
import math
import time

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
 def __gt__(self, other):
  if isinstance(other, Vector2):
   if self.x > other.x and self.y < other.y:
    return True
  else:
   if self.x > other and self.y > other:
    return True

 def __repr__(self):
  return f"Vector2(x: {self.x},y: {self.y})"
 def dupl(self):
  return Vector2(self.x, self.y)
 def __abs__(self):
  return Vector2(abs(self.x), abs(self.y))




SCREEN_SIZE = (240, 136)

t=0
pos = Vector2(0,0)

invent = 1
inventmen = False
inventbtnPresses = [False, False, False, False]

inventory = {"grass": 10, "planks": 10, "stone": 10, "leaves": 10, "logs": 2, "chest": 1, "":0, "stone pickaxe":1}
inventoryLayout = [["grass", "planks", "stone","leaves","logs",""],
                   ["chest","stone pickaxe","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""]]
sprites = {"grass":103, "planks":104, "":150, "stone":105, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20,
           "stone pickaxe":320, "iron pickaxe": 321, "gold pickaxe": 322, "diamond pickaxe": 323,
           "stone sword": 336, "iron sword": 336, "gold sword": 337, "diamond sword": 338,
           "stone spear": 352, "iron spear": 337, "gold spear": 338, "diamond spear": 339,
           "stone axe": 368, "iron axe":369, "gold axe":370, "diamond axe": 371}
nonPlacables = ["stone pickaxe", "stone sword", "stone axe", "stone spear",
                "iron pickaxe", " iron sword", "iron axe", "iron spear",
                "gold pickaxe", "gold sword", "gold axe", "gold spear",
                "diamond pickaxe", "diamond sword", "diamond axe", "diamond spear"]
breaking_tools = {"stone pickaxe":1, "iron pickaxe": 2, "gold pickaxe": 4, "diamond pickaxe": 5}
placeSprites = {"grass":2, "planks":1, "stone":3, "": 0, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20}
bottomBlocks = ["dark stone", "grass"]
inventorySellection = [0,0]
cBlock = ""

counter = Vector2(0,0)
speed = 1
walkable_blocks = ["grass", "leaves", "dark stone"]
walkable_blocks = [placeSprites[block] for block in walkable_blocks]
bottomBlocksBack = [placeSprites[block] for block in bottomBlocks]


#player stuff
PLAYERMAXHEALTH = 100


playerCurrentHealth = PLAYERMAXHEALTH

class Mob:
 def __init__(self, startPos, health, speed, damage, hostile, sprite, spriteSize, attack_range, collide, attackSpeed):
  # constants
  TOP_MOVEMENT_SPEED = 20
  TOP_DIRECTION_SPEED = 10


  # variables
  self.hp = health
  self.startPos = startPos.dupl()
  self.hostile = hostile
  self.damage = damage
  self.damageTimer = attackSpeed
  self.damageTimerMax = attackSpeed
  self.speed = speed
  self.sprite = sprite
  self.size = spriteSize
  self.range = attack_range
  self.currentPos = self.startPos.dupl()
  #movementAI
  self.direction = Vector2(random.randint(-1,1),random.randint(-1,1))
  self.directionTimer = 10
  self.directionTimerTop = random.randint(10, TOP_DIRECTION_SPEED)
  self.movementTimer = 10
  self.movementTimerTop = random.randint(10, TOP_MOVEMENT_SPEED)

  self.colide = collide
 

 def draw(self, cameraPos):
  spr(self.sprite, int(self.currentPos.x)-cameraPos.x, int(self.currentPos.y)-cameraPos.y, self.size, colorkey=1)
 
 
 def pathfinding(self, move):
  pos = self.currentPos + move
  if mget(int(pos.x / 8), int(pos.y / 8)) not in walkable_blocks or mget(int((pos.x+7) / 8), int((pos.y) / 8)) not in walkable_blocks or mget(int((pos.x) / 8), int((pos.y+7) / 8)) not in walkable_blocks or mget(int((pos.x+7) / 8), int((pos.y+7) / 8)) not in walkable_blocks:
   # try and move only up and down
   if  mget(int((self.currentPos.x / 8)), int((pos.y+7) / 8)) not in walkable_blocks or mget(int((self.currentPos.x+7) / 8), int((pos.y+7) / 8)) not in walkable_blocks:
    move.x = 0
   if mget(int(pos.x / 8), int((self.currentPos.x) / 8)) not in walkable_blocks or mget(int((pos.x+7) / 8), int((self.currentPos.x) / 8)) not in walkable_blocks : 
    move.y = 0

  # do the actual moving
  self.currentPos +=  move
 def damaging(self, playerPos):
  global playerCurrentHealth
  self.damageTimer -= 1
  if self.damageTimer < 0:
   if abs((playerPos - self.currentPos).x) < 8 and abs((playerPos - self.currentPos).y) < 8:
    playerCurrentHealth -= self.damage
    self.damageTimer = self.damageTimerMax

   

 def movement(self, playerPos):
  # hostile movement
  if self.hostile:
   if abs((playerPos - self.currentPos).x) < self.range and abs((playerPos - self.currentPos).y) < self.range:
    # move towards the target
    move_x = 0
    move_y = 0

    if playerPos.x > self.currentPos.x:
     move_x = self.speed
    elif playerPos.x < self.currentPos.x:
     move_x = -self.speed

    if playerPos.y > self.currentPos.y:
     move_y = self.speed
    elif playerPos.y < self.currentPos.y:
     move_y = -self.speed

    self.pathfinding(Vector2(move_x, move_y))


  self.directionTimer -= 1
  #general movement
  if self.movementTimer < 0:
   self.pathfinding(self.direction)
   self.movementTimer = self.movementTimerTop
  self.movementTimer -= 1
  self.directionTimer -= 1
  if self.directionTimer < 0:
   self.directionTimer = self.directionTimerTop
   self.direction = Vector2(random.randint(-1,1),random.randint(-1,1))
   self.directionTimer = self.directionTimerTop

 def loop(self, playerPos):
  self.movement(playerPos)
  if self.hostile:
   self.damaging(playerPos)


stone_map = [
    [False for x in range(SCREEN_SIZE[0])]
    for y in range(SCREEN_SIZE[1])
]

# placing variables
placingMode = False
currentDelta = Vector2(0,0)
currentButtonValues = [False, False, False, False]
MAX_REACH = 4
def placing(player_pos, true_pos):
 global placingMode, currentDelta, currentButtonValues, nonPlacables, breaking_tools, inventory, bottomBlocksBack
 spr(120,0,0)
 for i in range(len(str(inventory[cBlock]))-1):
  spr(121,(i)*8,0)
  spr(122,(i+1)*8,0)
 print(str(inventory[cBlock]), x=1, y=1, color=15, fixed=False, scale=1)
 # 5. Placing blocks (using player's exact world position)
 if btn(4):  # Place block
  if placingMode == False:
   currentDelta = Vector2(0,0)
  placingMode = True
 if placingMode == True:
  # remember that player_pos is relitive to the screen, not the map
  spr(100, int(player_pos.x/8)*8 + 8 * currentDelta.x,int(player_pos.y/8)*8 +  8 * currentDelta.y, colorkey=0)

  if btn(4) == False:
   placingMode = False
   if cBlock in nonPlacables:
    if cBlock in breaking_tools:
     if {value: key for key, value in placeSprites.items()}[mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y)] not in bottomBlocks:
      inventory[{value: key for key, value in placeSprites.items()}[mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y)]] += 1
      mset(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y, placeSprites["grass"])

   else:
    if mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y) != placeSprites[cBlock]:
     if inventory[cBlock] > 0:
      if mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y) in bottomBlocksBack:
       mset(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y, placeSprites[cBlock])
       inventory[cBlock] -= 1

  if currentButtonValues[0] == True:
   if btn(0) == False:
    currentButtonValues[0] = False
    currentDelta.y -= 1
  if currentButtonValues[1] == True:
   if btn(1) == False:
    currentButtonValues[1] = False
    currentDelta.y += 1
  if currentButtonValues[2] == True:
   if btn(2) == False:
    currentButtonValues[2] = False
    currentDelta.x -= 1
  if currentButtonValues[3] == True:
   if btn(3) == False:
    currentButtonValues[3] = False
    currentDelta.x += 1
  if abs(currentDelta.x) > MAX_REACH:
   currentDelta.x += MAX_REACH - currentDelta.x
  if abs(currentDelta.y) > MAX_REACH:
   currentDelta.y += MAX_REACH - currentDelta.y


  if btn(0):
   currentButtonValues[0] = True
  if btn(1):
   currentButtonValues[1] = True
  if btn(2):
   currentButtonValues[2] = True
  if btn(3):
   currentButtonValues[3] = True
 return placingMode


def generate_tree(possition):
 # Set the center trunk first
 mset(possition.x, possition.y, 5)
 
 # Loop through the 3x3 grid
 for y in range(3):
  for x in range(3):
   # Calculate proper relative offsets (-1, 0, 1)
   dx = x - 1
   dy = y - 1
   
   # Skip the center tile so we don't overwrite our trunk (5)
   if dx == 0 and dy == 0:
    pass
   else:
    # Draw the leaves around it
    mset(possition.x + dx, possition.y + dy, 4)
def fill_circle(center, radius, tile):
 for y in range(center.y - radius, center.y + radius + 1):
  for x in range(center.x - radius, center.x + radius + 1):

   # Keep coordinates inside the screen
   if x < 0 or x >= SCREEN_SIZE[0]:
    continue

   if y < 0 or y >= SCREEN_SIZE[1]:
    continue

   # Check if the tile is inside the circle
   dx = x - center.x
   dy = y - center.y

   if dx * dx + dy * dy <= radius * radius:
    mset(x, y, tile)

def generate_caves():
 wormStarters = []
 worms = 10
 # find random stone blocks
 while len(wormStarters) <  worms:
  testPoint = Vector2(random.randint(0,SCREEN_SIZE[0]), random.randint(0,SCREEN_SIZE[1]))
  if mget(testPoint.x, testPoint.y) == 3 and testPoint not in wormStarters:
   wormStarters.append(testPoint)
 # walking worm by worm
 worm_steps = 100
 radius = 3
 speed = 3
 directional_speed = 4
 for worm in wormStarters:
  radius = random.randint(1,3)
  currentPoss = worm
  direction = Vector2(random.randint(-directional_speed,directional_speed), random.randint(-directional_speed,directional_speed))
  for i in range(worm_steps):
   delta = Vector2(random.randint(-speed,speed), random.randint(-speed,speed)) + direction
   if mget(currentPoss.x + delta.x, currentPoss.y + delta.y) == 3:
    currentPoss += delta
    fill_circle(currentPoss, radius + random.randint(radius-1,radius + 1), 20)

def generate_world(seed):
 for y in range(SCREEN_SIZE[1]):
  for x in range (SCREEN_SIZE[0]):
   mset(x, y, placeSprites["grass"])
 random.seed(seed)

 offset_1 = Vector2(random.uniform(0, 100), random.uniform(0,100))
 offset_2 = Vector2(random.uniform(0, 100), random.uniform(0,100))

 forrestoffset_1 = Vector2(random.uniform(0, 100), random.uniform(0,100))
 forrestoffset_2 = Vector2(random.uniform(0, 100), random.uniform(0,100))

 frequency = 0.04
 treeRandomise = 2

 height = Vector2(0,0)
 for y in range(SCREEN_SIZE[1]):
  for x in range(240):
   height = Vector2(x,y) * frequency + offset_1

   heightwave1 = math.sin(height.x) * math.cos(height.y)

   height2 = Vector2(x,y) * frequency * 2.5 + offset_2
   heightwave2 = math.sin(height2.x) * math.cos(height2.y) * 0.4

   total_wave = heightwave1 + heightwave2

   # forest wave
   forrest = Vector2(x,y) * frequency + forrestoffset_2


   forrestwave1 = math.sin(forrest.x) * math.cos(forrest.y)

   forrest2 = Vector2(x,y) * frequency * 2.5 + forrestoffset_2
   forrestwave2 = math.sin(forrest2.x) * math.cos(forrest2.y) * 0.4
   total_forrestWave = forrestwave1 + forrestwave2


   if total_wave > 0.2:
    mset(x, y, placeSprites["stone"])
    stone_map[y][x] = True
   else:
    
    if total_forrestWave > 0.2:
     if x * random.randint(1, treeRandomise) % 4 == 0 and y * random.randint(1, treeRandomise) % 4 == 0:
      generate_tree(Vector2(x,y))
 
 # generating caves
 generate_caves()
 
 


generate_world(random.randint(0,1000))
test = Mob(Vector2(0,0), 100, 0.5, 0.5, True, 277, 2, 100, True, 10)
mobs = []

def display_lives():
 global playerCurrentHealth

 offset = 20
 row = 0

 full_hearts = int(playerCurrentHealth / 10)

 for i in range(full_hearts):
  spr(385, i * 9 + offset, row, colorkey=0)

 if playerCurrentHealth % 10 >= 5:
  spr(384, full_hearts * 9 + offset, row, colorkey=0)

def DeathScreen():
 cls(0)
 print(str("You are dead"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2), color=15, fixed=False, scale=3)
 print(str("Yes you read that correctly"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2)+20, color=15, fixed=False, scale=1)
 time.sleep(10)
 exit()


def TIC():
 global t
 global pos
 global invent, inventmen, cBlock, walkable_blocks
 global inventory, inventoryLayout, inventbtnPresses
 global counter
 global buttonDown, buttonUp, buttonRight, buttonLeft
 global mobs
 if len(mobs) < 10:
  mobs.append(Mob(Vector2(random.randint(0,SCREEN_SIZE[0]*8),random.randint(0, SCREEN_SIZE[1]*8)), 100, 0.5, 0.5, True, 277, 2, 100, True, 10))
 if playerCurrentHealth <= 0:
  DeathScreen()


 SCREEN_W = 240
 SCREEN_H = 136
 SCREEN = Vector2(SCREEN_W, SCREEN_H)
 HALF_W = SCREEN_W // 2
 HALF_H = SCREEN_H // 2
 HALF_SCREEN_SIZE = SCREEN // 2

# Total map size in pixels
 map_pixel_w = SCREEN_SIZE[0] * 8
 map_pixel_h = SCREEN_SIZE[1] * 8

 cls(15)

# 1. Keep player (x, y) strictly within map boundaries
 if pos.x < 0:
  pos.x = 0
 if pos.y < 0:
  pos.y = 0
 if pos.x > map_pixel_w:
  pos.x = map_pixel_w
 if pos.y > map_pixel_h:
  pos.y = map_pixel_h

# 2. Calculate camera position centered on the player
 cam = pos - HALF_SCREEN_SIZE

# Clamp camera so it never scrolls past the map edges
 max_cam = Vector2(map_pixel_w, map_pixel_h) - SCREEN

 if cam.x < 0:
  cam.x = 0
 if cam.x > max_cam.x:
  cam.x = max_cam.x
 if cam.y < 0:
  cam.y = 0
 if cam.y > max_cam.y:
  cam.y = max_cam.y

 map(int((cam.x/speed)/8), int((cam.y/speed)/8), sx=-(cam.x%8), sy=-(cam.y%8))
 for mob in mobs:
  mob.draw(cam)
  mob.loop(pos)
 display_lives()
 if inventmen == True:
  cls(15)
  map(int((pos.x/speed)/8), int((pos.y/speed)/8))

  inventWidth = 15
  inventHeight = 17

  for iy in range(inventHeight):
   for ix in range(inventWidth):
    if iy == 0:
     if ix == 0:
      sprite  = 133
     elif ix == inventWidth-1:
      sprite = 135
     else:
      sprite = 134
    elif iy == inventHeight-1:
     if ix == 0:
      sprite = 165
     elif ix == inventWidth-1:
      sprite = 167
     else:
      sprite = 166
    elif ix == 0:
     sprite = 149
    elif ix == inventWidth-1:
     sprite = 151
    else:
     sprite = 150
    spr(sprite, (240-inventWidth*8) + ix*8, iy*8)

  # doing the layout
  for iy in range(len(inventoryLayout)):
   for ix in range(len(inventoryLayout[0])):
    spr(sprites[inventoryLayout[iy][ix]], ((240-inventWidth*8)+ 16 + 8*ix*2), (0) + 8*iy*2+8, colorkey=0)
    if inventorySellection == [ix,iy]:
     spr(102,  ((240-inventWidth*8)+ 16 + 8*ix*2), (0) + 8*iy*2+8, colorkey=0)
    else:
     spr(101,  ((240-inventWidth*8)+ 16 + 8*ix*2), (0) + 8*iy*2+8, colorkey=0)
  if btn(0): inventbtnPresses[0] = True
  if btn(1): inventbtnPresses[1] = True 
  if btn(2): inventbtnPresses[2] = True
  if btn(3): inventbtnPresses[3] = True
  if btn(4):
   cBlock = inventoryLayout[inventorySellection[1]][inventorySellection[0]]
   inventmen = False
  if inventbtnPresses[0] == True and btn(0) == False:
   inventorySellection[1] -= 1
   inventbtnPresses[0] = False

  if inventbtnPresses[1] == True and btn(1) == False:
   inventorySellection[1] += 1
   inventbtnPresses[1] = False

  if inventbtnPresses[2] == True and btn(2) == False:
   inventorySellection[0] -= 1
   inventbtnPresses[2] = False

  if inventbtnPresses[3] == True and btn(3) == False:
   inventorySellection[0] += 1
   inventbtnPresses[3] = False

  #round the output
  inventorySellection[0] %= len(inventoryLayout[0])
  inventorySellection[1] %= len(inventoryLayout)

  if inventorySellection[0] < 0:
   inventorySellection[0] = len(inventoryLayout[0]) - 1

  if inventorySellection[1] < 0:
   inventorySellection[1] = len(inventoryLayout) - 1
 elif placing(pos-cam, pos) == True:
  pass
 else:

  if btn(0): 
   if mget(int(pos.x / 8), int((pos.y-1) / 8)) in walkable_blocks and mget(int((pos.x+7) / 8), int((pos.y-1) / 8)) in walkable_blocks:
    pos.y -= 1
  if btn(1):
   if mget(int(pos.x / 8), int((pos.y+8) / 8)) in walkable_blocks and mget(int((pos.x+7) / 8), int((pos.y+8) / 8)) in walkable_blocks:
    pos.y += 1
  if btn(2):
   if mget(int((pos.x-1) / 8), int((pos.y) / 8)) in walkable_blocks and mget(int((pos.x-1) / 8), int((pos.y+7) / 8)) in walkable_blocks:
    pos.x -= 1
  if btn(3):
   if mget(int((pos.x+8) / 8), int((pos.y) / 8)) in walkable_blocks and mget(int((pos.x+8) / 8), int((pos.y+7) / 8)) in walkable_blocks:
    pos.x += 1



# 3. Render map using the camera coordinates


# 4. Render sprite (centered normally, but moves to the edge when near map borders)
  spr(256, pos.x - cam.x, pos.y - cam.y, colorkey=0)
  t += 1




  if btn(5):
   inventmen = True
