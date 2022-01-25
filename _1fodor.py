from ast import Return


def van_e_100zal_oszthato(lista):
    i = 0
    while i < len(lista) and lista[i] % 100 != 0:
        i += 1
    return i > lista[i]
#kesz