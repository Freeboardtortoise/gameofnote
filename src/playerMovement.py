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


