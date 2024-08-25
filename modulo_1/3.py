n = int(input())
Q = 0
R = 0

for i in range(n):
    aux = int(input())
    if aux > 0:
        Q += aux
        continue
    R += aux
print(f"positivos {Q}, negativos {R}")