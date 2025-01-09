#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    count = 0
    for i in range(1, len(arr)):
        minIndex = i
        while minIndex > 0 and arr[minIndex]<arr[minIndex-1]:
            arr[minIndex], arr[minIndex-1] = arr[minIndex-1], arr[minIndex]
            minIndex -= 1
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
