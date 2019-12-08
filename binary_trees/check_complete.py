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

def check_complete(root):
    if root:
        queue = [root]
        flag = False
        while queue:
            node = queue.pop()
            if flag and (node.left or node.right):
                return False
            if node.left:
                queue.insert(0, node.left)
            else:
                flag = True
            if node.right:
                queue.insert(0, node.right)
            else:
                flag = True
        return True

if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)
    root1.right.right.left = Node(8)

    if check_complete(root1):
        print("This tree is complete")
    else:
        print("This tree is not complete")
