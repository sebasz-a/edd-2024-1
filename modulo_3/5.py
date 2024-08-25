c = int(input())

for _ in range(c):
    ids = tuple(map(int, input().split(" ")))

    out = 0 # cantidad de cambios
    for i in range(len(ids)):
        for j in range(1, len(ids)-i):
            if ids[j] < ids[j-1]:
                ids = ids[:j-1] + (ids[j], ids[j-1],) + ids[j+1:]
                out += 1
    print(out)
