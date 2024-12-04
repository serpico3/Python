import gestore_auto

garage = gestore_auto.Garage()

while True:

    print("\nInserisci i dettagli di un'auto (oppure digita 'stop' per terminare):")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    chilometri = int(input("Chilometri: "))
    var = input("Modello? (Auto/Moto): ")
    

    if var == "Auto":
        porte = int(input("Porte: "))
        autoPorte = gestore_auto.Veicolo(marca, modello, anno, chilometri, porte)
        garage.aggiungi_valore(autoPorte)
        gestore_auto.Auto.guidareVeicolo(autoPorte)
    elif var == "Moto":
        cilindrata = int(input("Cilindrata: "))
        autoCilindrata = gestore_auto.Moto(marca, modello, anno, chilometri, cilindrata)
        garage.aggiungi_valore(autoCilindrata)
        gestore_auto.Auto.guidareVeicolo()
    else:
        print("veicolo non esistente")

    print("\nLe auto nel garage sono:")
    garage.mostra_valori()