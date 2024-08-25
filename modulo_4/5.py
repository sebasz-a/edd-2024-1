from collections import deque

N = int(input())

for _ in range(N):
    N, k = tuple(map(int, input().split()))
    fila = deque(map(int, input().split()))

    aux = k
    out = 0
    while True:
        out += 5
        if aux == 1:
            if fila[0] - 1 == 0:
                print(out)
                break
            fila[0] -= 1
            aux = N
            fila.rotate(-1)
            continue
        if fila[0] - 1 == 0:
            fila.popleft()
            N -= 1
            aux -= 1
            continue
        fila[0] -= 1
        fila.rotate(-1)
        aux -= 1
