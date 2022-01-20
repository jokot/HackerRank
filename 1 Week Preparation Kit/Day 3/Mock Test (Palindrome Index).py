#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if len(s) == 1:
        return -1
    elif len(s) ==2 :
        if s[:len(s)//2] == s[len(s)//2:][::-1]:
            return -1
        elif len(s) == 2:
            return 0
    else:
        mid = len(s)//2
        firstIndexSecondString = mid if len(s)%2 == 0 else mid+1
        if s[:mid] == s[firstIndexSecondString:][::-1]:
            return -1
        l = len(s)
        i = 0
        j = l-1
        while i < l:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        newStringI = s[:j]+s[j+1:]
        newStringJ = s[:i]+s[i+1:]
        mid = len(newStringI)//2
        firstIndexSecondString = mid if len(newStringI)%2 == 0 else mid+1
        if newStringI[:mid] == newStringI[firstIndexSecondString:][::-1]:
            return j
        elif newStringJ[:mid] == newStringJ[firstIndexSecondString:][::-1]:
            return i
        else:
            return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
