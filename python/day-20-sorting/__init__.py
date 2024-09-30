#!/bin/python3

import math
import os
import random
import re
import sys

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def bubble_sort(a):
    swap_count = 0
    swapped = False
    n = len(a)
    
    while True:
        swapped = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j+ 1)
                swap_count += 1
                swapped = True
        if not swapped:
            break
    
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    return a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    bubble_sort(a)

