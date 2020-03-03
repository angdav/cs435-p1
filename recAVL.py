# Extra Credit (Implement Recursive AVL Functions)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def isLeaf(self):
        '''returns if node is leaf or not'''
        return not self.left and not self.right

class recAVL:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = nd.Node(rootval)

    def getHeight(self, node):
        '''returns the height of the tree starting at the given node'''
        if node is None:
            return 0
        
        lHeight = self.getHeight(node.left)
        rHeight = self.getHeight(node.right)

        if (lHeight > rHeight):
            return lHeight + 1
        return rHeight + 1

    def getbf(self, node):
        '''returns the balance factor of the given node'''
        if node.right and not node.left:
            return 0 - self.getHeight(node.right)
        elif not node.right and node.left:
            return self.getHeight(node.left)
        elif not node.right and not node.right:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def balance(self, node):
        '''balances the recAVL tree'''
        while node:
            if self.getbf(node) > 1 and self.getbf(node.left) > 0: # left left
                self.ll(node)
            elif self.getbf(node) > 1 and self.getbf(node.left) < 0: # left right
                self.lr(node)
            elif self.getbf(node) < -1 and self.getbf(node.right) < 0: # right right
                self.rr(node)
            elif self.getbf(node) < -1 and self.getbf(node.right) > 0: # right left
                self.rl(node)
            node = node.parent

    def ll(self, node):
        '''performs a left-left rotation'''
        newroot = node.left
        parent = node.parent
        if node.left.right:
            store = node.left.right
            store2 = node.right
            newroot.right = Node(node.val)
            newroot.right.parent = node.left
            if parent:
                if parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
            else:
                newroot.parent = None
            newroot.right.left = store
            if store:
                store.parent = newroot.right
            newroot.right.right = store2
            if store2:
                store2.parent = newroot.right
            node.left = None
            node.right = None
        else:
            store2 = node.right
            newroot.right = Node(node.val)
            newroot.right.parent = node.left
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
            newroot.right.right = store2
            if store2:
                store2.parent = newroot.right
            node.left = None
            node.parent = None
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def lr(self, node):
        '''performs a left-right rotation'''
        lnode = node.left
        parent = lnode.parent
        if lnode.right:
            store = lnode.right.left
            store2 = lnode.left
            newroot = lnode.right
            if parent:
                if parent.left == lnode:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == lnode:
                    parent.right = newroot
                    newroot.parent = parent
            node.left = newroot
            newroot.parent = node
            lnode.parent = None
            lnode.right = None
            newroot.left = Node(lnode.val)
            newroot.left.parent = newroot
            newroot.left.left = store2
            if store2:
                store2.parent = newroot.left
            newroot.left.right = store
            if store:
                store.parent = newroot.left
        self.ll(node)

    def rr(self, node):
        '''performs a right-right rotation'''
        newroot = node.right
        parent = node.parent
        if node.right.left:
            store = node.right.left
            store2 = node.left
            newroot.left = Node(node.val)
            newroot.left.parent = node.right
            if parent:
                if parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
            else:
                newroot.parent = None
            newroot.left.right = store
            if store:
                store.parent = newroot.left
            newroot.left.left = store2
            if store2:
                store2.parent = newroot.left
            node.right = None
            node.left = None
        else:
            store2 = node.left
            newroot.left = Node(node.val)
            newroot.left.parent = node.right
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
            newroot.left.left = store2
            if store2:
                store2.parent = newroot.left
            node.right = None
            node.parent = None
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def rl(self, node):
        '''performs a right-left rotation'''
        lnode = node.right
        parent = lnode.parent
        if lnode.left:
            store = lnode.left.right
            store2 = lnode.right
            newroot = lnode.left
            if parent:
                if parent.left == lnode:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == lnode:
                    parent.right = newroot
                    newroot.parent = parent
            node.right = newroot
            newroot.parent = node
            lnode.parent = None
            lnode.left = None
            newroot.right = Node(lnode.val)
            newroot.right.parent = newroot
            newroot.right.right = store2
            if store2:
                store2.parent = newroot.right
            newroot.right.left = store
            if store:
                store.parent = newroot.right
        self.rr(node)

    def insertRec(self, val):
        '''inserts val recursively into recAVL, returns inserted node'''
        return self.insertRecHelper(val, self.root, None, False)

    def insertRecHelper(self, val, node, prev, l):
        if not node:
            if self.root == None:
                self.root = Node(val)
                return
            if l:
                prev.left = Node(val)
                prev.left.parent = prev
                self.balance(prev)
                return prev.left
            prev.right = Node(val)
            prev.right.parent = prev
            self.balance(prev)
            return prev.right

        if val < node.val:
            return self.insertRecHelper(val, node.left, node, True)
        return self.insertRecHelper(val, node.right, node, False)

    def deleteRec(self, val):
        '''deletes node with given value in recAVL'''
        return self.deleteRecHelper(val, self.root, False)
    
    def deleteRecHelper(self, val, node, l):
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
                    self.balance(node.parent)
                else:
                    node.parent.right = None
                    self.balance(node.parent)
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
                self.balance(node.parent)
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
                self.balance(node.parent)
            else:
                suc = self.findNextRec(node)
                node.val = suc.val
                self.deleteRecHelper(suc.val, node.right, False)

    def findNextRec(self, node):
        '''returns node with next highest value in recAVL'''
        return self.findNextRecHelper(node, 0, node.val)

    def findNextRecHelper(self, node, oper, orig):
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
        '''returns node with next lowest value in recAVL'''
        return self.findPrevRecHelper(node, 0, node.val)

    def findPrevRecHelper(self, node, oper, orig):
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
        '''returns node with highest value in recAVL'''
        return self.findMaxRecHelper(self.root)
    
    def findMaxRecHelper(self, node):
        if not node.right:
            return node
        return self.findMaxRecHelper(node.right)

    def findMinRec(self):
        '''returns node with lowest value in recAVL'''
        return self.findMinRecHelper(self.root)

    def findMinRecHelper(self, node):
        if not node.left:
            return node
        return self.findMinRecHelper(node.left)

    def inOrder(self):
        '''prints recAVL with inorder traversal'''
        print("INORDER TRAVERSAL")
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, node):
        if not node:
            return
        self.inOrderHelper(node.left)
        print(node.val)
        self.inOrderHelper(node.right)
