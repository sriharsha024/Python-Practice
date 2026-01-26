"""
=============================================================================
FUNCTION PRACTICE EXERCISES - PART 2
=============================================================================
This module contains practice functions demonstrating:
- Character classification and counting
- Set operations for finding unique elements
- String analysis (pangram detection)
- Built-in Python functions and methods
=============================================================================
"""

import string


# ============================================================================
# 1. UPPER/LOWER CASE COUNTER
# ============================================================================
def upper_lower(mystring):
    """
    Counts the number of uppercase and lowercase characters in a string.
    Non-alphabetic characters are ignored.
    
    Args:
        mystring (str): The string to analyze
        
    Prints:
        Number of uppercase characters
        Number of lowercase characters
    """
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in mystring:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    # Display results
    print("No. of upper case chars: " + str(upper_count))
    print("No. of lower case chars: " + str(lower_count))


# Test the function
upper_lower("Hi Hello")
# Output:
# No. of upper case chars: 2
# No. of lower case chars: 6


# ============================================================================
# 2. FIND UNIQUE ELEMENTS IN LIST
# ============================================================================
def unique_list(nums):
    """
    Returns a list of unique elements from a list.
    Uses set to eliminate duplicates.
    
    Args:
        nums (list): List that may contain duplicate elements
        
    Returns:
        list: List with only unique elements (order may change)
    """
    return list(set(nums))


# Test the function
print(unique_list([12, 12, 3, 4, 6, 7, 1, 3, 45, 66, 6, 7]))
# Output: List with unique elements (order varies)


# ============================================================================
# 3. PANGRAM DETECTOR
# ============================================================================
def is_pangram(sentence):
    """
    Checks if a sentence is a pangram.
    A pangram contains at least one instance of every letter in the alphabet.
    
    Args:
        sentence (str): The sentence to check
        
    Returns:
        bool: True if pangram, False otherwise
    """
    # Get all lowercase letters of the English alphabet
    alphabet = string.ascii_lowercase
    
    # Convert sentence to lowercase for comparison
    sentence = sentence.lower()
    
    # Check if each letter of the alphabet is in the sentence
    for letter in alphabet:
        if letter not in sentence:
            return False
    
    return True


# Test the function
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(is_pangram("Hello World"))                                  # Output: False
