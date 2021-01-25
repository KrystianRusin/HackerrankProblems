import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def lilysHomework(arr):
    l = len(arr)
    rArr = arr.copy()
    swaps = 0
    rswaps = 0
    sortedArr = sorted(arr)
    rSortedArr = sorted(rArr, key=None, reverse=True)


    if (arr == sortedArr or arr == rSortedArr):
        return swaps

    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i

    for i in range(len(arr)):

        if arr[i] != sortedArr[i]:

            swaps += 1

            iswap = d[sortedArr[i]]
            d[arr[i]] = d[sortedArr[i]]
            arr[i], arr[iswap]  = sortedArr[i], arr[i]



    dReverse = {}
    for i in range(len(rArr)):
        dReverse[rArr[i]] = i


    for i in range(len(rArr)):

        if rArr[i] != rSortedArr[i]:
            rswaps+=1

            iswapr = dReverse[rSortedArr[i]]
            dReverse[rArr[i]] = dReverse[rSortedArr[i]]
            rArr[i], rArr[iswapr] = rSortedArr[i], rArr[i]

    
    return min(swaps,rswaps)




n = int(input())

arr = list(map(int, input().rstrip().split()))

result = lilysHomework(arr)
print(result)