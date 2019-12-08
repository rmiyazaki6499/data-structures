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
        print(root.data, end=' ')
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

def delete_BST(root, key):
    if not root:
        return Node(key)
    # Recursively traverse the tree to find the node
    if key < root.data:
        root.left = delete_BST(root.left, key)
        return root
    elif root.data < key:
        root.right = delete_BST(root.right, key)
        return root
    # We arrive at the node to be deleted
    # If one of the children is empty
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
    # if both children exists
        else:
            parent = root.right
            successor = root.right
            while successor.left:
                parent = successor
                successor = successor.left

            parent.left = successor.right
            root.data = successor.data
            successor = None
            return root

if __name__ == '__main__':
    root2 = Node(5)
    root2.left = Node(2)
    root2.left.left = Node(1)
    root2.left.right = Node(3)
    root2.right = Node(21)
    root2.right.left = Node(19)
    root2.right.right = Node(25)

    key = 21

    print("We will delete node " + str(key))

    inorder(root2)
    print()
    delete_BST(root2, key)
    inorder(root2)

