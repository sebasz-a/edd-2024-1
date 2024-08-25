n = int(input())
SO = 0
LAR = 0
IS = 0

l = tuple([int(x) for x in input().split(", ") + input().split(", ") + input().split(", ")])
for i in range(n):
    if (l[i] + l[i+n] + l[i+n*2]) % 2 == 0:
        if l[i] % 2 == 0:
            SO += 1
        if l[i+n] % 2 == 0:
            LAR += 1
        if l[i+n+n] % 2 == 0:
            IS += 1
        continue
    if l[i] % 2 != 0:
        SO += 1
    if l[i+n] % 2 != 0:
        LAR += 1
    if l[i+n+n] % 2 != 0:
        IS += 1

print(f"SO:{SO}, LAR:{LAR}, IS:{IS}")
