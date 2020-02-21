# Problem 1 Part D (Implement Iterative BST Functions)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def isLeaf(self):
        '''returns if node is leaf or not'''
        return not self.left and not self.right

class BST:
    def __init__(self, rootval):
        self.root = Node(rootval)