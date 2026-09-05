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





class State_Machine:
 def __init__(self):
  self.inventory = False
  self.menu = False
  self.playing = False
  self.start = False
  # rest of the things
 def set(self, state):
  self.__init__()
  setattr(self, state, True)
 def get(self, state):
  return getattr(self, state)


SCREEN_SIZE = (240, 136)

t=0
pos = Vector2(0,0)

invent = 1
inventmen = False
inventbtnPresses = [False, False, False, False]

inventory = {"grass": 10, "planks": 10, "stone": 10, "leaves": 10, "logs": 2, "chest": 1, "":0, "stone pickaxe":1, "iron ingot": 3, "stone sword": 120}
inventoryLayout = [["grass", "planks", "stone","leaves","logs",""],
                   ["chest","stone pickaxe","iron ingot","","",""],
                   ["","stone sword","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""]]
sprites = {"grass":2, "planks":101, "":150, "stone":3, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20,
           "stone pickaxe":320, "iron pickaxe": 321, "gold pickaxe": 322, "diamond pickaxe": 323,
           "stone sword": 336, "iron sword": 336, "gold sword": 337, "diamond sword": 338,
           "stone spear": 352, "iron spear": 337, "gold spear": 338, "diamond spear": 339,
           "stone axe": 368, "iron axe":369, "gold axe":370, "diamond axe": 371,
           # ores
           "iron ore": 22, "gold ore": 23, "diamond ore": 24,
           "iron ingot": 38, "gold ingot": 39, "diamond peice": 40}
UNDERGROUND = ["stone", "darkstone", "gold ore", "iron ore", "diamond ore"]
ORES = ["iron ore", "gold ore", "diamond ore"]
INVENTORY_ORES = ["iron ingot", "gold ingot", "diamond peice"]
ORES_TO_INVENTORY = {"iron ore":"iron ingot", "gold ore": "gold ingot", "diamond ore": "diamond peice"}
ORES_VEIN_SIZE = {"iron ore": 4, "gold ore": 3, "diamond ore": 2}
WEAPONS = ["stone sword", "iron sword", "gold sword", "diamond sword", "stone spear", "iron spear", "gold spear", "diamond spear"]
WEAPONS_ATTACK = {"stone sword": 12, "iron sword": 20, "diamond sword": 30, "stone spear": 10, "gold spear": 15, "iron spear": 20, "diamond spear": 40, "gold sword": 23}
WEAPONS_DURABILITY = {"stone sword": 120, "iron sword": 200, "gold sword": 50, "diamond sword": 300, " stone spear": 50, "iron spear": 100, "gold spear": 25, "diamond spear": 150}
nonPlacables = ["stone pickaxe", "stone sword", "stone axe", "stone spear",
                "iron pickaxe", " iron sword", "iron axe", "iron spear",
                "gold pickaxe", "gold sword", "gold axe", "gold spear",
                "diamond pickaxe", "diamond sword", "diamond axe", "diamond spear",
                ### ores and ingots
                "iron ingot", "gold ingot", "diamond peice"]
breaking_tools = {"stone pickaxe":1, "iron pickaxe": 2, "gold pickaxe": 4, "diamond pickaxe": 5}
placeSprites = {"grass":2, "planks":1, "stone":3, "": 0, "leaves": 4, "logs": 5, "chest": 18, "dark stone":20}
bottomBlocks = ["dark stone", "grass"]
inventorySellection = [0,0]
cBlock = ""
def reverse(dictionary):
    return {value: key for key, value in dictionary.items()}


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
  self.health = health
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
  # try and move only up and down
  if  mget(int((self.currentPos.x / 8)), int((pos.y+7) / 8)) not in walkable_blocks or mget(int((self.currentPos.x+7) / 8), int((pos.y+7) / 8)) not in walkable_blocks or mget(int((self.currentPos.x / 8)), int((pos.y) / 8)) not in walkable_blocks or mget(int((self.currentPos.x+7) / 8), int((pos.y) / 8)) not in walkable_blocks:
   move.y = 0
  if  mget(int((pos.x / 8)), int((self.currentPos.y+7) / 8)) not in walkable_blocks or mget(int((pos.x+7) / 8), int((self.currentPos.y+7) / 8)) not in walkable_blocks or mget(int((pos.x / 8)), int((self.currentPos.y) / 8)) not in walkable_blocks or mget(int((pos.x+7) / 8), int((self.currentPos.y) / 8)) not in walkable_blocks:
   move.x = 0

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

 def loop(self, playerPos, cam):
  if self.health >= 1:
   self.movement(playerPos)
   if self.hostile:
    self.damaging(playerPos)

   self.draw(cam)


stone_map = [
    [False for x in range(SCREEN_SIZE[0])]
    for y in range(SCREEN_SIZE[1])
]

ATTACKING_SPEED = 10
attacking_timer = ATTACKING_SPEED
# attacking function
def attacking_check():
 global ATTACKING_SPEED, attacking_timer
 global inventory, WEAPONS, cBlock
 attacking_timer -= 1
 if cBlock in WEAPONS:
  if inventory[cBlock] > 0:
   if attacking_timer < 0:
    attacking_timer = ATTACKING_SPEED
    return True
 return False

def attack(player_pos, mobs):
 global WEAPONS_ATTACK, cBlock
 ATTACKING_RANGE = 5
 for mob in mobs:
  if abs(mob.currentPos-player_pos) < Vector2(ATTACKING_RANGE,ATTACKING_RANGE):
   mob.health -= WEAPONS_ATTACK[cBlock]
   inventory[cBlock] -= 1

# placing variables
placingMode = False
currentDelta = Vector2(0,0)
currentButtonValues = [False, False, False, False]
MAX_REACH = 4
def placing(player_pos, true_pos, mobs):
 global placingMode, currentDelta, currentButtonValues, nonPlacables, breaking_tools, inventory, bottomBlocksBack

 # showing the amount of blocks left in the top left corner
 spr(120,0,0)
 for i in range(len(str(inventory[cBlock]))-1):
  spr(121,(i)*8,0)
  spr(122,(i+1)*8,0)
 print(str(inventory[cBlock]), x=1, y=1, color=15, fixed=False, scale=1)

 
 if btn(4):  # Place block
  if placingMode == False:
   currentDelta = Vector2(0,0)
  if cBlock in WEAPONS:
   if attacking_check():
    attack(true_pos, mobs)
  else:
   placingMode = True
 if placingMode == True:
  # remember that player_pos is relitive to the screen, not the map
  spr(100, int(player_pos.x/8)*8 + 8 * currentDelta.x,int(player_pos.y/8)*8 +  8 * currentDelta.y, colorkey=0)
  current = mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y)
  if btn(4) == False:
   placingMode = False
   if cBlock in nonPlacables:
    if cBlock in breaking_tools:
     if reverse(sprites)[current] in ORES:
      if ORES_TO_INVENTORY[reverse(sprites)[current]] in inventory:
       inventory[ORES_TO_INVENTORY[reverse(sprites)[current]]] += 1
      else:
       inventory[ORES_TO_INVENTORY[reverse(sprites)[current]]] = 1
     if reverse(sprites)[current] in UNDERGROUND:
      mset(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y, placeSprites["dark stone"])

     elif reverse(placeSprites)[mget(int(true_pos.x / 8) + currentDelta.x, int(true_pos.y / 8) + currentDelta.y)] not in bottomBlocks:
      inventory[reverse(placeSprites)[current]] += 1
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

def generate_ores(veinRange, number, ore, radius):
 starters = []
 for i in range(number):
  ## find a starting stone tile
  testPoint = Vector2(random.randint(0,SCREEN_SIZE[0]), random.randint(0,SCREEN_SIZE[1]))
  if mget(testPoint.x, testPoint.y) == 3 and testPoint not in starters:
   starters.append(testPoint)
 
 # making the veins
 for vein in starters:
  direction = Vector2(random.randint(-2,2), random.randint(-2,2))
  current = vein.dupl()
  for i in range(random.randint(veinRange[0], veinRange[1])):
   fill_circle(current, radius, ore)
   microMovement = Vector2(random.randint(-1,1), random.randint(-1,1))
   current += direction + microMovement

   

  
def generate_world(seed):
 global ORES, ORES_VEIN_SIZE, sprites
 for y in range(SCREEN_SIZE[1]):
  for x in range (SCREEN_SIZE[0]):
   mset(x, y, placeSprites["grass"])
 random.seed(seed)

 offset_1 = Vector2(random.random() * 100.0, random.random() * 100.0)
 offset_2 = Vector2(random.random() * 100.0, random.random() * 100.0)

 forrestoffset_1 = Vector2(random.random() * 100.0, random.random() * 100.0)
 forrestoffset_2 = Vector2(random.random() * 100.0, random.random() * 100.0)


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
 ## generating ores
 for ore in ORES:
  generate_ores([5,10], 10, sprites[ore], ORES_VEIN_SIZE[ore])
 
 


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

 if int(playerCurrentHealth) % 10 >= 5:
  spr(384, full_hearts * 9 + offset, row, colorkey=0)

def DeathScreen():
 cls(0)
 print(str("You are dead"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2), color=15, fixed=False, scale=3)
 print(str("Yes you read that correctly"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2)+20, color=15, fixed=False, scale=1)
 time.sleep(10)
 exit()


def playerMovement():
 global pos, walkable_blocks
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

def inventory_main():
 global inventory, inventoryLayout, inventbtnPresses
 global invent, inventmen, cBlock, walkable_blocks
 global state
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
  state.set("playing")
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

tempCam = Vector2(0,0)
def start():
 global state
 global tempCam
 cam = tempCam
 speed = 2
 cls(15)
 map(int((cam.x/speed)/8), int((cam.y/speed)/8), sx=-(int(cam.x/speed)%8), sy=-(int(cam.y/speed)%8))
 spr(224, 10,10, colorkey=0, w=11,h=2, scale=2)
 print("Press A to start", 100,100,color=12)
 if btn(4) == True:
  state.set("playing")
 tempCam += Vector2(1, 1)


state = State_Machine()
state.set("start")
def TIC():
 global t
 global pos
 global invent, inventmen, cBlock, walkable_blocks
 global inventory, inventoryLayout, inventbtnPresses
 global counter
 global buttonDown, buttonUp, buttonRight, buttonLeft
 global mobs
 global state
 if len(mobs) < 10:
  mobs.append(Mob(Vector2(random.randint(0,SCREEN_SIZE[0]*8),random.randint(0, SCREEN_SIZE[1]*8)), 100, 0.5, 0.5, True, 277, 2, 100, True, 10))
 if playerCurrentHealth <= 0:
  DeathScreen()

 if state.get("start"):
  start()
 else:
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
   mob.loop(pos, cam)
  display_lives()
  if state.get("inventory"):
   inventory_main()
  elif placing(pos-cam, pos, mobs) == True:
   pass
  elif state.get("playing"):
   playerMovement()
  
# 4. Render sprite (centered normally, but moves to the edge when near map borders)
  spr(256, pos.x - cam.x, pos.y - cam.y, colorkey=0)
  t += 1
  if btn(5):
   state.set("inventory")
