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

    def complete(self, q: Node | None = None, height: int = 0) -> bool:
        if not q:
            q = self.root
        if not q.left and not q.right: # leaf node
            return True
        if q.left and q.right:
            if self.complete(q.left) and self.complete(q.right) and self._height(q.left) == self._height(q.right):
                return True
        return False

    def _height(self, q: Node | None = None, out: int = 0) -> int:
        if not q:
            q = self.root
        out += 1
        if not q.left and not q.right:
            return out
        l_out = 0
        if q.left:
            l_out += self._height(q.left)
        r_out = 0
        if q.right:
            r_out += self._height(q.right)
        return out + l_out if l_out >= r_out else out + r_out

C = int(input())

for i in range(C):
    bst = BinarySearchTree()
    for num in input().split():
        if int(num) != -1:
            bst.insert(int(num))
    print("completo") if bst.complete() else print("no")
