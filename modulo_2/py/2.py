n = int(input())
SO = 0
LAR = 0
IS = 0

so_l = tuple(map(int, input().split(", ")))
lar_l = tuple(map(int, input().split(", ")))
is_l = tuple(map(int, input().split(", ")))

for i in range(n):
    result = so_l[i] + lar_l[i] + is_l[i]
    if result % 2 == 0:
        if so_l[i] % 2 == 0:
            SO += 1
        if lar_l[i] % 2 == 0:
            LAR += 1
        if is_l[i] % 2 == 0:
            IS += 1
    else:
        if so_l[i] % 2 != 0:
            SO += 1
        if lar_l[i] % 2 != 0:
            LAR += 1
        if is_l[i] % 2 != 0:
            IS += 1

print(f"SO: {SO}, LAR:{LAR}, IS:{IS}")
