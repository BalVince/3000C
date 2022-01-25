def van_e_pozitiv(lista):
    i = 0
    while i<len(lista) and lista[i] <= 0:
        i += 1
    if i > lista[i]:
        return False
    else:
        return True
#kesz