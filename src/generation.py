
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

