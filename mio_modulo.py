def saluta():
    print("Ciao Mondo")

def sommaedifferenza(a,b):
    somma = a + b
    differenza = a - b
    print("La somma è", somma)
    print("La differenza è", differenza)

def tabellina(n):
    for i in range(1,10):
        print(n, "x", i, "=", n*i)

def rettangolo(a,b):
    print("Il perimetro del rettangolo è", 2*a + 2*b)
    print("L'area del rettangolo è", a*b)

def random():
    import random
    return random.randint(0, 100)

def riepilogo(lista):
    if not lista:
        return None
    min_val = lista[0]
    for num in lista:
        if num < min_val:
            min_val = num
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    media = sum(lista) / len(lista)
    print("La media è", media, "Il minimo è", min_val, "Il massimo è", max_val)

def solopositivoERovescio(n):
    if n <= 0:
        Exception("Il numero deve essere positivo")
    else:
        while n >= 0:
            print(n)
            n -= 1