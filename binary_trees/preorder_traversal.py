#!/usr/bin/env python3
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        def __repr__(self):
            return str(self.data)

def preorder(root):
    if root:
        print(root.data, end=" ")
        left = preorder(root.left)
        right = preorder(root.right)

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.left = Node(5)
    root1.right.left.left = Node(7)
    root1.right.left.right = Node(8)
    root1.right.right = Node(6)

    preorder(root1)
