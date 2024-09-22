from collections import deque

class Node:
    def __init__(self):
        self.visited = False
        self.hops = 0

def min_path(nodes, edges, start, end):
    if start == end:
        return 0
    for node in nodes:
        nodes[node].visited = False
        nodes[node].hops = 0

    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        u = q.popleft()
        for v in edges[u]:
            if not nodes[v].visited:
                nodes[v].visited = True
                nodes[v].hops = nodes[u].hops + 1
                q.append(v)
    return nodes[end].hops

nodes = {(i, j): Node() for i in range(8) for j in range(8)}
edges = {}
for node in nodes:
    if node not in edges:
        edges[node] = set()
    i, j = node
    if i == 0:
        if j == 0:
            edges[node].add((i+1, j+2))
            edges[node].add((i+2, j+1))
        elif j == 7:
            edges[node].add((i+1, j-2))
            edges[node].add((i+2, j-1))
        elif j == 1:
            edges[node].add((i+1, j+2))
            edges[node].add((i+2, j-1))
            edges[node].add((i+2, j+1))
        elif j == 6:
            edges[node].add((i+1, j-2))
            edges[node].add((i+2, j-1))
            edges[node].add((i+2, j+1))
        else:
            edges[node].add((i+1, j-2))
            edges[node].add((i+1, j+2))
            edges[node].add((i+2, j-1))
            edges[node].add((i+2, j+1))

    elif i == 7:
        if j == 0:
            edges[node].add((i-1, j+2))
            edges[node].add((i-2, j+1))
        elif j == 7:
            edges[node].add((i-1, j-2))
            edges[node].add((i-2, j-1))
        elif j == 1:
            edges[node].add((i-1, j+2))
            edges[node].add((i-2, j-1))
            edges[node].add((i-2, j+1))
        elif j == 6:
            edges[node].add((i-1, j-2))
            edges[node].add((i-2, j-1))
            edges[node].add((i-2, j+1))
        else:
            edges[node].add((i-1, j-2))
            edges[node].add((i-1, j+2))
            edges[node].add((i-2, j-1))
            edges[node].add((i-2, j+1))

    elif i == 1:
            if j == 0:
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j+2))
                edges[node].add((i+2, j+1))
            elif j == 7:
                edges[node].add((i-1, j-2))
                edges[node].add((i+1, j-2))
                edges[node].add((i+2, j-1))
            elif j == 1:
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j+2))
                edges[node].add((i+2, j-1))
                edges[node].add((i+2, j+1))
            elif j == 6:
                edges[node].add((i-1, j-2))
                edges[node].add((i+1, j-2))
                edges[node].add((i+2, j-1))
                edges[node].add((i+2, j+1))
            else:
                edges[node].add((i-1, j-2))
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j-2))
                edges[node].add((i+1, j+2))
                edges[node].add((i+2, j-1))
                edges[node].add((i+2, j+1))

    elif i == 6:
            if j == 0:
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j+2))
                edges[node].add((i-2, j+1))
            elif j == 7:
                edges[node].add((i-1, j-2))
                edges[node].add((i+1, j-2))
                edges[node].add((i-2, j-1))
            elif j == 1:
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j+2))
                edges[node].add((i-2, j+1))
                edges[node].add((i-2, j-1))
            elif j == 6:
                edges[node].add((i-1, j-2))
                edges[node].add((i+1, j-2))
                edges[node].add((i-2, j-1))
                edges[node].add((i-2, j+1))
            else:
                edges[node].add((i-1, j-2))
                edges[node].add((i-1, j+2))
                edges[node].add((i+1, j-2))
                edges[node].add((i+1, j+2))
                edges[node].add((i-2, j-1))
                edges[node].add((i-2, j+1))

    else:
        if j == 0:
            edges[node].add((i-1, j+2))
            edges[node].add((i+1, j+2))
            edges[node].add((i-2, j+1))
            edges[node].add((i+2, j+1))
        elif j == 7:
            edges[node].add((i-1, j-2))
            edges[node].add((i+1, j-2))
            edges[node].add((i-2, j-1))
            edges[node].add((i+2, j-1))
        elif j == 1:
            edges[node].add((i-1, j+2))
            edges[node].add((i+1, j+2))
            edges[node].add((i-2, j+1))
            edges[node].add((i-2, j-1))
            edges[node].add((i+2, j+1))
            edges[node].add((i+2, j-1))
        elif j == 6:
            edges[node].add((i-1, j-2))
            edges[node].add((i+1, j-2))
            edges[node].add((i-2, j-1))
            edges[node].add((i-2, j+1))
            edges[node].add((i+2, j-1))
            edges[node].add((i+2, j+1))
        else:
            edges[node].add((i-1, j-2))
            edges[node].add((i-1, j+2))
            edges[node].add((i+1, j-2))
            edges[node].add((i+1, j+2))
            edges[node].add((i-2, j-1))
            edges[node].add((i-2, j+1))
            edges[node].add((i+2, j-1))
            edges[node].add((i+2, j+1))

C = int(input())
for _ in range(C):
    by, to = tuple(input().split())
    start = (ord(by[0]) - ord("A"), int(by[1])-1)
    end = (ord(to[0])- ord("A"), int(to[1])-1)
    print(min_path(nodes, edges, start, end))
