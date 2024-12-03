class Auto:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def __str__(self):
        return f"{self.marca} {self.modello}"


class Garage:
    def __init__(self):
        self.garage = []

    def aggiungi_valore(self, auto):
        self.garage.append(auto)
        print(f"Auto aggiunta: {auto}")

    def mostra_valori(self):
        if not self.garage:
            print("Il garage è vuoto.")
        else:
            print("Auto nel garage:")
            for i, valore in enumerate(self.garage, start=1):
                print(f"{i}. {valore}")


