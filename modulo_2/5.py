c = int(input())
for _ in range(c):
    info = input().split(" ")
    billetes = tuple(map(lambda x: int(x), input().split(" ")))
    aux = 0
    out = [0] * int(info[0])
    for n in billetes:
        out[aux] += n
        if aux == int(info[0])-1:
            aux = 0
            continue
        aux += 1
    print(max(out) - min(out))
