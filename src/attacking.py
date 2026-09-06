#attacking function
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


