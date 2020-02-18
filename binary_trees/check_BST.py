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


def check_BST(root, lower=None, higher=None):
    if not root:
        return True
    if lower and root.data < lower:
        return False
    if higher and root.data > higher:
        return False
    return check_BST(root.left, lower, root.data) and \
        check_BST(root.right, root.data, higher)


def printif_BST(root):
    if check_BST(root):
        print("This tree is a BST")
    else:
        print("This tree is not a BST")

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.left = Node(5)
    root1.right.left.left = Node(7)
    root1.right.left.right = Node(8)
    root1.right.right = Node(6)

    root2 = Node(5)
    root2.left = Node(2)
    root2.left.left = Node(1)
    root2.left.right = Node(3)
    root2.right = Node(21)
    root2.right.left = Node(19)
    root2.right.right = Node(25)

    printif_BST(root1)
    printif_BST(root2)

