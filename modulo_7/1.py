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

    def pre_order(self, q: Node | None = None, out: str = "") -> str:
        if not q:
            q = self.root
        out += str(q.key)
        if q.left:
            out += self.pre_order(q.left)
        if q.right:
            out += self.pre_order(q.right)
        return out

C = int(input())

for _ in range(C):
    bst = BinarySearchTree()
    for num in input().split():
        if int(num) != -1:
            bst.insert(int(num))
    print(bst.pre_order())
