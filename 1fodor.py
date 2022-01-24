def van_e_pozitiv(lista):
    i = 0
    while lista[i] <= 0:
        i += 1
    if i > lista[i]:
        return "nincs"
    else:
        return "van"