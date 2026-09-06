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

def reverse(dictionary):
    return {value: key for key, value in dictionary.items()}




ATTACKING_SPEED = 10
attacking_timer = ATTACKING_SPEED

generate_world(random.randint(0,1000))
test = Mob(Vector2(0,0), 100, 0.5, 0.5, True, 277, 2, 100, True, 10)
mobs = []

def DeathScreen():
 cls(0)
 print(str("You are dead"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2), color=15, fixed=False, scale=3)
 print(str("Yes you read that correctly"), x=int(SCREEN_SIZE[0]/2), y=int(SCREEN_SIZE[1]/2)+20, color=15, fixed=False, scale=1)
 time.sleep(10)
 exit()


state = State_Machine()
state.set("start")

shader_object = Shader(4)
def TIC():
 global t
 global pos
 global invent, inventmen, cBlock, walkable_blocks
 global inventory, inventoryLayout, inventbtnPresses
 global counter
 global buttonDown, buttonUp, buttonRight, buttonLeft
 global mobs
 global state
 global shader_object
 shader_object.calculate(pos)
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

  map(int((cam.x/speed)/8), int((cam.y/speed)/8), sx=-(cam.x%8), sy=-(cam.y%8), remap=shader_object.shader)
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
