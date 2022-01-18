import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    for a in arr:
        if a == 0:
            zero += 1
        elif a > 0:
            positive += 1
        else:
            negative += 1
    print(format(positive/len(arr),'.6f'))
    print(format(negative/len(arr),'.6f'))
    print(format(zero/len(arr),'.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
