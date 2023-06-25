menu = """
    ************
    *   menu   *
    ************
"""
print(menu)



imie = input("podaj imię: ").lower()
rok = input("podaj rok: ")
# print(type(imie))
# print(type(rok))

lata=(rok,imie)
print(type(lata))


if int(rok)<2020:
    print("to jest rok przed 2020...")
elif int(rok) > 2023:
    print("to jest data przyszła")
    if imie == "Tomek":
        print("to jest Tomek z przyzłości")
else:
    print("to jest data pomiędzy 2020-2023")

print("zawartość krotki:",lata)

#print(imie.startswith("T"))
#print(lata[1])