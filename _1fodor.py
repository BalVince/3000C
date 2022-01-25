def van_e_100zal_oszthato(lista):
    i = 0
    while i < len(lista) and lista[i] % 100 != 0:
        i += 1
    if i > lista[i]:
        return False
    else:
        return True
#kesz