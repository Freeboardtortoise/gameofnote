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

