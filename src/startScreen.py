tempCam = Vector2(0,0)
def start():
 global state
 global tempCam
 cam = tempCam
 speed = 2
 cls(15)
 map(int((cam.x/speed)/8), int((cam.y/speed)/8), sx=-(int(cam.x/speed)%8), sy=-(int(cam.y/speed)%8))
 spr(224, 10,10, colorkey=0, w=11,h=2, scale=2)
 print("Press A to start", 100,100,color=12)
 if btn(4) == True:
  state.set("playing")
 tempCam += Vector2(1, 1)

