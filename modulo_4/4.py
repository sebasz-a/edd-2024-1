from collections import deque

N = int(input())
abiertas = "{", "(", "["

for _ in range(N):
    serie = tuple(input().split())
    aux = deque()
    correcto = True

    if len(serie) == 1:
        print("correcta")
        continue
    if len(serie) % 2 == 0:
        print("incorrecta")
        continue

    for i in range(len(serie)-1):
        if serie[i] in abiertas:
            aux.append(serie[i])
            continue
        else:
            if len(aux) == 0:
                print("incorrecta")
                correcto = False
                break

        if serie[i] == "}" and aux[-1] != "{":
            print("incorrecta")
            correcto = False
            break
        if serie[i] == ")" and aux[-1] != "(":
            print("incorrecta")
            correcto = False
            break
        if serie[i] == "]" and aux[-1] != "[":
            print("incorrecta")
            correcto = False
            break
        
        aux.pop()
    if correcto:
        print("correcta")
