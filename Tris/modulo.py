# calcolatrice_modulo.py

class Calcolatrice:
    def __init__(self):
        self.operazione = ""

    def aggiungi(self, valore):
        """Aggiunge un valore all'operazione."""
        self.operazione += str(valore)

    def calcola(self):
        """Esegue il calcolo dell'operazione corrente."""
        try:
            risultato = eval(self.operazione)  # Esegue l'operazione
            self.operazione = str(risultato)
        except Exception:
            self.operazione = "Errore"

    def reset(self):
        """Cancella l'operazione corrente."""
        self.operazione = ""
