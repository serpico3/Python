import gestore_auto

garage = gestore_auto.Garage()

while True:
    print("\nInserisci i dettagli di un'auto (oppure digita 'stop' per terminare):")
    marca = input("Marca: ")
    if marca.lower() == 'stop':
        break
    modello = input("Modello: ")

    # Creazione dell'oggetto Auto e aggiunta al garage
    auto = gestore_auto.Auto(marca, modello)
    garage.aggiungi_valore(auto)

    # Mostra il contenuto del garage
    print("\nLe auto nel garage sono:")
    garage.mostra_valori()