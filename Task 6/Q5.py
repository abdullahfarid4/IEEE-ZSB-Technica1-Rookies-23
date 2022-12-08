#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    sss = 'hackerrank'
    j = len(sss)
    for i in range(len(s) - 1, -1, -1):
        if sss[j - 1] == s[i]:
            j -= 1
        if j == 0:
            return "YES"
    if i == 0:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
