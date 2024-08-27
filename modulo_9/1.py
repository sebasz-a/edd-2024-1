poke_F = set()
poke_V = set()

while True:
    inp = tuple(input().split())
    nombre = inp[0]
    if nombre == "#":
        print(len(poke_F), len(poke_V), len(poke_F | poke_V), sep=" ")
        break
    pokemon = int(inp[1])
    if nombre == "F":
        poke_F.add(pokemon)
    else:
        poke_V.add(pokemon)
    