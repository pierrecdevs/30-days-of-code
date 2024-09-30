#!/bin/python3

import math
import os
import random
import re
import sys


def hourglass_sum(arr: list) -> int:
    
    max_sum = -63
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            hourglass = top + mid + bot
            max_sum = max(max_sum, hourglass)
    return max_sum

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglass_sum(arr))

    # Time Complexity: O(1)
    # Space Complexity: O(1)

