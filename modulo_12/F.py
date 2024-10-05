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

    def _searchPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node

    def _traverseRecursively(self, node, current_word, words_list, words):
        if node.is_end_of_word:
            words_list.append((current_word, words[current_word]))
        for char, child_node in node.children.items():
            self._traverseRecursively(child_node, current_word + char, words_list, words)

    def traverse(self, prefix, words):
        node = self._searchPrefix(prefix)
        if not node:
            return []
        words_list = []
        self._traverseRecursively(node, prefix, words_list, words)
        return words_list

L = int(input())

trie = Trie()
words = {}
for _ in range(L):
    line = map(lambda x: x.lower().strip(",.;:?!-"), input().split())
    for word in line:
        if word not in words:
            words[word] = 1
            trie.insert(word)
        else:
            words[word] += 1

C = int(input())

for _ in range(C):
    words_output = trie.traverse(input(), words)
    if not words_output:
        print("-")
    else:
        out = ""
        for word in sorted(words_output, key=lambda x: (-x[1], x[0])):
            out += word[0] + " "
        print(out.strip())
