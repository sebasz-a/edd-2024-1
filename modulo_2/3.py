c = int(input())
exit = ()

def desencriptacion(l: list) -> str:
    out = ""
    aux = list(reversed(l))
    for i in range(1,len(aux), 2):
        out += aux[i]
        out += aux[i-1]
    if len(aux) % 2 != 0:
        out += aux[-1]
    print(out)

for i in range(c):
    desencriptacion(input().split(" "))
