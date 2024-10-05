from collections import deque

class TrieNode:
    def __init__(self, height = 0):
        self.children = {}
        self.is_end_of_word = False
        self.height = height

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(node.height+1)
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.count += 1

    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node

    def delete(self, word):
        q = deque()
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            else:
                q.append(node)
                node = node.children[char]
        if len(node.children) > 0:
            node.is_end_of_word = False
        else:
            for char in word[::-1]:
                node = q.pop()
                if node.is_end_of_word or len(node.children) > 1:
                    break
                else:
                    node.children.pop(char)
            self.count -= 1
            return True

def traverse(n, h, k):
    q = deque()
    q.append(n)

    while q:
        c = q.popleft()
        if c.height < h:
            pass
        elif c.height == h:
            if DFS(c) >= k:
                return True
        else:
            return False

        for child in c.children.values():
            q.append(child)
    return False

def DFS(n):
    q = deque()
    q.append(n)
    out = 0

    while q:
        c = q.pop()
        if c.is_end_of_word:
            out += 1
        for child in c.children.values():
            q.append(child)
    return out

P = int(input())

trie = Trie()
words = set()
for _ in range(P):
    inp = tuple(input().split())
    opt = int(inp[0])
    if opt == 1:
        if inp[1] not in words:
            words.add(inp[1])
            trie.insert(inp[1])

    elif opt == 2:
        if inp[1] in words:
            words.remove(inp[1])
            trie.delete(inp[1])

    else:
        k, h = map(int, inp[1:])

        if traverse(trie.root, h, k):
            print("SI")
        else:
            print("NO")
