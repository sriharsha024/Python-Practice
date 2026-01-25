"""
=============================================================================
*ARGS AND **KWARGS DEMONSTRATION
=============================================================================
This module demonstrates:
- Default parameters
- *args (non-keyword arguments)
- **kwargs (keyword arguments)
- Combining both *args and **kwargs
=============================================================================
"""


# ============================================================================
# 1. FUNCTION WITH DEFAULT PARAMETERS
# ============================================================================
def myfunc(a, b, c=0, d=0):
    """
    Calculates 5% of the sum of four numbers.
    Parameters c and d have default values of 0.
    
    Args:
        a (int/float): First required parameter
        b (int/float): Second required parameter
        c (int/float): Third parameter with default value 0
        d (int/float): Fourth parameter with default value 0
        
    Returns:
        float: 5% of the sum of all parameters
    """
    return sum((a, b, c, d)) * 0.05


print(myfunc(40, 60, 100, 100))  # Output: 15.0


# Error case (uncommenting would cause TypeError: too many positional arguments):
# print(myfunc(40, 60, 20, 3, 0))


# ============================================================================
# 2. *ARGS - ACCEPT VARIABLE NUMBER OF POSITIONAL ARGUMENTS
# ============================================================================
def myfunc_1(*args):
    """
    Accepts any number of positional arguments.
    *args collects all positional arguments as a tuple.
    Calculates 5% of the sum of all arguments.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        float: 5% of the sum of all arguments
    """
    return sum(args) * 0.05


print(myfunc_1(40, 60, 100, 300))   # Output: 15.0 (sum: 300)
print(myfunc_1(40, 60, 20, 3, 0))   # Output: 6.15 (sum: 123)


# ============================================================================
# 3. *ARGS - PRINT ARGUMENTS AS TUPLE
# ============================================================================
def myfunc_2(*args):
    """
    Demonstrates how *args collects arguments into a tuple.
    Prints the tuple of all provided arguments.
    
    Args:
        *args: Variable number of arguments (any type)
    """
    print(args)


myfunc_2(1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)
myfunc_2('a', 'b', 'c')   # Output: ('a', 'b', 'c')


# ============================================================================
# 4. **KWARGS - ACCEPT VARIABLE NUMBER OF KEYWORD ARGUMENTS
# ============================================================================
def myfunc_3(**kwargs):
    """
    Accepts any number of keyword arguments.
    **kwargs collects all keyword arguments as a dictionary.
    Checks if 'fruit' key exists in the kwargs dictionary.
    
    Args:
        **kwargs: Variable number of keyword arguments
    """
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")


myfunc_3(fruit='apple', veggie='lettuce')  # Output: My fruit of choice is apple
myfunc_3(veggie='lettuce')                  # Output: I did not find any fruit here

# Note: Duplicate keys in kwargs cause SyntaxError or last value wins:
# myfunc_3(fruit='apple', veggie='lettuce', fruit='banana')


# ============================================================================
# 5. COMBINED *ARGS AND **KWARGS
# ============================================================================
def myfunc_4(*args, **kwargs):
    """
    Combines both *args and **kwargs.
    *args collects positional arguments as a tuple.
    **kwargs collects keyword arguments as a dictionary.
    
    Args:
        *args: Variable number of positional arguments
        **kwargs: Variable number of keyword arguments
    """
    print("I would like to eat {} {}".format(args[2], kwargs['food']))


# args: (3, 2, 5, ...)  -> args[2] = 5
# kwargs: {'fruit': 'apple', 'food': 'eggs', 'animal': 'dog'} -> kwargs['food'] = 'eggs'
myfunc_4(3, 2, 5, fruit='apple', food='eggs', animal='dog')  # Output: I would like to eat 5 eggs