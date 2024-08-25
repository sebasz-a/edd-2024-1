import heapq

C = int(input())

for _ in range(C):
    N, A, B = map(int, input().split())
    numeros = [((x*A) % B) for x in range(1, N+1)]

    while True:
        heapq.heapify(numeros)
        if len(numeros) == 2:
            print(numeros[1])
            break
        for i in range(len(numeros)//2):
            heapq.heappop(numeros)
        numeros = [((x*A) % B) for x in numeros]
