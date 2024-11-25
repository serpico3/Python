import random

# Vecchio codice
"""
piuDiMax = 0

for i in range(0, 1000):
    disponibilita = 10000
    puntato = 1
    count = 0
    max = disponibilita
    while puntato < disponibilita:
        numero = random.randint(0, 1)
        if numero == 0:
            disponibilita -= puntato
            puntato = puntato * 2
            
        else:
            disponibilita -= puntato
            disponibilita += puntato * 2
            puntato = 1

        count += 1
        if disponibilita > max:
            max = disponibilita
    
    if max > 10500:
        piuDiMax += 1

print(piuDiMax)
"""

perdite_totali = 0
guadagni_totali = 0
piuDiMax = 0

for i in range(0, 100):
    disponibilita = 10000
    puntato = disponibilita / 100
    sconfitte = 0
    max = disponibilita
    puntate_perse= 0
    for i in range(0, 100):
        numero = random.randint(0, 1)
        if numero == 0:
            disponibilita -= puntato
            sconfitte += 1
            perdite_totali += puntato  # Aggiungi la puntata persa alle perdite
        else:
            disponibilita -= puntato
            disponibilita += puntato * 2
            guadagni_totali += puntato * 2  # Guadagni dalla vittoria (la puntata moltiplicata per 2)

        if disponibilita > max:
            max = disponibilita

        if puntato <= 100:
            puntate_perse += 1
    
    if max > 10500:
        piuDiMax += 1

print("Perdite totali:", perdite_totali)
print("Guadagni totali:", guadagni_totali)
print("Numero di volte che la disponibilità ha superato i 10500:", piuDiMax)
print("Puntate perse:", puntate_perse)