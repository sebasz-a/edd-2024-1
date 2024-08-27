poblacion = {x for x in range(1, int(input())+1)}

while True:
    inp = tuple(input().split())
    tipo = inp[0]
    if tipo == "#":
        break
    if tipo == "new":
        hijo = int(inp[1]) + int(inp[2])
        while True:
            if hijo in poblacion:
                hijo += 1
            else:
                poblacion.add(hijo)
                break
    if tipo == "search":
        if int(inp[1]) in poblacion:
            print("existe")
        else:
            print("no existe")
