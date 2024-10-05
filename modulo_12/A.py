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
        return len(node.children) > 0

while True:
    E = int(input())
    if E == 0:
        break

    words = []
    for _ in range(E):
        words.append(input())

    q = True
    for w in words:
        trie = Trie()
        trie.insert(w)

        for aux in words:
            if aux == w:
                continue
            if trie.startsWithPrefix(aux):
                q = False
                break

        if not q:
            break

    if q:
        print("TRUE")
    else:
        print("FALSE")
