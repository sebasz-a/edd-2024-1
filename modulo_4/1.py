from collections import deque

N, T = tuple(map(int, input().split()))
revendedores = deque()
boletas = deque()

for i in range(N):
    id, k = tuple(map(int, input().split()))
    revendedores.append(id)
    boletas.append(k)

aux = 1
while True:
    if len(revendedores) == 0:
        print("quedaron boletas disponibles")
        break
    if boletas[0] < T:
        T -= boletas[0]
        if aux % 5 == 0:
            revendedores.popleft()
            boletas.popleft()
            aux = 1
            continue
        revendedores.rotate(-1)
        boletas.rotate(-1)
        aux += 1
        continue
    print(f"{revendedores[0]} {T}")
    break
