numeros = []
M = int(input())
aux = 0

while True:
    numero = int(input())
    if numero == 0:
        break
    
    numeros.append(numero)
    aux += 1
    if aux % M == 0:
        numeros.sort()
        if aux % 2 != 0:
            print(numeros[aux//2])
            continue
        mediana = numeros[aux//2] + numeros[(aux//2) - 1]
        if mediana % 2 != 0:
            print(f"{mediana}/2")
            continue
        print(mediana//2)
