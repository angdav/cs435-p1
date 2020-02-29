import node as nd

class AVL:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = nd.Node(rootval)
        self.traversecount = 0

    def getbf(self, node):
        '''returns the balance factor of the given node'''
        if node.right and not node.left:
            return 0 - node.right.height
        elif not node.right and node.left:
            return node.left.height
        elif not node.right and not node.right:
            return 0
        return node.left.height - node.right.height

    def setHeight(self, node):
        '''sets the proper height of a given node and all its parents'''
        while node:
            if not node.left and not node.right:
                node.height = 1
            elif node.left and not node.right:
                node.height = node.left.height + 1
            elif not node.left and node.right:
                node.height = node.right.height + 1
            else:
                node.height = max(node.left.height, node.right.height) + 1
            node = node.parent

    def balance(self, node):
        '''balances the AVL tree'''
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
            newroot.right = nd.Node(node.val)
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
            newroot.right = nd.Node(node.val)
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
        self.setHeight(newroot.right)
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
            newroot.left = nd.Node(lnode.val)
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
            newroot.left = nd.Node(node.val)
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
            newroot.left = nd.Node(node.val)
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
        self.setHeight(newroot.left)
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
            newroot.right = nd.Node(lnode.val)
            newroot.right.parent = newroot
            newroot.right.right = store2
            if store2:
                store2.parent = newroot.right
            newroot.right.left = store
            if store:
                store.parent = newroot.right
        self.rr(node)

    def insertIter(self, val):
        '''inserts val iteratively into AVL, returns inserted node'''
        node = self.root
        levelcount = 1
        if self.root == None:
            self.root = nd.Node(val)
            return self.root

        while True:
            prev = node
            if val < node.val:
                if node.left:
                    node = node.left
                    self.traversecount += 1
                    continue
                node.left = nd.Node(val)
                node.left.parent = prev
                self.setHeight(node)
                self.balance(node)
                return node.left
            if node.right:
                node = node.right
                self.traversecount += 1
                continue
            node.right = nd.Node(val)
            node.right.parent = prev
            self.setHeight(node)
            self.balance(node)
            return node.right

    def deleteIter(self, val):
        '''deletes node with given value in AVL'''
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
                self.setHeight(node.parent)
                self.balance(node.parent)
            else:
                node.parent.right = None
                self.setHeight(node.parent)
                self.balance(node.parent)
        elif node.left and not node.right:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                self.setHeight(self.root)
                self.balance(self.root)
            else:
                self.jumpPointLeft(node)
        elif node.right and not node.left:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                self.setHeight(self.root)
                self.balance(self.root)
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
                self.setHeight(suc.parent)
                self.balance(suc.parent)
            elif suc.left and suc.right:
                suc.parent.right = suc.right
                suc.parent.right.parent = suc.parent
                store = suc.left
                newnode = suc.parent.right
                while newnode.left:
                    newnode = newnode.left
                newnode.left = store
                store.parent = newnode
                self.setHeight(store)
                self.balance(store)
            elif suc.left:
                self.jumpPointLeft(suc)
            elif suc.right:
                self.jumpPointRight(suc)
        
    def jumpPointLeft(self, node):
        if node.parent.left == node:
            node.parent.left = node.left
            node.parent.left.parent = node.parent
            self.setHeight(node.parent.left)
            self.balance(node.parent.left)
        elif node.parent.right == node:
            node.parent.right = node.left
            node.parent.right.parent = node.parent
            self.setHeight(node.parent.right)
            self.balance(node.parent.right)
    
    def jumpPointRight(self, node):
        if node.parent.left == node:
            node.parent.left = node.right
            node.parent.left.parent = node.parent
            self.setHeight(node.parent.left)
            self.balance(node.parent.left)
        elif node.parent.right == node:
            node.parent.right = node.right
            node.parent.right.parent = node.parent
            self.setHeight(node.parent.right)
            self.balance(node.parent.right)


    def findNextIter(self, node):
        '''returns node with next highest value in AVL'''
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
        '''returns node with next lowest value in AVL'''
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
        '''returns node with highest value in AVL'''
        node = self.root
        while node.right:
            node = node.right
        return node

    def findMinIter(self):
        '''returns node with lowest value in AVL'''
        node = self.root
        while node.left:
            node = node.left
        return node

    def inOrder(self):
        '''prints AVL with inorder traversal'''
        print("INORDER TRAVERSAL")
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, node):
        if not node:
            return
        self.inOrderHelper(node.left)
        print(node.val, node.height)
        self.inOrderHelper(node.right)