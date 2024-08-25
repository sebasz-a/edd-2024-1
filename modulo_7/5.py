class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root

    def draw(self, q: Node | None = None, h: int = 0, out: str = "") -> str:
        if not q:
            q = self.root
        if q.right:
            out = self.draw(q.right, h+1) + out
        out += h*"\t" + str(q.key) + "\n"
        if q.left:
            out += self.draw(q.left, h+1)
        return out

C = int(input())

for _ in range(C):
    bst = BinarySearchTree()
    for num in input().split():
        if int(num) != -1:
            bst.insert(int(num))
    print(bst.draw())
