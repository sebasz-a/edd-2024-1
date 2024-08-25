fanaticos = []

while True:
    entrada = int(input().split()[-1])

    if entrada == 0:
        print(len(fanaticos))
        break

    if len(fanaticos) >= entrada:
        continue
    
    fanaticos.append(entrada)

    for i in range(-1, (len(fanaticos)*-1)-1, -1):
        if fanaticos[i] < len(fanaticos):
            fanaticos.pop(i)    
            break
