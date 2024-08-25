digitos = []

def c_borrado(lista):
    if len(lista) == 0:
        return
    lista.pop()
    
while True:
    entrada = input().split()

    if entrada[0] == "end":
        break

    if len(entrada) == 1:
        if entrada[0] != "C":
            digitos.append(entrada[0])
            continue
        c_borrado(digitos)
        continue
    
    if entrada[0] == "D":
        if int(entrada[1]) == 1:
            c_borrado(digitos)
            continue
        if len(digitos) < int(entrada[1]):
            continue
        for i in range(int(entrada[1])):
            digitos.pop()
        continue

    i, j = int(entrada[1]), int(entrada[2])
    if len(digitos) < j:
        continue
    out = ""
    for dig in range(i-1, j):
        out += str(digitos[dig])
    print(out)
