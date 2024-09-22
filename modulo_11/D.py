from collections import debipartiteue

class Node:
    def __init__(self):
        self.visited = False
        self.hops = 0

def BFS(nodes, edges, start):
    nodes[start].visited = True
    bipartite = debipartiteue()
    bipartite.append(start)

    reds = set()
    reds.add(start)
    blues = set()

    while bipartite:
        node = bipartite.popleft()
        for v in edges[node]:
            if not nodes[v].visited:
                nodes[v].visited = True
                nodes[v].hops = nodes[node].hops + 1
                if nodes[v].hops % 2 == 0:
                    reds.add(v)
                else:
                    blues.add(v)
                bipartite.append(v)

    return reds, blues

C = int(input())

for _ in range(C):
    edges = {}
    nodes = {}
    N, M = tuple(map(int, input().split()))

    for _ in range(M):
        u, v = tuple(map(int, input().split(", ")))
        aux = u

        if u not in nodes:
            nodes[u] = Node()
        if v not in nodes:
            nodes[v] = Node()

        if u not in edges:
            edges[u] = set()
        if v not in edges:
            edges[v] = set()

        edges[u].add(v)
        edges[v].add(u)

    bipartite = True
    for node in nodes:
        if not nodes[node].visited:
            reds, blues = BFS(nodes, edges, node)
            for n in nodes:
                if n in reds:
                    if edges[n] & reds:
                        print("no bipartito")
                        bipartite = False
                        break
                else:
                    if edges[n] & blues:
                        print("no bipartito")
                        bipartite = False
                        break
            if not bipartite:
                break
    if bipartite:
        print("bipartito")
