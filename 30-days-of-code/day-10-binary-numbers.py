#!/bin/python3

import math
import os
import random
import re
import sys

def consecutive_binary(n):
    counter = 0
    max_consecutive = 0
    while n>0:
        reminder = n%2
        if reminder == 1:
            counter += 1
        else:
            counter = 0
        max_consecutive = max(counter, max_consecutive)
        n=n//2
    return max_consecutive
    
if __name__ == '__main__':
    n = int(input().strip())
    result = consecutive_binary(n)
    print(result)