class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    def isLeaf(self):
        '''returns if node is leaf or not'''
        return not self.left and not self.right
