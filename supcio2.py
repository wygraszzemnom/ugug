class SklepInternetowy:
  def __init__(self):
      self.produkty = {}
      self.koszyk = []
      self.zalogowany_uzytkownik = None
      self.uzytkownicy = {}

  def dodaj_produkt(self, numer, nazwa, cena, marka):
      if marka not in self.produkty:
          self.produkty[marka] = []
      self.produkty[marka].append({'numer': numer, 'nazwa': nazwa, 'cena': cena})

  def wyswietl_produkty(self):
      for marka, produkty in self.produkty.items():
          print(f"Marka: {marka}")
          for produkt in produkty:
              print(f"  Numer: {produkt['numer']}, Nazwa: {produkt['nazwa']}, Cena: {produkt['cena']}")

  def dodaj_do_koszyka(self, numer_produktu, ilosc):
      for marka, produkty in self.produkty.items():
          for produkt in produkty:
              if produkt['numer'] == numer_produktu:
                  for _ in range(ilosc):
                      self.koszyk.append({'nazwa': produkt['nazwa'], 'cena': produkt['cena'], 'marka': marka})
                  print(f"Dodano do koszyka: {produkt['nazwa']} ({marka}), Cena: {produkt['cena']}, Ilość: {ilosc}")
                  return
      print("Nieprawidłowy numer produktu.")

  def wyswietl_koszyk(self):
      print("Produkty w koszyku:")
      for produkt in self.koszyk:
          print(f"  Nazwa: {produkt['nazwa']}, Cena: {produkt['cena']}, Marka: {produkt['marka']}")

  def podsumowanie_zakupow(self):
      suma = sum(produkt['cena'] for produkt in self.koszyk)
      print(f"\nPodsumowanie zakupów:")
      print(f"Razem do zapłaty: {suma} PLN")

  def zarejestruj_uzytkownika(self, login, haslo):
      if login not in self.uzytkownicy:
          self.uzytkownicy[login] = haslo
          print("Rejestracja udana. Możesz teraz się zalogować.")
      else:
          print("Użytkownik o podanym loginie już istnieje.")

  def zaloguj_uzytkownika(self, login, haslo):
      if login in self.uzytkownicy and self.uzytkownicy[login] == haslo:
          self.zalogowany_uzytkownik = login
          print(f"Zalogowano jako: {login}")
      else:
          print("zalogowano pomyślnie.")

  def dokonaj_platnosci(self, numer_karty, kwota):
      if self.zalogowany_uzytkownik is not None:
          print(f"Płatność za zakupy w kwocie {kwota} PLN dokonana z konta {numer_karty}. Dziękujemy!")
      else:
          print("płatność udana.")

  def zakoncz_zakupy(self):
    # Wyświetlamy zawartość koszyka
    self.wyswietl_koszyk()

    # Podsumowanie zakupów
    self.podsumowanie_zakupow()

    # Użytkownik dokonuje płatności
    while True:
        numer_karty = input("Podaj numer karty kredytowej (maksymalnie 9 cyfr): ")

        # Sprawdzamy, czy numer karty ma maksymalnie 9 cyfr
        if numer_karty.isdigit() and len(numer_karty) <= 9:
            kwota = sum(produkt['cena'] for produkt in self.koszyk)
            self.dokonaj_platnosci(numer_karty, kwota)
            print("Dziękujemy za zakupy!")
            break
        else:
            print("Nieprawidłowy numer karty. Podaj maksymalnie 9 cyfr.")

import random

def gra_z_liczeniem():
    print("Witaj w grze z liczeniem!")
    print("Twoim zadaniem jest dodawanie dwóch liczb.")

    # Generuj dwie losowe liczby
    liczba1 = random.randint(1, 10)
    liczba2 = random.randint(1, 10)

    # Oblicz poprawny wynik
    poprawny_wynik = liczba1 + liczba2

    # Pytaj gracza o odpowiedź
    odpowiedz_gracza = int(input(f"Ile to jest {liczba1} + {liczba2}? "))

    # Sprawdź odpowiedź
    if odpowiedz_gracza == poprawny_wynik:
        print("Brawo! Odpowiedź jest poprawna. Przechodzisz do kolejnego etapu.")
    else:
        print(f"Niestety, odpowiedź nieprawidłowa. Prawidłowy wynik to {poprawny_wynik}. Spróbuj ponownie!")

# Uruchom grę z liczeniem
gra_z_liczeniem()



# Tworzymy instancję sklepu
sklep = SklepInternetowy()

# Dodajemy produkty
sklep.dodaj_produkt(1, 'Jajkofon Pro', 999, 'Jajkofon')
sklep.dodaj_produkt(2, 'Jajko Komputer 2000', 1299, 'Jajko Komputer')
sklep.dodaj_produkt(3, 'JakoTablet X', 499, 'JakoTablet')
sklep.dodaj_produkt(4, 'Zlotejajko', 10000, 'Zlotejajko')
sklep.dodaj_produkt(5, 'Telejajko', 9899, 'Telejajko')
sklep.dodaj_produkt(6, 'aparatjajkograficzny', 499, 'aparatjajkograficzny')
sklep.dodaj_produkt(7, 'Jajkoconsole', 980, 'Jajkoconsole')
sklep.dodaj_produkt(8, 'Jajkoladowarka', 399, 'Jajkoladowarka')
sklep.dodaj_produkt(9, 'odtwarzacz jajek', 900, 'odtwarzacz jajek')
sklep.dodaj_produkt(10, 'dronjaj', 5799, 'dronjaj')
sklep.dodaj_produkt(11, 'drukjaj', 2000, 'drukjaj')
sklep.dodaj_produkt(12, 'smart hom jajko', 800, 'smart hom jajkoj')
sklep.dodaj_produkt(13, 'inteligentne jajko', 800, 'inteligentne jajko')

sklep.dodaj_produkt(14, 'Samsung Galaxy S21', 3299, 'Samsung')
sklep.dodaj_produkt(15, 'Samsung Galaxy Tab S7', 2399, 'Samsung')
sklep.dodaj_produkt(16, 'Samsung Smart TV 55"', 21000, 'Samsung')
sklep.dodaj_produkt(17, 'Samsung Galaxy Watch 4', 899, 'Samsung')
sklep.dodaj_produkt(18, 'Samsung Odyssey G7', 2499, 'Samsung')
sklep.dodaj_produkt(19, 'Samsung Soundbar HW-Q950T', 2999, 'Samsung')
sklep.dodaj_produkt(20, 'Samsung Portable SSD T7', 599, 'Samsung')
sklep.dodaj_produkt(21, 'Samsung Galaxy Tab S8', 6999, 'Samsung')
sklep.dodaj_produkt(22, 'Samsung Galaxy Tab S7+', 3999, 'Samsung')
sklep.dodaj_produkt(23, 'Samsung Galaxy Tab S7 Plus', 3500, 'Samsung')
sklep.dodaj_produkt(24, 'Samsung Galaxy Tab S7 Lite', 5000, 'Samsung')

# Dodajemy produkty Redmi
sklep.dodaj_produkt(24, 'Redmi Note 10 Pro', 1299, 'Redmi')
sklep.dodaj_produkt(25, 'Redmi K40 Pro', 2499, 'Redmi')
sklep.dodaj_produkt(26, 'Redmi 9A', 499, 'Redmi')
sklep.dodaj_produkt(27, 'Redmi Note 9', 899, 'Redmi')
sklep.dodaj_produkt(28, 'Redmi 10X', 1399, 'Redmi')
sklep.dodaj_produkt(29, 'Redmi K30 Ultra', 1899, 'Redmi')
sklep.dodaj_produkt(30, 'Redmi 9 Power', 799, 'Redmi')
sklep.dodaj_produkt(31, 'Redmi Note 8', 699, 'Redmi')
sklep.dodaj_produkt(32, 'Redmi K20 Pro', 1799, 'Redmi')
sklep.dodaj_produkt(33, 'Redmi 9T', 999, 'Redmi')
sklep.dodaj_produkt(34, 'Redmi Note 7', 599, 'Redmi')
sklep.dodaj_produkt(35, 'Redmi K40 Gaming Edition', 2999, 'Redmi')
sklep.dodaj_produkt(36, 'Redmi Note 10S', 1099, 'Redmi')
sklep.dodaj_produkt(37, 'Redmi K30S Ultra', 2099, 'Redmi')
sklep.dodaj_produkt(38, 'Redmi 8', 499, 'Redmi')


# Dodajemy produkty Asus
sklep.dodaj_produkt(39, 'Asus ROG Zephyrus G14', 4999, 'Asus')
sklep.dodaj_produkt(40, 'Asus ZenBook 14', 3499, 'Asus')
sklep.dodaj_produkt(41, 'Asus VivoBook S15', 2499, 'Asus')
sklep.dodaj_produkt(42, 'Asus TUF Gaming A15', 2999, 'Asus')
sklep.dodaj_produkt(43, 'Asus ROG Strix Scar 15', 5999, 'Asus')
sklep.dodaj_produkt(44, 'Asus ZenBook Duo', 4299, 'Asus')
sklep.dodaj_produkt(45, 'Asus VivoBook Flip 14', 1799, 'Asus')
sklep.dodaj_produkt(46, 'Asus ROG Zephyrus G15', 5499, 'Asus')
sklep.dodaj_produkt(47, 'Asus TUF Gaming F15', 2599, 'Asus')
sklep.dodaj_produkt(48, 'Asus ROG Flow Z13', 4799, 'Asus')
sklep.dodaj_produkt(49, 'Asus ZenBook Pro Duo', 6999, 'Asus')
sklep.dodaj_produkt(50, 'Asus VivoBook 15', 1999, 'Asus')
sklep.dodaj_produkt(51, 'Asus ROG Zephyrus Duo', 5799, 'Asus')
sklep.dodaj_produkt(52, 'Asus TUF Gaming FX505', 2199, 'Asus')
sklep.dodaj_produkt(53, 'Asus Chromebook Flip', 1299, 'Asus')

sklep.dodaj_produkt(54, 'Alcatel 1', 399, 'Alcatel')
sklep.dodaj_produkt(55, 'Alcatel 3X', 599, 'Alcatel')
sklep.dodaj_produkt(56, 'Alcatel 1S', 499, 'Alcatel')
sklep.dodaj_produkt(57, 'Alcatel 3L', 349, 'Alcatel')
sklep.dodaj_produkt(58, 'Alcatel 5', 899, 'Alcatel')
sklep.dodaj_produkt(59, 'Alcatel 1X', 299, 'Alcatel')
sklep.dodaj_produkt(60, 'Alcatel 3', 449, 'Alcatel')
sklep.dodaj_produkt(61, 'Alcatel 1B', 199, 'Alcatel')
sklep.dodaj_produkt(62, 'Alcatel 1V', 299, 'Alcatel')
sklep.dodaj_produkt(63, 'Alcatel 1T 10', 499, 'Alcatel')
sklep.dodaj_produkt(64, 'Alcatel 1T 7', 299, 'Alcatel')
sklep.dodaj_produkt(65, 'Alcatel 3T 10', 899, 'Alcatel')
sklep.dodaj_produkt(66, 'Alcatel 1T 7 (2020)', 249, 'Alcatel')
sklep.dodaj_produkt(67, 'Alcatel 1T 10 (2020)', 399, 'Alcatel')
sklep.dodaj_produkt(68, 'Alcatel 3T 8', 599, 'Alcatel')

# Dodajemy 15 różnych produktów marki Huawei
sklep.dodaj_produkt(69, 'Huawei P30 Pro', 2499, 'Huawei')
sklep.dodaj_produkt(70, 'Huawei Mate 20 Lite', 1299, 'Huawei')
sklep.dodaj_produkt(71, 'Huawei P40', 2999, 'Huawei')
sklep.dodaj_produkt(72, 'Huawei Nova 5T', 1699, 'Huawei')
sklep.dodaj_produkt(73, 'Huawei P Smart', 899, 'Huawei')
sklep.dodaj_produkt(74, 'Huawei Y6p', 599, 'Huawei')
sklep.dodaj_produkt(75, 'Huawei Mate X', 8999, 'Huawei')
sklep.dodaj_produkt(76, 'Huawei P20 Pro', 1999, 'Huawei')
sklep.dodaj_produkt(77, 'Huawei Nova 7i', 1499, 'Huawei')
sklep.dodaj_produkt(78, 'Huawei P Smart Z', 999, 'Huawei')
sklep.dodaj_produkt(79, 'Huawei Y9 Prime', 1299, 'Huawei')
sklep.dodaj_produkt(80, 'Huawei Mate 30 Pro', 3599, 'Huawei')
sklep.dodaj_produkt(81, 'Huawei P50', 3999, 'Huawei')
sklep.dodaj_produkt(82, 'Huawei Enjoy 20', 899, 'Huawei')
sklep.dodaj_produkt(83, 'Huawei FreeBuds Pro', 699, 'Huawei')
sklep.dodaj_produkt(84, 'Huawei Watch GT 2', 899, 'Huawei')



# Rejestracja lub logowanie
akcja = int(input("Wybierz akcję (1 - logowanie, 2 - rejestracja): "))
if akcja == 1:
  login = input("Podaj login: ")
  haslo = input("Podaj hasło: ")
  sklep.zaloguj_uzytkownika(login, haslo)
elif akcja == 2:
  login = input("Podaj nowy login: ")
  haslo = input("Podaj nowe hasło: ")
  sklep.zarejestruj_uzytkownika(login, haslo)
else:
  print("Nieprawidłowa akcja.")

# Dodajemy produkty
# ... (reszta kodu bez zmian)

# Wyświetlamy produkty
sklep.wyswietl_produkty()

# Użytkownik wybiera produkty do koszyka
while True:
  numer_produktu = int(input("Wybierz numer produktu do dodania do koszyka (0 aby zakończyć): "))
  if numer_produktu == 0:
      break
  ilosc_produktu = int(input("Podaj ilość produktu do dodania do koszyka: "))
  sklep.dodaj_do_koszyka(numer_produktu, ilosc_produktu)

# Zakończenie zakupów (wyświetlenie koszyka, podsumowanie i płatność)
sklep.zakoncz_zakupy()


