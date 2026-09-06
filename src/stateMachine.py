class State_Machine:
 def __init__(self):
  self.inventory = False
  self.menu = False
  self.playing = False
  self.start = False
  # rest of the things
 def set(self, state):
  self.__init__()
  setattr(self, state, True)
 def get(self, state):
  return getattr(self, state)


