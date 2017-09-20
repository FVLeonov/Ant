import random
from random import randint
import time
def fion(v):
  return 'x' if v is None else (v.x,v.y) 
class Game ():
  def __init__(self):
    self.anth = Anthill()
    self.world = World(4,4)
    self.player = Player(self.world)
    self.Command()
  def Command (self):
    while True:
      i = input('-->')
      if i == 'quit':
        break
      elif i == 'go':
        self.player.Go()
      elif i == 'look':
        self.player.room.biom.desc
class World ():
  def __init__(self,w,h):
    self.WH = h
    self.WW = w
    self.WS = self.WH * self.WW
    self.RM = []
    self.RB = [Grass(),Dirt()]
    self.NewMatric()
    AddSomeThing()
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
        if i != WW//2 or j != WH//2:
          self.RM[j].append(Room(j,i))
        else:
          pass
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
  def AddSomeThing():
    for i in range(5):
      a = randint(0,WW-1)
      b = randint(0,WH-1)
      c = randint(0,5)
      th = weightedChoice(self.Things)
      th(self.RM[a][b],c)
class Room ():
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
  def __init__ (self):
    super().__init__(World.WH//2,World.WW//2)
class Player ():
  def __init__(self,w,a):
    self.anth = a
    self.world = w 
    self.room = self.anth
    self.room.inr.append(self)
  def Go (self):
    while True:
      i = input('>->-> ')
      if i == 'n':
        if self.room.north != None:
          self.room.inr.remove(self)
          self.room = self.room.north
          self.room.inr.append(self)
          print("Координаты x{},y{}".format(self.room.x,self.room.y))
          if self.room == Anthill:
            print("Вы в муравейнике")
        else:
          print("Вы не можете ползти туда")
      if i == 's':
        if self.room.south != None:
          self.room.inr.remove(self)
          self.room = self.room.south
          self.room.inr.append(self)
          print("Координаты x{},y{}".format(self.room.x,self.room.y))
          if self.room == Anthill:
            print("Вы в муравейнике")
        else:
          print("Вы не можете ползти туда")
      if i == 'w':
        if self.room.west != None:
          self.room.inr.remove(self)
          self.room = self.room.west
          self.room.inr.append(self)
          print("Кординаты x{},y{}".format(self.room.x,self.room.y))
          if self.room == Anthill:
            print("Вы в муравейнике")
        else:
          print("Вы не можете ползти туда")
      if i == 'e':
        if self.room.east != None:
          self.room.inr.remove(self)
          self.room = self.room.east
          self.room.inr.append(self)
          print("Координаты x{},y{}".format(self.room.x,self.room.y))
          if self.room == Anthill:
            print("Вы в муравейнике")
        else:
          print("Вы не можете ползти туда")
      if i == 'com':
        break
if __name__ == "__main__":
  g = Game()
