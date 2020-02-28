# Problem 4 Part C (Implement Iterative AVL Functions)
import genarray as ga

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

    def insertIter(self, val):
        '''inserts val iteratively into BST, returns inserted node'''
        node = self.root
        if self.root == None:
            self.root = Node(val)
            return self.root

        while True:
            prev = node
            if val < node.val:
                if node.left:
                    node = node.left
                    continue
                node.left = Node(val)
                node.left.parent = prev
                return node.left
            if node.right:
                node = node.right
                continue
            node.right = Node(val)
            node.right.parent = prev
            return node.right

    def deleteIter(self, val):
        '''deletes node with given value in BST'''
        node = self.root
        l = False

        while node.val != val:
            if val < node.val:
                node = node.left
                l = True
            else:
                node = node.right
                l = False
        if node.isLeaf():
            if not node.parent:
                self.root = None
            elif l:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left and not node.right:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
            else:
                self.jumpPointLeft(node)
        elif node.right and not node.left:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
            else:
                self.jumpPointRight(node)
        else:
            suc = self.findNextIter(node)
            node.val = suc.val
            if suc.isLeaf():
                if suc.parent.right == suc:
                    suc.parent.right = None
                else:
                    suc.parent.left = None
            elif suc.left and suc.right:
                suc.parent.right = suc.right
                suc.parent.right.parent = suc.parent
                store = suc.left
                newnode = suc.parent.right
                while newnode.left:
                    newnode = newnode.left
                newnode.left = store
                store.parent = newnode
            elif suc.left:
                self.jumpPointLeft(suc)
            elif suc.right:
                self.jumpPointRight(suc)
        
    def jumpPointLeft(self, node):
        if node.parent.left == node:
            node.parent.left = node.left
            node.parent.left.parent = node.parent
        elif node.parent.right == node:
            node.parent.right = node.left
            node.parent.right.parent = node.parent
    
    def jumpPointRight(self, node):
        if node.parent.left == node:
            node.parent.left = node.right
            node.parent.left.parent = node.parent
        elif node.parent.right == node:
            node.parent.right = node.right
            node.parent.right.parent = node.parent


    def findNextIter(self, node):
        '''returns node with next highest value in BST'''
        val = node.val
        if val == self.findMaxIter().val:
            print("there is no higher value")
            return None
        if not node.right:
            node = node.parent
            while node and node.val < val:
                node = node.parent
            return node
        else:
            node = node.right
            while node.left:
                node = node.left
            return node

    def findPrevIter(self, node):
        '''returns node with next lowest value in BST'''
        val = node.val
        if val == self.findMinIter().val:
            print("there is no lower value")
            return None
        if not node.left:
            node = node.parent
            while node and node.val >= val:
                node = node.parent
            return node
        else:
            node = node.left
            while node.right:
                node = node.right
            return node

    def findMaxIter(self):
        '''returns node with highest value in BST'''
        node = self.root
        while node.right:
            node = node.right
        return node

    def findMinIter(self):
        '''returns node with lowest value in BST'''
        node = self.root
        while node.left:
            node = node.left
        return node

    def inOrder(self):
        '''prints BST with inorder traversal'''
        print("INORDER TRAVERSAL")
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, node):
        if not node:
            return
        self.inOrderHelper(node.left)
        print(node.val)
        self.inOrderHelper(node.right)


bst = BST(5000)
lst = ga.getRandomArray(1000)
print(lst)
for val in lst:
    bst.insertIter(val)
bst.inOrder()

print("next val for", bst.root.left.val, ":", bst.findNextIter(bst.root.left).val)
print("next val for", bst.root.left.left.val, ":", bst.findNextIter(bst.root.left.left).val)
print("next val for", bst.root.left.left.left.val, ":", bst.findNextIter(bst.root.left.left.left).val)
print("prev val for", bst.root.left.val, ":", bst.findPrevIter(bst.root.left).val)
print("prev val for", bst.root.left.left.val, ":", bst.findPrevIter(bst.root.left.left).val)
print("prev val for", bst.root.left.right.val, ":", bst.findPrevIter(bst.root.left.right).val)

print("max value:", bst.findMaxIter().val)
print("min value:", bst.findMinIter().val)

print(bst.root.val)
print(bst.root.left.val)
print(bst.root.left.left.val)
print(bst.root.left.left.left.val)