import random
from random import randint
import time
import pdb
def fion(v):
  return 'x' if v is None else (v.x,v.y) 
class Game ():
  def __init__(self):
    self.world = World(4,4)
    self.player = Player(self.world)
    self.Command()
  def Command (self):
    while True:
      print('com: go, quit, map, look')
      i = input('-->')
      if i == 'quit':
        break
      elif i == 'go':
        self.player.Go()
      elif i == 'look':
        print("В этой локации:")
        for i in self.player.room.inr:
          print(i.info)
        print()
        print("Локация:",self.player.room.info)
        print()
      elif i == 'map':
        for l in self.world.RM:
          for i in l:
            if i.inr.count(self.player) > 0:
              print('[Я]',end="")
            else:
              print('[_]', end="")
          print()
      else:
        print('Ошибка!')
class World ():
  def __init__(self,w,h):
    self.WH = h
    self.WW = w
    self.WS = self.WH * self.WW
    self.RM = []
    self.NewMatric()
  def __str__(self):
    s = "World w={} h={}\n".format(self.WH,self.WW)
    for j in range(self.WH):
      for i in range(self.WW):
        s += str(self.RM[j][i])+" "
      s+="\n"
    return s
  def NewMatric (self):
    for j in range(self.WH):
      self.RM.append([])
      for i in range(self.WW):
        if i + j == 0:
          self.RM[j].append(Anthill(j,i))
        else:
          self.RM[j].append(Room(j,i))
    for j in range(1,self.WH-1):
        for i in range(1,self.WW-1):
          r = self.RM[j][i] 
          r.east = self.RM[j][i+1]
          r.west = self.RM[j][i-1]
          r.north = self.RM[j-1][i]
          r.south = self.RM[j+1][i]
    for j in range(1,self.WH-1):
      r = self.RM[j]
      r[0].north = self.RM[j-1][0]
      r[0].south = self.RM[j+1][0]
      r[0].east = self.RM[j][1]
      r[self.WW-1].west = self.RM[j][self.WW-2]
      r[self.WW-1].north = self.RM[j-1][self.WW-1]
      r[self.WW-1].south = self.RM[j+1][self.WW-1]
    for i in range(1,self.WW-1):
      r = self.RM[0]
      r[i].west = r[i-1]
      r[i].east = r[i+1]
      r[i].south = self.RM[1][i]
      r = self.RM[self.WH-1]
      r[i].west = r[i-1]
      r[i].east = r[i+1]
      r[i].north = self.RM[self.WH-2][i]
    self.RM[-1][0].north = self.RM[-2][0]
    self.RM[-1][-1].north = self.RM[-2][-1]
    self.RM[0][-1].west = self.RM[0][-2]
    self.RM[-1][-1].west = self.RM[-1][-2]
    self.RM[-1][0].east = self.RM[-1][1]
    self.RM[0][0].east = self.RM[0][1]
    self.RM[0][-1].south = self.RM[1][-1]
    self.RM[0][0].south = self.RM[1][0]
class Room ():
  info = "Стартовая"
  def __init__ (self,y,x):
    self.north = None
    self.south = None
    self.west = None
    self.east = None
    self.inr = []
    self.x = x
    self.y = y
  def add(self,st):
    self.inr.append(st)
  def __str__(self):
    s = "({},{}):{}{}{}{}".format(
        self.x,self.y,
        fion(self.north),
        fion(self.south),
        fion(self.west),
        fion(self.east) 
        )
    return s
class Anthill(Room):
  info = "Муравейник"
  def __init__(self,y,x):
    super().__init__(y,x)
class Bug ():
  info = "Насекомое"
  def __init__ (self,w):
    self.world = w
    self.room = self.world.RM[2][2]
class Player (Bug):
  info = "Муравей(игрок)"
  def __init__(self,w):
    super().__init__(w)
    self.room.inr.append(self)
  def Go (self):
    while True:
      r0 = self.room
      i = input('>->-> ')
      if i == 'n' and self.room.north != None:
        self.room.inr.remove(self)
        self.room = self.room.north
        self.room.inr.append(self)
      if i == 's' and self.room.south != None:
        self.room.inr.remove(self)
        self.room = self.room.south
        self.room.inr.append(self)
      if i == 'w' and self.room.west != None:
        self.room.inr.remove(self)
        self.room = self.room.west
        self.room.inr.append(self)
      if i == 'e' and self.room.east != None:
        self.room.inr.remove(self)
        self.room = self.room.east
        self.room.inr.append(self)
      if i == "com":
        break
      if r0 != self.room:
        print("{}".format(self.room.info))
      else:
        print("Вы не можете ползти туда")
if __name__ == "__main__":
  g = Game()
