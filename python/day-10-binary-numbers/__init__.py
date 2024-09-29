#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    base2 = bin(n).__str__()[2:]
    highest = 0
    count = 0

    for i in range(len(base2)):
        if base2[i] == '1':
            count += 1
            highest = max(highest, count)
        else:
            count = 0
    print(highest)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
