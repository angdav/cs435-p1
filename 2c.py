# Problem 2 Part C (Implement Sort Using BST)

import node
import bst

def inOrder(node, arr):
    '''modified inorder traversal that appends to a list instead of printing'''
    if not node:
        return 
    inOrder(node.left, arr)
    arr.append(node.val)
    inOrder(node.right, arr)

def sort(lst):
    '''utilizes BST to sort a given list'''
    if len(lst) < 2:
        return lst
    
    retlst = []
    b = bst.BST(lst[0])

    for val in lst:
        b.insertRec(val)
    
    inOrder(b.root, retlst)
    return retlst

print(sort([5, 4, 2, 6, 8, 4, 3, 4, 6, 3, 2, 50, 34, 23, 12, 35, 645, 765, 34 , 234, 46, 2345, 234, 435]))