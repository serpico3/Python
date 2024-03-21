#Completa lo stub, considerando che la formula per la serie armonica è la seguente:
#Sum da 1 a inf, 1+1/2+1/3+1/4+...+1/n

def calculate_harmonic_series(n):
    result = 0
    for i in range(1, n+1):
        result = result + 1/i
    return result

n = int(input())
harmonic_sum = round(calculate_harmonic_series(n),5)
print(harmonic_sum)