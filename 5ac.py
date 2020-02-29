# Problem 5 Part A

import avl as av
import bst as bs
import genarray as ga

avl = av.AVL(None)
bst = bs.BST(None)
arr = ga.getRandomArray(10000)

print("Constructing AVL tree iteratively and BST recursively...")
for val in arr:
    avl.insertIter(val)
    bst.insertRec(val)

# Problem 5 Part C

avl2 = av.AVL(None)
bst2 = bs.BST(None)
arr = ga.getRandomArray(10000)

print("Constructing AVL tree iteratively and BST iteratively...")
for val in arr:
    avl2.insertIter(val)
    bst2.insertIter(val)