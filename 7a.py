# Problem 7 Part A

import avl as av
import bst as bs
import genarray as ga
import node as nd
import datetime as dt

avl2 = av.AVL(None)
bst2 = bs.BST(None)
arr2 = ga.getSortedArray(10000)

print("Doing BST now...")
bstStart = dt.datetime.now()
for val in arr2:
    bst2.insertIter(val)

for val in arr2:
    bst2.deleteIter(val)
bstFinish = dt.datetime.now()
bstTime = bstFinish-bstStart
print("BST took", bstTime, "seconds")

print("Doing AVL now...")
avlStart = dt.datetime.now()
for val in arr2:
    avl2.insertIter(val)

for val in arr2:
    avl2.deleteIter(val)
avlFinish = dt.datetime.now()
avlTime = avlFinish-avlStart
print("AVL took", avlTime, "seconds")