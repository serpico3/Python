import classe

azienda = classe.Azienda()
while True:
    selezione = input("Cosa vuoi fare? (1)Mostra azienda (2)Aggiungi dipendente (3)esci")
    if selezione == "1":
        classe.Azienda.mostra_azienda(azienda)
    elif selezione == "2":
        lavoro = input("che lavoratore stai inserendo? (1)Programmatore (2)Manager")
        if lavoro == "1":
            azienda.aggiungi_dipendente(classe.programmatore(input("Inserisci il nome del lavoratore: "), input("Inserisci il cognome del lavoratore: "), int(input("Inserisci lo stipendio del lavoratore: "))))
            while (linguaggio.equals("break")):
                linguaggio = input("Inserisci il linguaggio del programmatore: ")
        elif lavoro == "2":
            azienda.aggiungi_dipendente(classe.manager(input("Inserisci il nome del lavoratore: "), input("Inserisci il cognome del lavoratore: "), int(input("Inserisci lo stipendio del lavoratore: ")), input("Inserisci il team del manager: ")))
    elif selezione == "3":
        break