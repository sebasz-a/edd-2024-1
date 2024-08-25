import heapq

C = int(input())

for _ in range(C):
    N = int(input())

    conjunto = input().split()
    heapq.heapify(conjunto)

    n1 = ""
    n2 = ""
    for i in range(N):
        if i % 2 == 0:
            n1 += heapq.heappop(conjunto)
            continue
        n2 += heapq.heappop(conjunto)
    print(int(n1) + int(n2))
