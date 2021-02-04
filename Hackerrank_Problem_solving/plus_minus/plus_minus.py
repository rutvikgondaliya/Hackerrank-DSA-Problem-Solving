#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_count, neg_count, zero_count = 0, 0, 0
    num = 0
    # while loop
    while(num < len(arr)):
    # check
        if arr[num] > 0:
            pos_count += 1
        elif arr[num] == 0:
            zero_count += 1
        else:
            neg_count += 1
        # increment num
        num += 1
    total_pos = pos_count / n
    total_zero = zero_count / n
    total_neg = neg_count / n
    print('%.6f'%total_pos)
    print('%.6f'%total_neg)
    print('%.6f'%total_zero)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
