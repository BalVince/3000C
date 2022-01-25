def legkisebb_szam(lista):
    legk = lista[0]
    for elem in lista:
        if elem < legk:
            legk = elem
    return legk
#kesz