class Auto:
    def __init__(self, marca, modello, anno, chilometri):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.chilometri = chilometri

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} {self.chilometri}"
    
class Moto(Auto):
    def __init__(self, marca, modello, anno, chilometri, cilindrata):
        super().__init__(marca, modello, anno, chilometri)
        self.cilindrata = cilindrata

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} {self.chilometri} {self.cilindrata}"
    
class Veicolo(Auto):
    def __init__(self, marca, modello, anno, chilometri, porte):
        super().__init__(marca, modello, anno, chilometri)
        self.porte = porte

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} {self.chilometri} {self.porte}"


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


