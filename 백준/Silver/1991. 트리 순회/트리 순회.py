import sys

class Node:
    def __init__(self, n):
        self.data = n

    def make_node(self, value):
        self.value = value
        self.left = -1
        self.right = -1
        return self

    def make_relation(self, child1, child2):
        self.left = child1
        self.right = child2
    
    def print(self):
        print(self.data, end="")

class TreeNode:
    def __init__(self, N):
        self.data = []
        for i in range(N):
            self.data.append(Node(chr(i + ord('A'))))
        self.root = self.data[0]

    def preorder(self, cursor):
        cursor.print()
        if cursor.left != -1:
            self.preorder(cursor.left)
        if cursor.right != -1:
            self.preorder(cursor.right)

    def inorder(self, cursor):
        if cursor.left != -1:
            self.inorder(cursor.left)
        cursor.print()
        if cursor.right != -1:
            self.inorder(cursor.right)

    def postorder(self, cursor):
        if cursor.left != -1:
            self.postorder(cursor.left)
        if cursor.right != -1:
            self.postorder(cursor.right)
        cursor.print()

N = int(sys.stdin.readline().strip())

tree = TreeNode(N)

for i in range(N):
    parent, child1, child2 = map(str, sys.stdin.readline().strip().split())
    if child1 == '.':
        child1 = -1
    else:
        child1 = tree.data[ord(child1) - ord('A')]
    if child2 == '.':
        child2 = -1
    else:
        child2 = tree.data[ord(child2) - ord('A')]
    tree.data[ord(parent) - ord('A')].make_relation(child1, child2)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
