#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    for i in range(1, n):
        for j in range(n-i):
            if isSpecialSubString(s[j:j+i+1]):
                count +=1
                
    return count+n
        
def isSpecialSubString(s):
    if len(s)%2 != 0:
        midleIndex = int((len(s)/2))
        left = s[:midleIndex]
        right = s[midleIndex+1:]
        return isConsistOfOneCharacter(left+right)
    else:
        return isConsistOfOneCharacter(s)
    
def isConsistOfOneCharacter(s):
    return s == len(s) * s[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
