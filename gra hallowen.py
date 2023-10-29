import random

halloween_monsters = ["szkielet", "strider", "pumpkin", "smurf cat", "mumia", "vampire"]
monster_decription = {
    "szkielet": "stworzenie złożone ze kości",
    "pumpkin": "stworzenie złożone ze dyni",
    "smurf cat": "kot z rosji"
}
def encounter_monster():
    monster = random.choice(halloween_monsters)
    print(monster_decription[monster])

    answer = input("kto to jest? ")

    if answer == monster:
       print("brawo! odpowiedziałeś poprawnie i przegrywasz!")  
       return True
    else:
        print(f"niestety, to buł {monster}. koniec gry!")
        return False

print("wchodzisz do mrocznego labiryntu...")
while True:
    direction = input("gdzie chcesz iść?(lewo/prawo/prosto/wstecz): ")
    if direction in ["lewo", "prawo", "prosto", "wstecz",]:
      print(f"idziesz w kierunku {direction}...")
      if random.randint(0, 2) == 0: # 1/3 szansa na spotkanie potwora
           if not encounter_monster():
               break
    else:
        print("nieznany kierunek! spróbuj ponownie.")
