
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    i=0
    magazine_dict = listStringToDictInt(magazine)
    note_dict = listStringToDictInt(note)
    status = "Yes"
    for word, count in list(note_dict.items()):
        if word in magazine_dict:
            if count > magazine_dict[word]:
                status = "No"
                break
        else:
            status = "No"
            break
    print(status)

def listStringToDictInt(string):
    dict_int={}
    for s in string:
        if s not in dict_int:
            dict_int[s] = 1
        else:
            dict_int[s] += 1
    return dict_int


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
