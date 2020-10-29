import math
import os
import random
import re
import sys


def beautifulDays(i, j, k):
    beautifulDay = []
    for n in range(i,j+1):
        # revNumb = reverseNumb(n)
        revNumb = reverseNumbString(n)
        if abs(n-revNumb) % k == 0:
            beautifulDay.append(revNumb)
        
    return len(beautifulDay)

def reverseNumb(n):
    num = n
    tmpNumb = 0
    while(num>0) :
        reminder = num % 10
        tmpNumb = (tmpNumb * 10) + reminder
        num = num // 10
    
    return tmpNumb

# faster reverse number
def reverseNumbString(n):
    stringNumb = str(n)[::-1]
    return int(stringNumb)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')

    # fptr.write(str(result) + '\n')

    # fptr.close()
