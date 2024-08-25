import heapq

lenght = int(input())
N = int(input())
orden = []

for i in range(N):
    code, start, step = map(int, input().split())
    for j in range(start, lenght+1, step):
        heapq.heappush(orden, j)

for i in range(len(orden)):
    print(heapq.heappop(orden))
