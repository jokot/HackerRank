#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    aLen = len(a)
    bLen = len(b)
    shortest = a
    longest = b
    count = bLen + aLen
    if (len(a)>len(b)):
        shortest = b
        longest = a
    matchedS = ""
    for c in shortest:
        index = longest.find(c)
        if index != -1:
            matchedS += c
            longest= longest[:index] + longest[index+1:]

    return count - len(matchedS)*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()