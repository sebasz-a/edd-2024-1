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

    def maxCommonPrefix(self, prefix):
        node = self.root

        out = ""
        for char in prefix:
            if len(node.children) > 1:
                break
            out += char
            node = node.children[char]

        if out:
            return out
        else:
            return "-"

while True:
    T = int(input())
    if T == 0:
        break

    nums = set()
    trie = Trie()
    min_num = input()
    for _ in range(T-1):
        num = input()
        if num not in nums:
            nums.add(num)
            if len(num) < len(min_num):
                min_num = num
            trie.insert(num)

    print(trie.maxCommonPrefix(min_num))
