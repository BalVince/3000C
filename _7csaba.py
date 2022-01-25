def tizenotosztfele(lista):
    listaasd = []
    for elem in lista:
        if elem % 15 == 0:
            listaasd.append(elem/2)
    return listaasd