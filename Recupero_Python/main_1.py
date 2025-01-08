random = 15
tentativi=0
guess = 0

while(random != guess):
    guess = int(input("dimmi un tentativo: "))
    tentativi+=1
    if(guess<random):
        print("il numero da indovinre è maggiore ")
    elif(guess>random):
        print("il numero da indovinare è minore")
    else:
        print("corretto")

print(tentativi)