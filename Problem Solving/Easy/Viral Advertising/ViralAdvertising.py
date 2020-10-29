import math
import os
import random
import re
import sys


def viralAdvertising(n):
    day = n
    shared = 5
    liked = 0
    comulative = 0

    for i in range(day):
        liked = shared//2
        shared = liked * 3
        comulative += liked


    return comulative

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')

    # fptr.write(str(result) + '\n')

    # fptr.close()
