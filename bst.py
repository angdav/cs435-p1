import node as nd

class BST:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = nd.Node(rootval)
        self.traversecount = 0
    
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
                self.root = nd.Node(val)
                return
            if l:
                prev.left = nd.Node(val)
                prev.left.parent = prev
                return prev.left
            prev.right = nd.Node(val)
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

    def insertIter(self, val):
        '''inserts val iteratively into BST, returns inserted node'''
        node = self.root
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
                return node.left
            if node.right:
                node = node.right
                self.traversecount += 1
                continue
            node.right = nd.Node(val)
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