#!/usr/bin/python3

"""
UTF-8 Validation
"""


def valid_utf8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of integers):
        The data set to be checked for a valid UTF-8 encoding.
        Each integer represents 1 byte of data, so only the 8 least
        significant bits of each integer are considered.

Returns:
bool: True if data is a valid UTF-8 encoding, else False.
    """
    byte_count = 0

    for i in data:
        if byte_count == 0:
            # If the first few bits of the byte
            # indicate a 1 to 4 byte character,
            # set byte_count to the number of bytes minus 1.
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            # If the first bit of the byte is
            # set to 1, it is a continuation byte
            # instead of a first byte, so return False.
            elif i >> 7 == 0b1:
                return False
        else:
            # If the byte is not a continuation byte, return False.
            if i >> 6 != 0b10:
                return False
            # If this is the last byte of the character, decrement byte_count.
            byte_count -= 1
    # If there is no incomplete character at the end, return True.
    return byte_count == 0
