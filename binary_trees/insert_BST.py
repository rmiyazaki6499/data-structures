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

def inorder(root):
    if root:
        left = inorder(root.left)
        print(root.data, end=" ")
        right = inorder(root.right)

def insert_BST(root, node):
    if not root:
        root = node
    else:
        if root.data < node.data:
            if not root.right:
                root.right = node
            else:
                insert_BST(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                insert_BST(root.left, node)

if __name__ == '__main__':
    root2 = Node(5)
    root2.left = Node(2)
    root2.left.left = Node(1)
    root2.left.right = Node(3)
    root2.right = Node(21)
    root2.right.left = Node(19)
    root2.right.right = Node(25)

    inorder(root2)
    print()
    insert_BST(root2, Node(9))
    inorder(root2)

