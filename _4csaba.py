def atlag_negyzet(lista):    
    sum = 0
    for elem in lista:
        sum += elem
    sum = sum / len(lista)
    return(round(sum**2, 2))
