#!/usr/bin/python3
""" UTF-8 Validation
"""


def validUTF8(data):
    """ determines if a given data set represents
    a valid UTF-8 encoding.
    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding
    - Return: False if data is not a valid UTF-8 encoding
    """
    n_bytes = 0

    dataB = 1 << 7
    dataJ = 1 << 6

    for i in data:

        mbytes = 1 << 7

        if n_bytes == 0:
            while mbytes & i:
                n_bytes += 1
                mbytes = mbytes >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (i & dataB and not (i & dataJ)):
                    return False

        n_bytes -= 1

    if n_bytes == 0:
        return True

    return False
