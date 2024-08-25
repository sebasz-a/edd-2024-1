from collections import deque

c = int(input())

for _ in range(c):
    pila = deque(map(int, input().split()))
    while True:
        if len(pila) != 1:
            ult = pila.pop()
            if (ult + pila[-1]) % 2 == 0:
                pila.append((ult + pila.pop()) // 2)
                continue
            print(f"{len(pila) + 1} {ult}")
            break
        print(f"1 {pila[0]}")
        break
