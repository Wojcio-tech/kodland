import random

klucze = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugosc = int(input("Podaj długość hasła: "))
haslo = ""

for i in range(dlugosc):
    haslo += random.choice(klucze)

print("Twoje wygenerowane hasło to:", haslo)

