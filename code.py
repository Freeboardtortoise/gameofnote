# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python
# this is a test

t=0
x=0
y=0

invent = 1
inventmen = False
inventbtnPresses = [False, False, False, False]
inventory = {"grass": 100, "planks": 100, "stone": 100}
inventoryLayout = [["grass", "planks", "stone","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""],
                   ["","","","","",""]]
sprites = {"grass":103, "planks":104, "":150, "stone":105}
placeSprites = {"grass":2, "planks":1, "stone":3}
inventorySellection = [0,0]

xcounter = 1
ycounter = 1
speed = 1




def TIC():
 global t
 global x
 global y
 global invent, inventmen
 global inventory, inventoryLayout, inventbtnPresses
 global xcounter, ycounter
 global buttonDown, buttonUp, buttonRight, buttonLeft
 if inventmen == True:
  cls(15)
  map(x, y)

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
   invent = sprites[inventoryLayout[inventorySellection[1]][inventorySellection[0]]]
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
 else:
  if btn(0) and ycounter > speed:
   y -= 1
   ycounter = 0
  if btn(1) and ycounter < -speed:
   y += 1
   ycounter = 0
  if btn(2) and xcounter > speed:
   x -= 1
   xcounter = 0
  if btn(3) and xcounter < -speed:
   x += 1
   xcounter = 0

  if btn(0): ycounter += 1
  if btn(1): ycounter -= 1
  if btn(2): xcounter += 1
  if btn(3): xcounter -= 1

  cls(15)
  map(x,y, sx=x%8, sy=y%8)
  spr(49, int(240/2), int(136/2))
  t+=1

  # placing blocks
  if btn(4): #place
   mset(int((240/2)/8)+x, int((136/2)/8)+y,invent)
 if btn(5):
  inventmen = True

