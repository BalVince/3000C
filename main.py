# print("Hello world!")

import _1fodor, _2fodor, _3fodor, _4csaba, _5csaba, _6csaba, _7csaba, _8vince, _9vince, _10vince

"""
3.000-C
Olvassuk be az alábbi fájl tartalmmát egy listába/tömbbe,
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát!
1. Van-e a sorozatban 100-zal osztható szám?
2. Írjuk ki az utolsó 7-tel osztható szám indexét!
3. Írjuk ki az első 19-cel osztható szám indexét!
4. Mennyi a sorozatban található számok átlagának a négyzete?
5. Igaz-e, hogy minden szám nagyobb, mint 10?
6. Hány 9-cel osztható szám található a sorozatban?
7. Írjuk ki a sorozatban található 15-tel osztható számok felét!
8. Hány eleme van a sorozatnak?
9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?
10. Mennyi a sorozatban található legkisebb szám fele?
"""

lista = []
with open("3000C_input.txt", "r", encoding="utf8") as f:
    for sor in f:
        lista.append(sor)

# 1. feladat
print("1. Van-e a sorozatban pozitív szám?\n")


# 2. feladat
print("2. Hány eleme van a sorozatnak? \n")


# 3. feladat
print("3. Mennyi a sorozatban található legkisebb szám?\n")


# 4. feladat
print("4. Írjuk ki az első 33-mal osztható szám indexét!\n")


# 5. feladat
print("5. Mennyi a sorozatban található számok átlagának a fele?\n")


# 6. feladat
print("6. Igaz-e, hogy minden szám pozitív?\n")


# 7. feladat
print("7. Hány páratlan szám található a sorozatban?\n")


# 8. feladat
print("8. Van-e a sorozatban olyan negatív szám, amelyet újabb negatív követ?\n")
_8vince.nyolc(lista)

# 9. feladat
print("9. Írjuk ki az utolsó 19-cel osztható szám indexét!\n")


# 10. feladat
print("10. Írjuk ki a sorozatban található 5-tel osztható számokat!\n")


