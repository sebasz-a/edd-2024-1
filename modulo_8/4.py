class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None
 
    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)
 
    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)
 
        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))
 
        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
 
        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
 
        return root
 
    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y
 
    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y
 
    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height
 
    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)
 
    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)
 
    def search(self, key):
        return self._searchRecursively(self.root, key) != None
 
    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)
 
    def draw(self, q = None, h: int = 0, out: str = "") -> str:
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
    N = int(input())
    avl = AVLTree()
    l = [1, 2]
    for i in range(2, N):
        l.append(l[i-1]+l[i-2])
    for num in l:
        avl.insert(num)
    print(avl.draw())
