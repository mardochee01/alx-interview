#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n) -> int:
    """write a method that calculates
    the fewest number of operations
    Prototype: def minOperations(n)
    Returns an integer If n is impossible
    to achieve return 0"""
    if n <= 0 and type(n) is not int:
        return 0

    text = 2
    op = 0
    while (text <= n):
        if not (n % text):
            n = int(n / text)
            op += text
            text = 1
        text += 1
    return op
