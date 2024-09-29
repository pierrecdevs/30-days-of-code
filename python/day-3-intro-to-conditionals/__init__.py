#!/bin/python3

import math
import os
import random
import re
import sys


def isOdd(n: int) -> bool:
    """
    Helper function to check if a number is odd
    :param n: The number to check
    :return: True if the number is odd, False otherwise
    """
    return n % 2 == 1


def isWeird(n: int) -> bool:
    """
    Determine if a number is considered "Weird"
    :param n: The number to check
    :return: True if the number is "Weird" based on the following AC:
        - AC 1: n is odd
        - AC 2: n is even, and in inclusive range of [6, 20]
    """
    return isOdd(n) or (6 <= n <= 20)

if __name__ == '__main__':
    N = int(input().strip())
    print("Weird" if isWeird(N) else "Not Weird")

    # Time Complexity: O(1)
    # Space Complexity: O(1)
