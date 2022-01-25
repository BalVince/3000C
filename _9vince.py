# 9. Van-e a sorozatban olyan negatív szám, amelyet pozitív követ?!

def kilenc(lista):
    for i,e in enumerate(lista):
        if lista[i-1] < 0 and 0 <= lista[i]:
            return True
    return False