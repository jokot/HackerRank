

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,len(arr)):
        minIndex = i
        while minIndex > 0 and arr[minIndex] < arr[minIndex-1]:
            arr[minIndex], arr[minIndex-1] = arr[minIndex-1], arr[minIndex]
            minIndex -= 1
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
