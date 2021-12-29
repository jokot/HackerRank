#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        checker = count
        for j,e in enumerate(a[:-1]):
            if e>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
        if checker == count:
            break
        
    print("Array is sorted in",count,"swaps.")
    print("First Element:",min(a))
    print("Last Element:", max(a))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
