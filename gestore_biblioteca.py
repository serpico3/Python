import json
import os

class Biblioteca:
    def __init__(self, file_biblioteca):
        self.file_biblioteca = file_biblioteca
        self.biblioteca = self.carica_biblioteca()

    def carica_biblioteca(self):
        """Carica i dati della biblioteca dal file JSON"""
        if os.path.exists(self.file_biblioteca):
            with open(self.file_biblioteca, 'r') as file:
                return json.load(file)
        else:
            return {}

    def salva_biblioteca(self):
        """Salva i dati della biblioteca nel file JSON"""
        with open(self.file_biblioteca, 'w') as file:
            json.dump(self.biblioteca, file, indent=4)

    def aggiungi_libro(self, titolo, autore, pagine):
        """Aggiungi un libro alla biblioteca"""
        if titolo in self.biblioteca:
            print(f"Il libro '{titolo}' è già presente nella biblioteca.")
        else:
            self.biblioteca[titolo] = {
                'autore': autore,
                'pagine': pagine,
                'prestato': False
            }
            print(f"Libro '{titolo}' aggiunto alla biblioteca.")
            self.salva_biblioteca()

    def mostra_libri(self):
        """Visualizza i libri nella biblioteca"""
        if not self.biblioteca:
            print("La biblioteca è vuota.")
        else:
            print("Libri nella biblioteca:")
            for titolo, info in self.biblioteca.items():
                stato = "Disponibile" if not info['prestato'] else "Prestato"
                print(f"{titolo} di {info['autore']}, {info['pagine']} pagine - {stato}")

    def remove_libro(self, titolo):
        """Rimuove un libro dalla biblioteca"""
        if titolo in self.biblioteca:
            del self.biblioteca[titolo]
            print(f"Libro '{titolo}' rimosso dalla biblioteca.")
            self.salva_biblioteca()
        else:
            print(f"Libro '{titolo}' non trovato nella biblioteca.")

    def prestito_libro(self, titolo):
        """Segna un libro come prestato"""
        if titolo in self.biblioteca:
            if self.biblioteca[titolo]['prestato']:
                print(f"Il libro '{titolo}' è già prestato.")
            else:
                self.biblioteca[titolo]['prestato'] = True
                print(f"Libro '{titolo}' prestato.")
                self.salva_biblioteca()
        else:
            print(f"Libro '{titolo}' non trovato nella biblioteca.")

    def ritiro_libro(self, titolo):
        """Segna un libro come ritirato (restituito)"""
        if titolo in self.biblioteca:
            if not self.biblioteca[titolo]['prestato']:
                print(f"Il libro '{titolo}' non è stato prestato, quindi non può essere ritirato.")
            else:
                self.biblioteca[titolo]['prestato'] = False
                print(f"Libro '{titolo}' ritirato e ora disponibile.")
                self.salva_biblioteca()
        else:
            print(f"Libro '{titolo}' non trovato nella biblioteca.")
