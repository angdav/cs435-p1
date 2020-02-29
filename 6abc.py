# Problem 6 Part A

# I have modified the bst and avl insert functions in the bst.py and avl.py files respectively, so that they indicate levels traversed by incrementing traversecount

# Problem 6 Part B 

import avl as av
import bst as bs
import genarray as ga
import node as nd

avl = av.AVL(None)
bst = bs.BST(None)
arr = ga.getRandomArray(10000)

print("Testing random array...")
for val in arr:
    avl.insertIter(val)
    bst.insertIter(val)

print("BST total traverses:", bst.traversecount)
print("AVL total traverses:", avl.traversecount)

# Problem 6 Part C

avl2 = av.AVL(None)
bst2 = bs.BST(None)
arr2 = ga.getSortedArray(10000)

print("Testing sorted array...")
for val in arr2:
    avl2.insertIter(val)
    bst2.insertIter(val)

print("BST2 total traverses:", bst2.traversecount)
print("AVL2 total traverses:", avl2.traversecount)

