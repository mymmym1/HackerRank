#!/bin/python3

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
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    for i in arr:
        if i > 0:
            positiveCount += 1
        elif i < 0:
            negativeCount += 1
        elif i == 0:
            zeroCount += 1
    n = len(arr)
    positiveRate = positiveCount / n
    negativeRate = negativeCount / n
    zeroRate = zeroCount / n
    print(format(positiveRate,".6f"))
    print(format(negativeRate,".6f"))
    print(format(zeroRate,".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
