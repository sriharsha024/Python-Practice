"""
=============================================================================
STRING CAPITALIZATION FUNCTIONS
=============================================================================
This module contains functions used to capitalize strings.
It is designed to be tested using Python's unittest framework.

Functions:
- cap_test   : Capitalizes only the first character of the string
- cap_test_1 : Capitalizes the first character of every word in the string
=============================================================================
"""


def cap_test(txt):
    """
    Capitalizes only the first character of the given string.

    Args:
        txt (str): Input string

    Returns:
        str: String with only the first character capitalized
    """
    return txt.capitalize()


def cap_test_1(txt):
    """
    Capitalizes the first character of every word in the given string.

    Args:
        txt (str): Input string containing one or more words

    Returns:
        str: String with each word capitalized
    """
    return txt.title()
