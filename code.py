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


SCREEN_SIZE = (240, 136)

t=0
x=0
y=0

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

xcounter = 1
ycounter = 1
speed = 1
walkable_blocks = ["grass", "leaves", "dark stone"]
walkable_blocks = [placeSprites[block] for block in walkable_blocks]
bottomBlocksBack = [placeSprites[block] for block in bottomBlocks]

stone_map = [
    [False for x in range(SCREEN_SIZE[0])]
    for y in range(SCREEN_SIZE[1])
]

# placing variables
placingMode = False
currentDelta = [0,0]
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
   currentDelta = [0,0]
  placingMode = True
 if placingMode == True:
  spr(100, int(player_pos[0]/8)*8 + 8 * currentDelta[0],int(player_pos[1]/8)*8 +  8 * currentDelta[1], colorkey=0)
  if btn(4) == False:
   placingMode = False
   if cBlock in nonPlacables:
    if cBlock in breaking_tools:
     if {value: key for key, value in placeSprites.items()}[mget(int(player_pos[0] / 8) + currentDelta[0], int(player_pos[1] / 8) + currentDelta[1])] not in bottomBlocks:
      inventory[{value: key for key, value in placeSprites.items()}[mget(int(true_pos[0] / 8) + currentDelta[0], int(true_pos[1] / 8) + currentDelta[1])]] += 1
      mset(int(true_pos[0] / 8) + currentDelta[0], int(true_pos[1] / 8) + currentDelta[1], placeSprites["grass"])

   else:
    if mget(int(true_pos[0] / 8) + currentDelta[0], int(true_pos[1] / 8) + currentDelta[1]) != placeSprites[cBlock]:
     if inventory[cBlock] > 0:
      if mget(int(true_pos[0] / 8) + currentDelta[0], int(true_pos[1] / 8) + currentDelta[1]) in bottomBlocksBack:
       mset(int(true_pos[0] / 8) + currentDelta[0], int(true_pos[1] / 8) + currentDelta[1], placeSprites[cBlock])
       inventory[cBlock] -= 1

  if currentButtonValues[0] == True:
   if btn(0) == False:
    currentButtonValues[0] = False
    currentDelta[1] -= 1
  if currentButtonValues[1] == True:
   if btn(1) == False:
    currentButtonValues[1] = False
    currentDelta[1] += 1
  if currentButtonValues[2] == True:
   if btn(2) == False:
    currentButtonValues[2] = False
    currentDelta[0] -= 1
  if currentButtonValues[3] == True:
   if btn(3) == False:
    currentButtonValues[3] = False
    currentDelta[0] += 1
  if abs(currentDelta[0]) > MAX_REACH:
   currentDelta[0] += MAX_REACH - currentDelta[0]
  if abs(currentDelta[1]) > MAX_REACH:
   currentDelta[1] += MAX_REACH - currentDelta[1]


  if btn(0):
   currentButtonValues[0] = True
  if btn(1):
   currentButtonValues[1] = True
  if btn(2):
   currentButtonValues[2] = True
  if btn(3):
   currentButtonValues[3] = True
 return placingMode


def generate_tree(possition=(0,0)):
 # Set the center trunk first
 mset(possition[0], possition[1], 5)
 
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
    mset(possition[0] + dx, possition[1] + dy, 4)
def fill_circle(center_x, center_y, radius, tile):
 for y in range(center_y - radius, center_y + radius + 1):
  for x in range(center_x - radius, center_x + radius + 1):

   # Keep coordinates inside the screen
   if x < 0 or x >= SCREEN_SIZE[0]:
    continue

   if y < 0 or y >= SCREEN_SIZE[1]:
    continue

   # Check if the tile is inside the circle
   dx = x - center_x
   dy = y - center_y

   if dx * dx + dy * dy <= radius * radius:
    mset(x, y, tile)
def generate_world(seed):
 for y in range(SCREEN_SIZE[1]):
  for x in range (SCREEN_SIZE[0]):
   mset(x, y, placeSprites["grass"])
 random.seed(seed)

 offset_x1 = random.uniform(0, 100)
 offset_y1 = random.uniform(0, 100)
 offset_x2 = random.uniform(0, 100)
 offset_y2 = random.uniform(0, 100)

 forrestoffset_x1 = random.uniform(0, 100)
 forrestoffset_y1 = random.uniform(0, 100)
 forrestoffset_x2 = random.uniform(0, 100)
 forrestoffset_y2 = random.uniform(0, 100)

 frequency = 0.04
 treeRandomise = 2

 for y in range(SCREEN_SIZE[1]):
  for x in range(240):
   heightx = (x * frequency) + offset_x1
   heighty = (y * frequency) + offset_y1

   heightwave1 = math.sin(heightx) * math.cos(heighty)

   heightnx2 = (x * (frequency * 2.5)) + offset_x2
   heightny2 = (y * (frequency * 2.5)) + offset_y2
   heightwave2 = math.sin(heightnx2) * math.cos(heightny2) * 0.4

   total_wave = heightwave1 + heightwave2

   # forest wave
   forrestx = (x * frequency) + forrestoffset_x1
   forresty = (y * frequency) + forrestoffset_y1

   forrestwave1 = math.sin(forrestx) * math.cos(forresty)

   forrestnx2 = (x * (frequency * 2.5)) + forrestoffset_x2
   forrestny2 = (y * (frequency * 2.5)) + forrestoffset_y2
   forrestwave2 = math.sin(forrestnx2) * math.cos(forrestny2) * 0.4
   total_forrestWave = forrestwave1 + forrestwave2


   if total_wave > 0.2:
    mset(x, y, placeSprites["stone"])
    stone_map[y][x] = True
   else:
    
    if total_forrestWave > 0.2:
     if x * random.randint(1, treeRandomise) % 4 == 0 and y * random.randint(1, treeRandomise) % 4 == 0:
      generate_tree((x,y))
 
 # generating caves
 
 wormStarters = []
 worms = 10
 # find random stone blocks
 while len(wormStarters) <  worms:
  testPoint = [random.randint(0,SCREEN_SIZE[0]), random.randint(0,SCREEN_SIZE[1])]
  if mget(testPoint[0], testPoint[1]) == 3 and testPoint not in wormStarters:
   wormStarters.append(testPoint)
 # walking worm by worm
 worm_steps = 100
 radius = 3
 speed = 3
 directional_speed = 4
 for worm in wormStarters:
  radius = random.randint(1,3)
  currentPoss = worm
  direction = [random.randint(-directional_speed,directional_speed), random.randint(-directional_speed,directional_speed)]
  for i in range(worm_steps):
   delta = [random.randint(-speed,speed) + direction[0], random.randint(-speed,speed) + direction[1]]
   if mget(currentPoss[0] + delta[0], currentPoss[1] + delta[1]) == 3:
    currentPoss = [currentPoss[0] + delta[0], currentPoss[1] + delta[1]]
    fill_circle(currentPoss[0], currentPoss[1], radius + random.randint(radius-1,radius + 1), 20)



generate_world(random.randint(0,1000))


def TIC():
 global t
 global x
 global y
 global invent, inventmen, cBlock, walkable_blocks
 global inventory, inventoryLayout, inventbtnPresses
 global xcounter, ycounter
 global buttonDown, buttonUp, buttonRight, buttonLeft

 SCREEN_W = 240
 SCREEN_H = 136
 HALF_W = SCREEN_W // 2
 HALF_H = SCREEN_H // 2

# Total map size in pixels
 map_pixel_w = SCREEN_SIZE[0] * 8
 map_pixel_h = SCREEN_SIZE[1] * 8

 cls(15)

# 1. Keep player (x, y) strictly within map boundaries
 if x < 0:
  x = 0
 if y < 0:
  y = 0
 if x > map_pixel_w:
  x = map_pixel_w
 if y > map_pixel_h:
  y = map_pixel_h

# 2. Calculate camera position centered on the player
 cam_x = x - HALF_W
 cam_y = y - HALF_H

# Clamp camera so it never scrolls past the map edges
 max_cam_x = map_pixel_w - SCREEN_W
 max_cam_y = map_pixel_h - SCREEN_H

 if cam_x < 0:
  cam_x = 0
 if cam_x > max_cam_x:
  cam_x = max_cam_x
 if cam_y < 0:
  cam_y = 0
 if cam_y > max_cam_y:
  cam_y = max_cam_y

 map(int((cam_x/speed)/8), int((cam_y/speed)/8), sx=-(cam_x%8), sy=-(cam_y%8))
 if inventmen == True:
  cls(15)
  map(int((x/speed)/8), int((y/speed)/8))

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
 elif placing((x - cam_x, y - cam_y), (x,y)) == True:
  pass
 else:

  if btn(0): 
   if mget(int(x / 8), int((y-1) / 8)) in walkable_blocks and mget(int((x+7) / 8), int((y-1) / 8)) in walkable_blocks:
    y -= 1
  if btn(1):
   if mget(int(x / 8), int((y+8) / 8)) in walkable_blocks and mget(int((x+7) / 8), int((y+8) / 8)) in walkable_blocks:
    y += 1
  if btn(2):
   if mget(int((x-1) / 8), int((y) / 8)) in walkable_blocks and mget(int((x-1) / 8), int((y+7) / 8)) in walkable_blocks:
    x -= 1
  if btn(3):
   if mget(int((x+8) / 8), int((y) / 8)) in walkable_blocks and mget(int((x+8) / 8), int((y+7) / 8)) in walkable_blocks:
    x += 1



# 3. Render map using the camera coordinates


# 4. Render sprite (centered normally, but moves to the edge when near map borders)
  spr(256, x - cam_x, y - cam_y, colorkey=0)
  t += 1




  if btn(5):
   inventmen = True
