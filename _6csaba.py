def kilencceloszthato(lista):
    kilenceloszt = 0
    for elem in lista:
        if elem % 9 == 0:
            kilenceloszt += 1
    return kilenceloszt