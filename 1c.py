# Problem 1 Part C (Implement Recursive BST Functions)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def isLeaf(self):
        return not self.left and not self.right

class BST:
    def __init__(self, rootval):
        self.root = Node(rootval)

    def insertRec(self, val, node="init", prev=None, l=False):
        '''inserts val recursively into BST'''
        # val is value to be inserted
        # node is current node
        # prev is previous node
        # l is whether the node is to be inserted on left or right
        if node == "init":
            node = self.root
        if not node:
            if l:
                prev.left = Node(val)
                prev.left.parent = prev
            else:
                prev.right = Node(val)
                prev.right.parent = prev
            return

        if val < node.val:
            self.insertRec(val, node.left, node, True)
        else:
            self.insertRec(val, node.right, node, False)

    def deleteRec(self):
        pass

    def findNextRec(self, node, oper=0, orig="init"):
        '''returns node with next highest value in BST'''
        # oper 0 means check right first. if no right, go to oper 2; if right, go to oper 1 with node.right
        # oper 1 means go node.left until leaf
        # oper 2 means go to parent until parent > original
        if orig == "init":
            orig = node.val
        if oper == 0 and orig == self.findMaxRec(self.root).val:
            print("there is no higher value")
            return None
        if oper == 0:
            if not node.right:
                return self.findNextRec(node, 2, orig)
            return self.findNextRec(node.right, 1, orig)
        if oper == 1:
            if not node.left:
                return node
            return self.findNextRec(node.left, 1, orig)
        if oper == 2:
            if node.val >= orig:
                return node
            return self.findNextRec(node.parent, 2, orig)

    def findPrevRec(self, node, oper=0, orig="init"):
        '''returns node with next lowest value in BST'''
        # oper 0 means check left first. if no left, go to oper 2; if left, go to oper 1 with node.left
        # oper 1 means go node.right until leaf 
        # oper 2 means go to parent until parent < original
        if orig == "init":
            orig = node.val
        if oper == 0 and orig == self.findMinRec(self.root).val:
            print("there is no lower value")
            return None
        if oper == 0:
            if not node.left:
                return self.findPrevRec(node, 2, orig)
            return self.findPrevRec(node.left, 1, orig)
        if oper == 1:
            if not node.right:
                return node
            return self.findPrevRec(node.right, 1, orig)
        if oper == 2:
            if node.val <= orig:
                return node
            return self.findPrevRec(node.parent, 2, orig)

    def findMaxRec(self, node):
        "returns node with highest value in BST"
        if not node.right:
            return node
        return self.findMaxRec(node.right)

    def findMinRec(self, node):
        "returns node with lowest value in BST"
        if not node.left:
            return node
        return self.findMinRec(node.left)

    def inOrder(self, node):
        "prints BST with inorder traversal"
        if not node:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)


bst = BST(10)
bst.insertRec(5)
bst.insertRec(8)
bst.insertRec(3)
bst.insertRec(4)
bst.insertRec(12)
bst.insertRec(6)
bst.insertRec(7)
bst.insertRec(2)
bst.inOrder(bst.root)

print("next val for", bst.root.left.val, ":", bst.findNextRec(bst.root.left).val)
print("next val for", bst.root.left.left.val, ":", bst.findNextRec(bst.root.left.left).val)
print("next val for", bst.root.left.left.left.val, ":", bst.findNextRec(bst.root.left.left.left).val)
print("prev val for", bst.root.left.val, ":", bst.findPrevRec(bst.root.left).val)
print("prev val for", bst.root.left.left.val, ":", bst.findPrevRec(bst.root.left.left).val)
print("prev val for", bst.root.left.right.val, ":", bst.findPrevRec(bst.root.left.right).val)

print("max value:", bst.findMaxRec(bst.root).val)
print("min value:", bst.findMinRec(bst.root).val)