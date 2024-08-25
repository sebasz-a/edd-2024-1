n = int(input())
l = tuple([int(x) for x in input().split(" ")])
aux = l[-1]
for i in l[-2::-1]:
    aux += i
    print(aux)
