vivos = set()
muertos = set()

while True:
    inp = tuple(input().split())
    tipo = inp[0]
    if tipo == "E":
        print(len(vivos))
        break
    shinobi = inp[1]
    if tipo == "B":
        if shinobi not in muertos:
            vivos.add(shinobi)
    elif tipo == "D":
        if shinobi in vivos:
            muertos.add(shinobi)
            vivos.discard(shinobi)
    else:
        if shinobi in muertos:
            vivos.add(shinobi)
