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

    def leafs(self, q: Node | None = None, out: int =  0):
        if not q:
            q = self.root
        if not q.left and not q.right:
            return 1
        if q.left:
            out += self.leafs(q.left)
        if q.right:
            out += self.leafs(q.right)
        return out
    
C = int(input())

for _ in range(C):
    bst = BinarySearchTree()
    for num in input().split():
        if int(num) != -1:
            bst.insert(int(num))
    print(bst.leafs())
