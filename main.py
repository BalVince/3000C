# print("Hello world!")

from keyword import kwlist
import _1fodor, _2fodor, _3fodor, _4csaba, _5csaba, _6csaba, _7csaba, _8vince, _9vince, _10csaba

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
        lista.append(int(sor))

# 1. feladat
print("1. Van-e a sorozatban 100-zal osztható szám?")
print(_1fodor.van_e_100zal_oszthato(lista), "\n")

# 2. feladat
print("2. Írjuk ki az utolsó 7-tel osztható szám indexét!")
print(_2fodor.hany_eleme_van(lista),"\n")

# 3. feladat
print("3. Írjuk ki az első 19-cel osztható szám indexét!")
print(_3fodor.legkisebb_szam(lista), "\n")

# 4. feladat
print("4. Mennyi a sorozatban található számok átlagának a négyzete?")
print(_4csaba.atlag_negyzet(lista),"\n")

# 5. feladat
print("5. Igaz-e, hogy minden szám nagyobb, mint 10?")
print(_5csaba.mindennagyobb10(lista),"\n")

# 6. feladat
print("6. Hány 9-cel osztható szám található a sorozatban?")
print(_6csaba.kilencceloszthato(lista),"\n")

# 7. feladat
print("7. Írjuk ki a sorozatban található 15-tel osztható számok felét!")
print(_7csaba.tizenotosztfele(lista),"\n")

# 8. feladat
print("8. Hány eleme van a sorozatnak?")
print(_8vince.nyolc(lista),"\n")

# 9. feladat
print("9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?")
print(_9vince.kilenc(lista),"\n")

# 10. feladat
print("10. Mennyi a sorozatban található legkisebb szám fele?")
print(_10csaba.legkisfele(lista),"\n")

