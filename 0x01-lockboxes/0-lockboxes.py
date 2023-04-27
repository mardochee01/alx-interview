#!/usr/bin/python3
"""
SE: Mardochée GNERAN
BY: ALX
INTERVIEW: Lockboxes
"""


def canUnlockAll(boxes):
    """check if boxes can opened"""
    UnlockAll = False
    keys = {0: True}
    n = len(boxes)
    while(True):

        nb = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > nb):
            break

    if nb == len(boxes):
        UnlockAll = True

    return UnlockAll#!/usr/bin/python3
"""
SE: Ikary Ryann
BY: ALX
INTERVIEW: Lockboxes
"""


def canUnlockAll(boxes):
    """check if boxes can opened"""
    UnlockAll = False
    keys = {0: True}
    n = len(boxes)
    while(True):

        nb = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > nb):
            break

    if nb == len(boxes):
        UnlockAll = True

    return UnlockAll
