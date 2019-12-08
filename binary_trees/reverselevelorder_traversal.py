#!/usr/bin/env python3
from collections import deque
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        def __repr__(self):
            return str(self.data)

def reverselevelorder(root):
    if root:
        queue = deque([root])
        stack = deque([])
        while queue:
            node = queue.pop()
            stack.append(node)
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)
        while stack:
            node = stack.pop()
            print(node.data, end=' ')

if __name__ == '__main__':
        root1 = Node(1)
        root1.left = Node(2)
        root1.right = Node(3)
        root1.left.left = Node(4)
        root1.left.right = Node(5)
        root1.right.left = Node(6)
        root1.right.right = Node(7)

        reverselevelorder(root1)
