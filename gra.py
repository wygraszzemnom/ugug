import random
monsters = {"zoombie" : {"hp": 100, "attack": 40}, "szkielet" : {"hp": 50 , "attack": 20}, "nekromamta" : {"hp": 1000 , "attack": 200}, "szczur" : {"hp": 100 , "attack": 10}, "pumpkin" : {"hp": 450 , "attack": 2000}, "boss" : {"hp": 25000 , "attack": 150},
"smok endu" : {"hp": 5000 , "attack": 500}}


def chooseMonsters():
  monster1 = random.choice(list(monsters.keys()))
  monster2 = random.choice(list(monsters.keys()))
  return [monster1, monster2]

def attack(monster1, monster2):
  monsters[monster2]['hp'] -= monsters[monster1]['attack']
  print(f"{monster1} atakuje za {monsters[monster1]['attack']} ")
  print(f"{monster2} ma {monsters[monster2]['hp']} ")

def checkWin(monster1, monster2):
  if monsters[monster1]['hp'] <= 0:     
     print(f"{monster1} został zniszczony!")     
     return True
  elif monsters[monster1]['hp'] <= 0:     
     print(f"{monster1} został zniszczony!")     
     return True
  return False

def game(): 
  print("_______________Walka Trwa_______________")
  monsters = chooseMonsters()
  while True:
    attack(monsters[0], monsters[1])
    if checkWin(monsters[0], monsters[1]):
      break
    attack(monsters[1], monsters[0])
    if checkWin(monsters[1], monsters[0]):
      break
game()






