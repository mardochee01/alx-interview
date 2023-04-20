#!/usr/bin/python3
"""
Auteur: Mardochée GNERAN
Function: Pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    """
    a = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        a.append([x+y for x, y in zip([0]+a[i-1], a[i-1]+[0])])
    return a[:n]
