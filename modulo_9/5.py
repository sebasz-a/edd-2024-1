libros_F = set()
libros_G = set()

while True:
    inp = tuple(input().split())
    if inp[0] == "0":
        print(len(libros_F), len(libros_G), sep=" ")
        break
    comprador = inp[1]
    if comprador == "F":
        libros_F.add(inp[0])
    else:
        libros_G.add(inp[0])
    if inp[0] in libros_F and inp[0] in libros_G:
        if int(inp[0]) % 2 == 0:
            libros_G.remove(inp[0])
        else:
            libros_F.remove(inp[0])
