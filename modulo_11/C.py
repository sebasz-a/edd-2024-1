from collections import deque

class Node:
    def __init__(self):
        self.visited = False

def connected(nodes, edges):
    c = 0
    max_size = 0
    for node in nodes:
        if not nodes[node].visited:
            c += 1
            size = 0
            s = deque()
            s.append(node)

            while s:
                u = s.pop()
                if not nodes[u].visited:
                    nodes[u].visited = True
                    size += 1
                    for v in edges[u]:
                        if not nodes[v].visited:
                            s.append(v)
                if size > max_size:
                    max_size = size
    return c, max_size

C = int(input())

for _ in range(C):
    nodes = {}
    edges = {}

    R = int(input())
    for _ in range(R):
        node0, node1 = tuple(map(int, input().split()))

        if node0 not in nodes:
            nodes[node0] = Node()
        if node1 not in nodes:
            nodes[node1] = Node()

        if node0 not in edges:
            edges[node0] = set()
        edges[node0].add(node1)
        if node1 not in edges:
            edges[node1] = set()
        edges[node1].add(node0)

    fams, max_num = connected(nodes, edges)
    print(fams, max_num)
