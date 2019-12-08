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

def find_leftdepth(node):
    depth = 0
    while node.left:
        depth += 1
        node = node.left
    return depth

def find_size(root):
    if not root:
        return 0
    return (find_size(root.left) + find_size(root.right) + 1)

def check_perfect(root):
    size = find_size(root)
    depth = find_leftdepth(root)
    return size == (2 << depth) - 1

def printif_perfect(root):
    if check_perfect(root):
        print("This tree is perfect")
    else:
        print("This tree is not perfect")

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)
    root1.right.right.left = Node(8)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)

    printif_perfect(root1)
    printif_perfect(root2)
