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

def array_BST(array):
    deque(array)
    root = Node(array.pop())
    for element in array:
        node = Node(element)
        insert_BST(root, node)
    return root

if __name__ == '__main__':

    array = [
        79, 47, 68, 87, 84, 91, 21, 32, 34, 2,
        20, 22, 98, 1, 62, 95
    ]
    inorder(array_BST(array))

