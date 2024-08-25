c = int(input())
for _ in range(c):
    n = int(input())
    tablero = [int(x) for x in input().split(" ")]
    aux = 0
    out = 0
    while True:
        if (aux < 0 or aux >= n) or tablero[aux] == 0:
            print(out)
            aux, out = 0, 0
            break
        x = aux
        aux += tablero[aux]
        tablero[x] = 0
        out += 1
