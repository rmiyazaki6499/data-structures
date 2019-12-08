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

# Recursive function to check if two given binary trees are identical or not
def isIdentical(root1, root2):
    if not root1 and not root2:
        return True

    if (root1 and root2) == (root1.data == root2.data):
        return (isIdentical(root1.left, root2.left) and\
                isIdentical(root1.right, root2.right))
    else:
        return False


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

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.left.right.left = Node(8)
    root2.left.right.left.left = Node(9)
    root2.left.right.left.left.left = Node(10)
    root2.right.right = Node(7)
    root2.right.right.right = Node(11)

    print("root1 and root2 are Identical " if isIdentical(root1, root2)
          else "root1 and root2 are not Identical ")

    root1.right.right.right = Node(12)
    print("root1 and root2 are Identical " if isIdentical(root1, root2)
          else "root1 and root2 are not Identical ")
