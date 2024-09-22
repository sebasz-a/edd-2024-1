from collections import deque

class Node():
    def __init__(self):
        self.visited = False

def DFS(nodes, edges, start):
    s = deque()
    s.append(start)
    count = 0

    while s:
        u = s.pop()
        if not nodes[u].visited:
            nodes[u].visited = True
            count += 1
            for v in edges[u]:
                if not nodes[v].visited:
                    s.append(v)
    return count

C = int(input())

for _ in range(C):
    A, B = map(int, input().split())
    nodes = {}
    edges = {}

    for i in range(A):
        inp = input()
        for j in range(B):
            if inp[j] == "X":
                pos = (i, j)
                nodes[pos] = Node()
                edges[pos] = set()

                if i == 0: # no mirar arriba
                    if j == 0:
                        if inp[j+1] == "X":
                            edges[pos].add((i, j+1))
                    elif j == B-1:
                        if inp[j-1] == "X":
                            edges[pos].add((i, j-1))
                    else:
                        if inp[j-1] == "X":
                            edges[pos].add((i, j-1))
                        if inp[j+1] == "X":
                            edges[pos].add((i, j+1))

                else: # mirar hacia arriba
                    if (i-1, j) in nodes:
                        edges[pos].add((i-1, j))
                        edges[(i-1, j)].add(pos)

                    if j == 0:
                        if inp[j+1] == "X":
                            edges[pos].add((i, j+1))
                    elif j == B-1:
                        if inp[j-1] == "X":
                            edges[pos].add((i, j-1))
                    else:
                        if inp[j-1] == "X":
                            edges[pos].add((i, j-1))
                        if inp[j+1] == "X":
                            edges[pos].add((i, j+1))

    max = 0
    for node in nodes:
        if not nodes[node].visited:
            defo = DFS(nodes, edges, node)
            if defo > max:
                max = defo
    print(max)
