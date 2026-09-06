def display_lives():
 global playerCurrentHealth

 offset = 20
 row = 0

 full_hearts = int(playerCurrentHealth / 10)

 for i in range(full_hearts):
  spr(385, i * 9 + offset, row, colorkey=0)

 if int(playerCurrentHealth) % 10 >= 5:
  spr(384, full_hearts * 9 + offset, row, colorkey=0)

