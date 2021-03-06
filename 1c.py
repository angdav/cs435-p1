# Problem 1 Part C (Implement Recursive BST Functions)

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

    def insertRec(self, val):
        '''inserts val recursively into BST, returns inserted node'''
        return self.insertRecHelper(val, self.root, None, False)

    def insertRecHelper(self, val, node, prev, l):
        # val is value to be inserted
        # node is current node
        # prev is previous node
        # l is whether the node is to be inserted on left or right
        if not node:
            if self.root == None:
                self.root = Node(val)
                return
            if l:
                prev.left = Node(val)
                prev.left.parent = prev
                return prev.left
            prev.right = Node(val)
            prev.right.parent = prev
            return prev.right

        if val < node.val:
            return self.insertRecHelper(val, node.left, node, True)
        return self.insertRecHelper(val, node.right, node, False)

    def deleteRec(self, val):
        '''deletes node with given value in BST'''
        return self.deleteRecHelper(val, self.root, False)
    
    def deleteRecHelper(self, val, node, l):
        # val is value to be inserted
        # node is current node
        # l is whether the current node is a left or right node
        if not node:
            return node
        if val < node.val:
            return self.deleteRecHelper(val, node.left, True)
        elif val > node.val:
            return self.deleteRecHelper(val, node.right, False)
        else:
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
                elif node.parent.left == node:
                    node.parent.left = node.left
                    node.parent.left.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.left
                    node.parent.right.parent = node.parent
            elif node.right and not node.left:
                if node == self.root:
                    self.root = node.right
                    self.root.parent = None
                elif node.parent.left == node:
                    node.parent.left = node.right
                    node.parent.left.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.right
                    node.parent.right.parent = node.parent
            else:
                suc = self.findNextRec(node)
                node.val = suc.val
                self.deleteRecHelper(suc.val, node.right, False)

    def findNextRec(self, node):
        '''returns node with next highest value in BST'''
        return self.findNextRecHelper(node, 0, node.val)

    def findNextRecHelper(self, node, oper, orig):
        # oper 0 means check right first. if no right, go to oper 2 with node.parent; if right, go to oper 1 with node.right
        # oper 1 means go node.left until leaf
        # oper 2 means go to parent until parent >= original
        if oper == 0 and orig == self.findMaxRec().val:
            print("there is no higher value")
            return None
        if oper == 0:
            if not node.right:
                return self.findNextRecHelper(node.parent, 2, orig)
            return self.findNextRecHelper(node.right, 1, orig)
        if oper == 1:
            if not node.left:
                return node
            return self.findNextRecHelper(node.left, 1, orig)
        if oper == 2:
            if node.val >= orig:
                return node
            return self.findNextRecHelper(node.parent, 2, orig)

    def findPrevRec(self, node):
        '''returns node with next lowest value in BST'''
        return self.findPrevRecHelper(node, 0, node.val)

    def findPrevRecHelper(self, node, oper, orig):
        # oper 0 means check left first. if no left, go to oper 2 with node.parent; if left, go to oper 1 with node.left
        # oper 1 means go node.right until leaf 
        # oper 2 means go to parent until parent < original
        if oper == 0 and orig == self.findMinRec().val:
            print("there is no lower value")
            return None
        if oper == 0:
            if not node.left:
                return self.findPrevRecHelper(node.parent, 2, orig)
            return self.findPrevRecHelper(node.left, 1, orig)
        if oper == 1:
            if not node.right:
                return node
            return self.findPrevRecHelper(node.right, 1, orig)
        if oper == 2:
            if node.val <= orig:
                return node
            return self.findPrevRecHelper(node.parent, 2, orig)

    def findMaxRec(self):
        '''returns node with highest value in BST'''
        return self.findMaxRecHelper(self.root)
    
    def findMaxRecHelper(self, node):
        if not node.right:
            return node
        return self.findMaxRecHelper(node.right)

    def findMinRec(self):
        '''returns node with lowest value in BST'''
        return self.findMinRecHelper(self.root)

    def findMinRecHelper(self, node):
        if not node.left:
            return node
        return self.findMinRecHelper(node.left)

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


bst = BST(10)
bst.insertRec(5)
bst.insertRec(8)
bst.insertRec(3)
four = bst.insertRec(4)
bst.insertRec(12)
bst.insertRec(6)
bst.insertRec(7)
bst.insertRec(2)
bst.deleteRec(12)
bst.inOrder()

print("next val for", bst.root.left.val, ":", bst.findNextRec(bst.root.left).val)
print("next val for", bst.root.left.left.val, ":", bst.findNextRec(bst.root.left.left).val)
print("next val for", bst.root.left.left.left.val, ":", bst.findNextRec(bst.root.left.left.left).val)
print("next val for", four.val, ":", bst.findNextRec(four).val)
print("prev val for", bst.root.left.val, ":", bst.findPrevRec(bst.root.left).val)
print("prev val for", bst.root.left.left.val, ":", bst.findPrevRec(bst.root.left.left).val)
print("prev val for", bst.root.left.right.val, ":", bst.findPrevRec(bst.root.left.right).val)
print("prev val for", four.val, ":", bst.findPrevRec(four).val)

print("max value:", bst.findMaxRec().val)
print("min value:", bst.findMinRec().val)

bst.deleteRec(7)
bst.deleteRec(2)
bst.deleteRec(5)
bst.deleteRec(6)
bst.deleteRec(3)
bst.deleteRec(4)
bst.deleteRec(10)
bst.deleteRec(8)

bst.insertRec(69)
bst.inOrder()
print("max value:", bst.findMaxRec().val)
print("min value:", bst.findMinRec().val)