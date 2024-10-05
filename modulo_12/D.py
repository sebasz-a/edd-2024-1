from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end_of_word:
            node.is_end_of_word = True
            self.count += 1

    def _bifurcates(self, start, out = ""):
        s = deque()
        s.append(start)

        while s:
            n = s.pop()
            if len(n.children) > 1:
                return n, out
            for char, child in n.children.items():
                out += char
                s.append(child)
        return None

    def count_chars(self, results, current_word = "", node = None):
        if not node:
            node = self.root
        for char, child in node.children.items():
            aux = self._bifurcates(child)
            if aux:
                aux_word = current_word + char + aux[1]
                self.count_chars(results, aux_word, aux[0])
            else:
                results.append(current_word+char)

while True:
    A = int(input())
    if A == 0:
        break

    trie = Trie()
    for _ in range(A):
        trie.insert(input())

    results = []
    trie.count_chars(results)
    out = 0

    for w in results:
        out += len(w)
    print(out)
