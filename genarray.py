import random

def getRandomArray(n):
    '''returns array of size n containing random unique values'''
    tempset = set()
    retarr = []
    while len(retarr) < n:
        r = random.randint(0,n*10)
        if n not in tempset:
            tempset.add(r)
            retarr.append(r)
    return retarr

def getSortedArray(n):
    '''return array of size n with integers from n to 1'''
    return [n-i for i in range(n)]