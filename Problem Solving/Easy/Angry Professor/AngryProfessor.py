
import math
import os
import random
import re
import sys


def angryProfessor(k, a):

    notLate = len([x for x in a if x <= 0])

    return "YES" if notLate < k else "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result + '\n')

        # fptr.write(result + '\n')

    # fptr.close()
