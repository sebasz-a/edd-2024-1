from collections import deque

C = int(input())

for _ in range(C):
    n = int(input())

    A = deque(x for x in range(n, 0, -1))
    B = deque()
    C = deque()

    valido = True
    while True:
        de, a = input().split()
        
        if de == a == "X":
            break
        if not valido:
            continue
        if de == a:
            continue
        
        if de == "A" and a == "B":
            if len(A) == 0:
                valido = False
                continue
            if len(B) == 0:
                B.append(A.pop())
                continue
            if A[-1] > B[-1]:
                valido = False
                continue
            B.append(A.pop())
            continue
        
        if de == "A" and a == "C":
            if len(A) == 0:
                valido = False
                continue
            if len(C) == 0:
                C.append(A.pop())
                continue
            if A[-1] > C[-1]:
                valido = False
                continue
            C.append(A.pop())
            continue

        if de == "B" and a == "A":
            if len(B) == 0:
                valido = False
                continue
            if len(A) == 0:
                A.append(B.pop())
                continue
            if B[-1] > A[-1]:
                valido = False
                continue
            A.append(B.pop())
            continue

        if de == "B" and a == "C":
            if len(B) == 0:
                valido = False
                continue
            if len(C) == 0:
                C.append(B.pop())
                continue
            if B[-1] > C[-1]:
                valido = False
                continue
            C.append(B.pop())
            continue

        if de == "C" and a == "A":
            if len(C) == 0:
                valido = False
                continue
            if len(A) == 0:
                A.append(C.pop())
                continue
            if C[-1] > A[-1]:
                valido = False
                continue
            A.append(C.pop())
            continue

        if de == "C" and a == "B":
            if len(C) == 0:
                valido = False
                continue
            if len(B) == 0:
                B.append(C.pop())
                continue
            if C[-1] > B[-1]:
                valido = False
                continue
            B.append(C.pop())

    if not valido:
        print("secuencia invalida")
        continue
    if len(C) == n:
        print("soluciona la torre")
        continue
    print("no soluciona la torre")
