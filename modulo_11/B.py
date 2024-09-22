from collections import deque

class Node:
    def __init__(self):
        self.visited = False
        self.hops = 0

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    days = {}

    while q:
        node = q.popleft()
        day = nodes[node].hops + 1
        if day not in days:
            days[day] = 0

        for e in edges[node]:
            if not nodes[e].visited:
                nodes[e].visited = True
                nodes[e].hops = day
                days[day] += 1
                q.append(e)

    return days

P = int(input())
edges = [[] for x in range(P)]

for i in range(P):
    inp = tuple(map(int, input().split()))
    if inp[0] == -1:
        continue
    for e in inp:
        edges[i].append(e)

query = tuple(map(int, input().split(", ")))
for q in query:
    nodes = tuple(Node() for x in range(P))
    days = BFS(nodes, edges, q)

    max, rad = 0, 0
    for day in days:
        if days[day] > rad:
            max, rad = day, days[day]
    if max == 0:
        print(0)
    else:
        print(max, rad, sep=' ')
