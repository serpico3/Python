max = int(input("Inserisci un numero: "))
y = int(input("Inserisci un altro numero: "))
if(y > max):
    max = y
z = int(input("di nuovo: "))
if(z>max):
    max = z
print(max)