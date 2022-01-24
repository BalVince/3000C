def mindennagyobb10(lista):
    igaze = True
    for elem in lista:
        if elem < 10:
            igaze = False
    return igaze