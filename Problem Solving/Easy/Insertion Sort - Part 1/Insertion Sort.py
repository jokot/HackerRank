
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    i = len(arr)-1
    while i > 0 and arr[i] < arr[i-1]:
        copyArr = arr.copy()
        copyArr[i] = arr[i-1]
        print(*copyArr)
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
