from collections import deque

class Node:
    def __init__(self, p_num = None):
        self.visited = False
        self.p_num = p_num

def BFS(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for b in edges[node]:
            if not nodes[b].visited:
                nodes[b].visited = True
                nodes[b].p_num = nodes[node].p_num + 1
                q.append(b)

N = int(input())
for i in range(1, N+1):
    I, B = tuple(map(int, input().split(", ")))
    nodes = tuple(Node(0) if x == 0 else Node() for x in range(I))
    edges = [[] for x in range(I)]

    for _ in range(B):
        a, b = tuple(map(int, input().split()))
        edges[a].append(b)
        edges[b].append(a)

    BFS(nodes, edges, 0)
    print(f"fiesta {i}:")
    for node in range(1, I):
        out = nodes[node].p_num
        if out:
            print(node, out, sep=' ')
        else:
            print(node, "INF", sep=' ')
    if i < N:
        print()
