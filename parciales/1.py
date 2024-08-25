from collections import deque
Q = int(input())
cilindro = deque()

for _ in range(Q):
    entrada = tuple(map(int, input().split()))
    tipo = entrada[0]
    if tipo == 1:
        K, E = entrada[1], entrada[2]
        cilindro.append([K, E])
    else:
        H = entrada[1]
        out = 0
        while H > 0:
            current = cilindro[0]
            if current[1] <= H:
                H -= current[1]
                out += current[1] * current[0]
                cilindro.popleft()
            else:
                current[1] -= H
                out += H * current[0]
                break
        print(out)
