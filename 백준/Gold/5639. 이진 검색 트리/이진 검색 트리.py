import sys

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, n):
        self.data = n
        self.left = None
        self.right = None
    
    def print(self):
        print(self.data)

    def postorder(self):
        if not self.left is None:
            self.left.postorder()
        if not self.right is None:
            self.right.postorder()
        self.print()

class TreeNode:
    def __init__(self, N):
        self.root = Node(N)

    def add_node(self, data):
        node = Node(data)
        cursor = self.root
        while True:
            if cursor.data < data:
                if not cursor.right is None:
                    cursor = cursor.right
                else:
                    cursor.right = node
                    break
            else:
                if not cursor.left is None:
                    cursor = cursor.left
                else:
                    cursor.left = node
                    break
    
    def postorder(self):
        self.root.postorder()

N = int(sys.stdin.readline())
tree = TreeNode(N)

while True:
    N = sys.stdin.readline()
    if not N:
        break
    tree.add_node(int(N))
tree.postorder()