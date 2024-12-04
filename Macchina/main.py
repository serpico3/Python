import gestore_auto

garage = gestore_auto.Garage()

while True:
    print("\nInserisci i dettagli di un'auto (oppure digita 'stop' per terminare):")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = input("Anno: ")
    chilometri = input("Chilometri: ")
    var = input("Modello? (Auto/Moto): ")
    

    if var == "Auto":
        porte = input("Porte: ")
        autoPorte = gestore_auto.Veicolo(marca, modello, anno, chilometri, porte)
        garage.aggiungi_valore(autoPorte)
    elif var == "Moto":
        cilindrata = input("Cilindrata: ")
        autoCilindrata = gestore_auto.Moto(marca, modello, anno, chilometri, cilindrata)
        garage.aggiungi_valore(autoCilindrata)
    else:
        print("veicolo non esistente")

    print("\nLe auto nel garage sono:")
    garage.mostra_valori()