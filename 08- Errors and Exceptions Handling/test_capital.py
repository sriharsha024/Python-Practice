"""
=============================================================================
UNIT TESTING FOR STRING CAPITALIZATION
=============================================================================
This module demonstrates unit testing using Python's unittest framework.

Tests covered:
- Single-word capitalization
- Multiple-word capitalization
- Validation of two different capitalization functions

The tests import functions from the capital module and verify correctness.
=============================================================================
"""

import unittest
import capital


class TestCapitalizeTitle(unittest.TestCase):
    """
    Test cases for the cap_test_1 function which uses title casing.
    """

    def test_single_word(self):
        """
        Tests capitalization of a single word.
        """
        text = 'python'
        result = capital.cap_test_1(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        """
        Tests capitalization of multiple words.
        """
        text = 'monty python'
        result = capital.cap_test_1(text)
        self.assertEqual(result, "Monty Python")


class TestCapitalizeFirst(unittest.TestCase):
    """
    Test cases for the cap_test function which capitalizes
    only the first character of the string.
    """

    def test_single_word(self):
        """
        Tests capitalization of a single word.
        """
        text = 'python'
        result = capital.cap_test(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        """
        Tests capitalization of multiple words.
        """
        text = 'monty python'
        result = capital.cap_test(text)
        self.assertEqual(result, "Monty python")


if __name__ == '__main__':
    unittest.main()
