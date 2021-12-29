#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    if len(s) == 1:
        return "YES"
    char_dict = {}
    for c in s:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    list_count = list(char_dict.values())
    list_count.sort()
    print(list_count)
    max_count = max(list_count)
    min_count = min(list_count)
    sum_count = sum(list_count)
    avg_count = float(sum_count/len(list_count))
    avg_of_min_one_count = float((sum_count-1)/len(list_count))
    print(max_count, min_count, sum_count, avg_of_min_one_count)
    
    new_min_count = min(list_count[1:])
    avg_without_min_count = float((sum_count-min_count)/(len(list_count)-1))
    print(new_min_count, avg_without_min_count)
   
    
    if avg_count == float(min_count) or avg_of_min_one_count == float(min_count) or avg_without_min_count == float(new_min_count):
      return "YES"
            
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
