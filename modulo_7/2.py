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

    def height(self, q: Node | None = None, out: int = 0) -> int:
        if not q:
            q = self.root
        out += 1
        if not q.left and not q.right:
            return out
        l_out = 0
        if q.left:
            l_out += self.height(q.left)
        r_out = 0
        if q.right:
            r_out += self.height(q.right)
        return out + l_out if l_out >= r_out else out + r_out

C = int(input())

for _ in range(C):
    bst = BinarySearchTree()
    for num in input().split():
        if int(num) != -1:
            bst.insert(int(num))
    print(bst.height())
