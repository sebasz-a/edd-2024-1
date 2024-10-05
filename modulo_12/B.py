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

    def startsWithPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node


def DFS(q, out = 0):
    if q.is_end_of_word:
        out += 1
    for child in q.children.values():
        out += DFS(child)
    return out

N = int(input())

words = set()
trie = Trie()
for _ in range(N):
    q = input()
    if q not in words:
        words.add(q)
        trie.insert(q)


T = int(input())

responses = {}
for _ in range(T):
    q = input()
    if q not in responses:
        s = trie.startsWithPrefix(q)
        if not s:
            print(0)
        else:
            r = DFS(s)
            responses[q] = r
            print(r)
    else:
        print(responses[q])
