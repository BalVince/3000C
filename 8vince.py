# 8. Van-e a sorozatban olyan negatív szám, amelyet újabb negatív követ?

from main import lista

def nyolc():
    for i,e in enumerate(lista[1:]):
        if lista[i-1] < 0 and lista[i] < 0:
            return True
    return False
    