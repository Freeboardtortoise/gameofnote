# title:   gameofnote
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
# this is a test


SCREEN_SIZE = (240, 136)

t=0
x=0
y=0

invent = 1
inventmen = False
inventbtnPresses = [False, False, False, False]

inventory = {"grass": 100, "planks": 100, "stone": 100, "leaves": 10, "logs": 2, "chest": 1}
inventoryLayout = [["grass", "planks", "stone","leaves","logs",""],
                   ["chest","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""]]
sprites = {"grass":103, "planks":104, "":150, "stone":105, "leaves": 4, "logs": 5, "chest": 18}
placeSprites = {"grass":2, "planks":1, "stone":3, "": 0, "leaves": 4, "logs": 5, "chest": 18}
inventorySellection = [0,0]
cBlock = ""

xcounter = 1
ycounter = 1
speed = 1
walkable_blocks = ["grass"]
walkable_blocks = [placeSprites[block] for block in walkable_blocks]


# placing variables
placingMode = False
currentDelta = [0,0]
currentButtonValues = [False, False, False, False]
MAX_REACH = 4
def placing(player_pos):
 global placingMode, currentDelta, currentButtonValues
 # 5. Placing blocks (using player's exact world position)
 if btn(4):  # Place block
  if placingMode == False:
   currentDelta = [0,0]
  placingMode = True
 if placingMode == True:
  spr(100, int(player_pos[0]/8)*8 + 8 * currentDelta[0],int(player_pos[1]/8)*8 +  8 * currentDelta[1], colorkey=0)
  if btn(4) == False:
   placingMode = False
   if mget(int(x / 8) + currentDelta[0], int(y / 8) + currentDelta[1]) != placeSprites[cBlock]:
    if inventory[cBlock] > 0:
     mset(int(x / 8) + currentDelta[0], int(y / 8) + currentDelta[1], placeSprites[cBlock])
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
 elif placing(( x - cam_x, y - cam_y)) == True:
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
