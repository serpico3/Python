from biblioteca.gestore_biblioteca import Biblioteca

file_biblioteca = "biblioteca.json"

biblioteca = Biblioteca(file_biblioteca)

while True:
    azione = input("Cosa vuoi fare? (Add/Mostra/Remove/Prestito/Ritiro/Fine): ").strip().lower()
    if azione == "fine":
        print("Uscita dal programma.")
        break
    elif azione == "add":
        titolo = input("Inserisci il titolo: ").strip()
        autore = input("Inserisci l'autore: ").strip()
        pagine = int(input("Inserisci il numero di pagine: ").strip())
        biblioteca.aggiungi_libro(titolo, autore, pagine)
    elif azione == "mostra":
        biblioteca.mostra_libri()
    elif azione == "remove":
        titolo = input("Inserisci il titolo del libro da rimuovere: ").strip()
        biblioteca.remove_libro(titolo)
    elif azione == "prestito":
        titolo = input("Inserisci il titolo del libro da prestare: ").strip()
        biblioteca.prestito_libro(titolo)
    elif azione == "ritiro":
        titolo = input("Inserisci il titolo del libro da ritirare: ").strip()
        biblioteca.ritiro_libro(titolo)
    else:
        print("Comando non riconosciuto. Usa 'Add', 'Mostra', 'Remove', 'Prestito' o 'Fine'.")
