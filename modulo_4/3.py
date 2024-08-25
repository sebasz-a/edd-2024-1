from collections import deque

fila = deque()
while True:
    a = input().split()
    if a[0] == "termina":
        if len(fila) == 0:
            print("uroboro vacio")
            break
        print(f"cabeza {fila[0]} cola {fila[-1]}")
        break
    if a[0] != "engulle":
        fila.append(int(a[-1]))
        continue
    if len(fila) == 0:
        continue
    if fila[0] > fila[-1]:
        fila.pop()
        continue
    fila.popleft()
