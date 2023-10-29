import random

nasza_druzyna = list(range(1, 11))  # Nasza drużyna składa się z numerów od 1 do 10
druzyna_wroga = list(range(11, 21))  # Drużyna wroga składa się z numerów od 11 do 20

def trafienie_sukces():
    return random.random() < 0.5  # Trafienie z prawdopodobieństwem 50%

while nasza_druzyna and druzyna_wroga:
    nasz_numer = int(input("Podaj numer żołnierza z naszej drużyny: "))
    if nasz_numer in nasza_druzyna:
        if trafienie_sukces():
            nasza_druzyna.remove(nasz_numer)
            print(f"Twój żołnierz o numerze {nasz_numer} trafił wroga!")
        else:
            print(f"Twój żołnierz o numerze {nasz_numer} spudłował.")
    else:
        print("Błąd! Taki numer nie istnieje w naszej drużynie.")
        continue

    komputer_numer = random.choice(druzyna_wroga)
    druzyna_wroga.remove(komputer_numer)
    print(f"Wrogi żołnierz o numerze {komputer_numer} zaatakował!")

    print(f"Nasza drużyna: {nasza_druzyna}")
    print(f"Drużyna wroga: {druzyna_wroga}")

if not nasza_druzyna:
    print("Wrogowie wygrali! Nasza drużyna została pokonana.")
else:
    print("Gratulacje! Wygraliśmy wojnę. Drużyna wroga została pokonana.")
