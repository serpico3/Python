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
        Exception(print("Errore: per favore inserisci un numero positivo."))
    else:
        while n >= 0:
            print(n)
            n -= 1

def verificaListaOrdinata(lista):
    try:
        lista = [int(i) for i in lista]
    except ValueError:
        print("Errore: per favore inserisci solo numeri.")
    if lista == sorted(lista):
        print("La lista è ordinata.")
    else:
        print("La lista non è ordinata.")

def calcolatrice():
    while True:
        operazione = input("Quale operazione vuoi eseguire? (+, -, *, /) ")
        if operazione == "fine":
            break
        if operazione not in ["+", "-", "*", "/"]:
            print("Errore: per favore inserisci un'operazione valida.")
            continue
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
        except ValueError:
            print("Errore: per favore inserisci un numero valido.")
            continue
        if operazione == "+":
            print(a + b)
        elif operazione == "-":
            print(a - b)
        elif operazione == "*":
            print(a * b)
        elif operazione == "/":
            if b == 0:
                print("Errore: divisione per zero.")
            else:
                print(a / b)
        else:
            print("Errore: per favore inserisci un'operazione valida.")

def gioco():
    numero = random()
    while True:
        try:
            guess = int(input("Indovina il numero: "))
        except ValueError:
            print("Errore: per favore inserisci un numero valido.")
            continue
        if guess == numero:
            print("Hai indovinato!")
            break
        elif guess < numero:
            print("Troppo basso.")
        elif guess > numero:
            print("Troppo alto.")

def listaSpesa():
    lista = []
    while True:
        comando = input("Vuoi aggiungere un prodotto o visualizzare la lista? ")
        if comando == "fine":
            break
        elif comando == "aggiungi":
            prodotto = input("Inserisci il prodotto: ")
            quantita = input("Inserisci la quantità: ")
            lista.append((prodotto, quantita))
        elif comando == "visualizza":
            for prodotto, quantita in lista:
                print(prodotto, quantita)
        else:
            print("Errore: per favore inserisci un comando valido.")