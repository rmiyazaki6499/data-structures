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

def find_LCA(root, x, y):
    if root:
        if root.data == x or root.data == y:
            return root
        left = find_LCA(root.left, x, y)
        right = find_LCA(root.right, x, y)
        if left and right:
            return root
        return left if left is not None else right


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.right.left = Node(8)
    root1.left.right.left.left = Node(9)
    root1.left.right.left.left.left = Node(10)
    root1.right.right = Node(7)
    root1.right.right.right = Node(11)

    x = 4
    y = 9
    print("The LCA of " + str(x) + " and " + str(y) + " is " + str(find_LCA(root1, x, y).data))
