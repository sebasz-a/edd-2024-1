import heapq

C = int(input())

for _ in range(C):
    conjunto = [int(x) for x in input().split()]
    conjunto.pop()
    heapq.heapify(conjunto)

    while True:
        if len(conjunto) == 2:
            print(f"{conjunto[0]} {conjunto[1]}")
            break
        heapq.heappush(conjunto, heapq.heappop(conjunto) + heapq.heappop(conjunto))
