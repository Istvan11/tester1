dozwolone_waluty = ("PLN", "EUR", "USD")
#waluta = input("Podaj walutę:")
#if waluta in dozwolone_waluty:
#   print("Poprawna waluta")
#else:
#   print(f"Nieznany kod waluty, podano:{waluta}")  #najprostrza metoda
#   print("Nieznany kod waluty, podano: %S" % waluta)   #stara metoda, można spotkać

#małe f = .format podany na końcuprint(f"Nieznany kod waluty, podano:{waluta}")
#print("Nieznany kod waluty, podano: {}".format(waluta))

# NIE SORTUJEMY LISTY, KTÓRA MA RÓŻNE ELEMENTY
lista = []

lista.append("Tomek")
lista.append("KAziu")
lista.append("Małgoś")
lista.insert(1, "Zuza")
lista.append(dozwolone_waluty)
#lista.pop() z automatu usuwa ostatni element, można indeksować ale mało ię uzywa tego
#lista.remove("zuza") usuwa wybrany element
#lista.clear() czyścu całą tablice
#lista[0] = "Tomek" zamieniasz indeks na nowy, podmiana

#lista.sort() ortuje np alfabetycznie
#lita.reverse() sortujesz od drugiej strony
# zmienna=lista[1:4]
# ostatni=lista[-1][0]

print(lista)
# print(zmienna)
# print(ostatni)