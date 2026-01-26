"""
=============================================================================
LAMBDA EXPRESSIONS AND FUNCTIONAL PROGRAMMING
=============================================================================
This module demonstrates:
- Traditional function definitions with map()
- Filter operations with custom functions
- Lambda expressions (anonymous functions)
- Using lambda with map() and filter()
=============================================================================
"""


# ============================================================================
# 1. MAP WITH CUSTOM FUNCTION - SQUARE NUMBERS
# ============================================================================
def square(num):
    """
    Returns the square of a number.
    
    Args:
        num (int/float): The number to square
        
    Returns:
        int/float: The squared value
    """
    return num * num


my_nums = [1, 2, 3, 4, 5]

# Using map() to apply square function to each element
print("--- Using map() with custom function ---")
for item in map(square, my_nums):
    print(item)  # Output: 1, 4, 9, 16, 25

# Convert map object to list
my_list = list(map(square, my_nums))
print(my_list)  # Output: [1, 4, 9, 16, 25]


# ============================================================================
# 2. MAP WITH CONDITIONAL LOGIC - STRING PROCESSING
# ============================================================================
def splicer(mystring):
    """
    Returns "EVEN" if string length is even, otherwise returns first character.
    
    Args:
        mystring (str): The string to process
        
    Returns:
        str: "EVEN" if length is even, first character otherwise
    """
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


names = ["Andy", "Johan", "Sally"]

# Apply splicer function to each name using map()
my_list_1 = list(map(splicer, names))
print("\n--- Using map() with conditional function ---")
print(my_list_1)  # Output: ['A', 'EVEN', 'S']
# 'Andy' (4 chars, even) -> 'EVEN'
# 'Johan' (5 chars, odd) -> 'J'
# 'Sally' (5 chars, odd) -> 'S'


# ============================================================================
# 3. FILTER WITH CUSTOM FUNCTION - FIND EVEN NUMBERS
# ============================================================================
def check_even(num):
    """
    Checks if a number is even.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if even, False if odd
    """
    return num % 2 == 0


my_nums_1 = [9, 2, 6, 8, 7, 5, 3, 12]

# Use filter() to keep only even numbers
even_nos = list(filter(check_even, my_nums_1))
print("\n--- Using filter() with custom function ---")
print(even_nos)  # Output: [2, 6, 8, 12]


# ============================================================================
# 4. LAMBDA EXPRESSIONS - ANONYMOUS FUNCTIONS
# ============================================================================
print("\n--- Using lambda with map() ---")
# Lambda syntax: lambda arguments: expression
# Square numbers using lambda instead of defining a separate function
print(list(map(lambda x: x * x, [5, 6, 9, 8, 7, 2])))
# Output: [25, 36, 81, 64, 49, 4]

print("\n--- Using lambda with filter() ---")
# Filter even numbers using lambda instead of defining a separate function
print(list(filter(lambda x: x % 2 == 0, [9, 2, 6, 8, 7, 5, 3, 12])))
# Output: [2, 6, 8, 12]

print("\n--- Using lambda with map() - String Reversal ---")
# Reverse each string in a list using lambda with slicing notation [::-1]
print(list(map(lambda x: x[::-1], ["Andy", "Johan", "Sally"])))
# Output: ['ydnA', 'nahoJ', 'yllaS']