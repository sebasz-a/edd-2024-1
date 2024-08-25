jugadores = []

while True:
    k = int(input())
    
    if k == 0:
        out = ""
        for jugador in jugadores:
            if jugador != 0:
                out += f"{jugador} "
                continue
        if not out:
            print(0)
            break
        print(out)
        break

    if len(jugadores) == 0:
        jugadores.append(k)
        continue

    c1 = False
    c2 = False
    ap = True
    for i in range(len(jugadores)):
        if jugadores[i] == 0:
            continue
        if jugadores[i] == k:
            jugadores[i] = 0
            ap = False
            break
        if jugadores[i] == k+1 and not c1:
            c1 = True
            c2 = False
            aux = i
            continue
        if jugadores[i] == k-1 and not c1 and not c2:
            c2 = True
            aux = i
            continue
    if c1 or c2:
        jugadores[aux] = 0
        continue
    if ap:
        jugadores.append(k)
