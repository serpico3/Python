class lavoratore():
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
    def __str__(self):
        return f"{self.nome} {self.cognome} {self.stipendio}"
    
class programmatore(lavoratore):
    def __init__(self, nome, cognome, stipendio, linguaggio):
        super().__init__(nome, cognome, stipendio)
        self.linguaggio = []

class manager(lavoratore):
    def __init__(self, nome, cognome, stipendio, team):
        super().__init__(nome, cognome, stipendio)
        self.team = team
    
    def __str__(self):
        return f"{self.nome} {self.cognome} {self.stipendio} {self.team}"
        
class Azienda():
    def __init__(self):
        self.dipendenti = []

    def __str__(self):
        return f"{self.dipendenti}"
    def aggiungi_dipendente(self, dipendente):
        self.dipendenti.append(dipendente)
    
    def calcola_stipendio(self):
        for dipendente in self.dipendenti:
            print(dipendente.stipendio)

    def mostra_azienda(self):
        for dipendente in self.dipendenti:
            print(dipendente)