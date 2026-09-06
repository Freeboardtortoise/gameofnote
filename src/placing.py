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

