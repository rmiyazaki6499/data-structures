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

def levelorder(root):
    if root:
        queue = [root]
        while queue:
            node = queue.pop()
            print(node.data, end=' ')
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

if __name__ == '__main__':
        root1 = Node(1)
        root1.left = Node(2)
        root1.right = Node(3)
        root1.left.left = Node(4)
        root1.right.left = Node(5)
        root1.right.left.left = Node(7)
        root1.right.left.right = Node(8)
        root1.right.right = Node(6)

        levelorder(root1)
