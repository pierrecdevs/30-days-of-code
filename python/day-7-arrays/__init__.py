#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr, src, dst):
    temp = arr[src]
    arr[src] = arr[dst]
    arr[dst] = temp
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # Method 1 - built in methods
    # arr.reverse()
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # Methond 2 - slicing
    rev = arr[::-1]
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Method 3 - reversed
    # rev = list((reversed(arr)))
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # print(' '.join(map(str, arr)))
    print(' '.join(map(str, rev)))

    # Time Complexity: O(n)
    # Space Complexity: O(n)
