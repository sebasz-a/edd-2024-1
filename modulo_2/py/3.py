c = int(input())

for _ in range(c):
    msg = tuple(input().split())

    out = ""
    if len(msg) % 2 == 0:
        start = 0
    else:
        out += msg[0]
        start = 1

    for i in range(start, len(msg)-1, 2):
        out = msg[i]+msg[i+1] + out
    print(out)
