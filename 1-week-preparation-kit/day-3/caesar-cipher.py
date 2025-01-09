#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    minUp = ord("A")-1
    maxUp = ord("Z")
    minLow = ord("a")-1
    maxLow = ord("z")
    k = k%(maxLow-minLow)
    newString = ""
    for c in s:
        if c.isalpha():
            valueC = ord(c)
            if c.isupper():
                if (valueC+k <= maxUp):
                    newString += chr(valueC+k)
                else:
                    newString += chr(valueC+k-maxUp+minUp)
            else:
                if (valueC+k <= maxLow):
                    newString += chr(valueC+k)
                else:
                    newString += chr(valueC+k-maxLow+minLow)
        else:
            newString += c
    return newString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
