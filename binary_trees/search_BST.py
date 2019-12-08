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

def search_BST(root, key):
    if not root or root.data == key:
        return root
    if root.data < key:
        return search_BST(root.right, key)
    return search_BST(root.left, key)

if __name__ == '__main__':
    root2 = Node(5)
    root2.left = Node(2)
    root2.left.left = Node(1)
    root2.left.right = Node(3)
    root2.right = Node(21)
    root2.right.left = Node(19)
    root2.right.right = Node(25)

    key = 3

    print("The key " + str(key) + " is in the BST as " + str(search_BST(root2, key).data))
