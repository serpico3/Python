dizionario = {'nome':'','data':'','mail':''}

dizionario['nome'] = input('Inserisci il tuo nome: ')
dizionario['data'] = input('Inserisci la tua data di nascita: ')
dizionario['mail'] = input('Inserisci la tua mail: ')
print(dizionario)

for chiave in dizionario:
    print(chiave, dizionario[chiave])


dizionario['canzone'] = input('Inserisci il tuo canzone preferito: ')

print(dizionario['canzone'])