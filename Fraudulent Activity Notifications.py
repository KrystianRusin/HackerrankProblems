import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    numOfNotifications = 0
    count = d

    tExpenditures = expenditure[:d]
    tExpenditures = sorted(tExpenditures)
    median = findMedian(tExpenditures,d)

    if expenditure[d] >= (2*median):

        numOfNotifications += 1

    for i in range(d, len(expenditure)):

        if(i >= (len(expenditure)-1)):
            break

        del tExpenditures[bisect.bisect_left(tExpenditures,expenditure[i-d])]
        bisect.insort(tExpenditures, expenditure[i])
        median = findMedian(tExpenditures, d)

        if expenditure[count+1] >= (2*median):

            numOfNotifications += 1

        count += 1

    return numOfNotifications


def findMedian(expenditure, d):
    if d%2 != 0:
        return expenditure[d//2]
    else:
       return (expenditure[d//2] + expenditure[(d//2)-1])/2




nd = input().split()

#Number of days total
n = int(nd[0])

#Number of trailing days
d = int(nd[1])

#Expenditures of size D
expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)

print(result)


