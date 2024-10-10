n = int(input())
l = tuple(map(int, input().split()))
aux = l[n-1]

for i in range(n-2, -1, -1):
    aux += l[i]
    print(aux)
