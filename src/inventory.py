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

