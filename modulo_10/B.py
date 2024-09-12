N, T = tuple(map(int, input().split()))
A = []

for _ in range(N):
    A.append(int(input()))

A.sort()
nums = set(A)
ternas = {}

for i in range(N-2):
    for j in range(i+1, N):
        aux = T - A[i] - A[j]
        if aux in nums and aux not in (A[i], A[j]):
            terna = frozenset({A[i], A[j], aux})
            if terna not in ternas:
                ternas[terna] = True
                print(A[i], A[j], aux, sep=' ')

if not ternas:
    print("No hay trillizas")
