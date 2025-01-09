#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    dict_count, dict_index = stringToDict(s)
    count = 0
    for k,v in list(dict_count.items()):
        if v > 1 :
            n = v-1
            count += ((n*n) + n) // 2
        
    
    for k,v in list(dict_index.items()):
        if dict_count[k] > 1:
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    if v[j] - v[i] > 1:
                        count += 1
    
    
    return count

def stringToDict(s):
    dict_count = {}
    dict_index = {}
    char_index = 0
    for c in s:
        if c in dict_count:
            dict_count[c] += 1
            dict_index[c].append(char_index)
        else:
            dict_count[c] = 1
            dict_index[c] = [char_index]
        char_index += 1
        
    return (dict_count, dict_index)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
