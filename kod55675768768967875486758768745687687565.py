class SklepInternetowy:
  def __init__(self):
      self.produkty = {}
      self.koszyk = []

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

# Wyświetlamy produkty
sklep.wyswietl_produkty()

# Użytkownik wybiera produkty do koszyka
while True:
  numer_produktu = int(input("Wybierz numer produktu do dodania do koszyka (0 aby zakończyć): "))
  if numer_produktu == 0:
      break
  ilosc_produktu = int(input("Podaj ilość produktu do dodania do koszyka: "))
  sklep.dodaj_do_koszyka(numer_produktu, ilosc_produktu)

# Wyświetlamy zawartość koszyka
sklep.wyswietl_koszyk()

# Podsumowanie zakupów
sklep.podsumowanie_zakupow()
