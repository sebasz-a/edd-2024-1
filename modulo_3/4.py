from bisect import bisect_left

k = int(input())
postes = tuple(sorted(map(int, input().split(" "))))

p = int(input())
for _ in range(p):
    pareja = tuple(map(int, input().split(" ")))
    print(f"{abs(bisect_left(postes, pareja[1]) - bisect_left(postes, pareja[0]))} kms")
