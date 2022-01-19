#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    if len(a) == 1:
        return a[0]
    else:
        if not a[-1] == a[-2]:
            return a[-1]
        for i in range(len(a)-1):
            if i > 0:
                if not (a[i] == a[i+1]) and not (a[i] == a[i-1]):
                    return a[i]
            else:
                if not a[i] == a[i+1]:
                    return a[i]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
