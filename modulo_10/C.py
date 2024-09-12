M = int(input())
messages = {}
winners = set()
winner = False # para saber si hay o no ganadores

while True:
    inp = tuple(input().split())
    tipo = inp[0]    
    if tipo == "end":
        if not winner:
            print(0)
        break
    
    boleta = int(inp[1])
    if tipo == "winner":
        winners.add(boleta)

    if tipo == "sms":
        if boleta not in messages:
            messages[boleta] = 0
        messages[boleta] += 1

        if boleta in winners:
            winner = True
            aux = messages[boleta] * len(winners)
            print(boleta, M // aux, sep=' ')
