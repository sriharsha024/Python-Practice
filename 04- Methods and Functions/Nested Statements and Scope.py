"""
=============================================================================
NESTED STATEMENTS AND SCOPE (LEGB RULE)
=============================================================================
This module demonstrates Python's variable scoping rules:

LEGB Rule determines the order of variable lookup:
1. Local - Variables defined in the current function
2. Enclosing - Variables in outer functions (nested functions)
3. Global - Variables defined at module/script level
4. Built-in - Python's built-in namespace (len, print, etc.)

This helps understand how Python resolves variable names.
=============================================================================
"""


# ============================================================================
# EXAMPLE 1: LOCAL SCOPE
# ============================================================================
print("=== EXAMPLE 1: LOCAL SCOPE ===")

x = 25  # Global scope

def printer():
    """
    Function with local variable x.
    The local x=50 shadows the global x=25 within this function.
    """
    x = 50  # Local scope
    return x


print(x)            # Output: 25 (global x)
print(printer())    # Output: 50 (local x inside function)


# ============================================================================
# EXAMPLE 2: LAMBDA AND LOCAL SCOPE
# ============================================================================
print("\n=== EXAMPLE 2: LAMBDA (LOCAL SCOPE) ===")

# Lambda creates its own local scope
square = lambda num: num ** 2
print(square(5))  # Output: 25


# ============================================================================
# EXAMPLE 3: NESTED FUNCTION - LOCAL VARIABLES
# ============================================================================
print("\n=== EXAMPLE 3: NESTED FUNCTION - LOCAL VARIABLES ===")

name = 'THIS IS A GLOBAL STRING'  # Global scope

def greet():
    """
    Outer function with local variable 'name'.
    Inner function 'hello' has its own local 'name' that shadows the outer one.
    """
    name = 'SAMMY'  # Outer function's local scope
    
    def hello():
        """Inner function with its own local 'name'."""
        name = "JOHN DOE"  # This local name shadows the enclosing 'name'
        print('Hello ' + name)
    
    hello()


greet()  # Output: Hello JOHN DOE


# ============================================================================
# EXAMPLE 4: ENCLOSING SCOPE (NESTED FUNCTIONS)
# ============================================================================
print("\n=== EXAMPLE 4: ENCLOSING SCOPE ===")

def greet():
    """
    Outer function defines 'name' in its local scope.
    Inner function 'hello' can access enclosing function's variable without redefining it.
    This is the ENCLOSING scope.
    """
    name = 'SAMMY'  # Enclosing function's local scope
    
    def hello():
        """
        Inner function accesses 'name' from enclosing function.
        Since 'name' is not defined here, Python looks in the enclosing scope.
        """
        print('Hello ' + name)  # Uses 'name' from enclosing scope
    
    hello()


greet()  # Output: Hello SAMMY


# ============================================================================
# EXAMPLE 5: GLOBAL SCOPE
# ============================================================================
print("\n=== EXAMPLE 5: GLOBAL SCOPE ===")

def greet():
    """
    Outer function does NOT define 'name' locally.
    Inner function 'hello' looks for 'name' in:
    1. Local scope (not found)
    2. Enclosing scope (not found)
    3. Global scope (found!)
    """
    # name = 'SAMMY'  # Commented out - not defined here
    
    def hello():
        """
        Inner function looks for 'name'.
        Since it's not in local or enclosing scope, uses global 'name'.
        """
        print('Hello ' + name)  # Uses 'name' from global scope
    
    hello()


greet()  # Output: Hello THIS IS A GLOBAL STRING


# ============================================================================
# EXAMPLE 6: GLOBAL KEYWORD - MODIFYING GLOBAL VARIABLES
# ============================================================================
print("\n=== EXAMPLE 6: GLOBAL KEYWORD - MODIFY GLOBAL ===")

x = 50  # Global variable

def func():
    """
    Function that uses the 'global' keyword to modify the global variable.
    Without 'global', assignment creates a local variable instead.
    With 'global', we can modify the variable in the global scope.
    """
    global x  # Declare that we want to use the global x
    print(f'X is {x}')  # Output: X is 50

    x = 200  # This modifies the GLOBAL x, not a local variable
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')  # Output: X is 200


print(x)  # Output: 50 (original global value)
func()    # Modifies global x to 200
print(x)  # Output: 200 (global x was changed)


# ============================================================================
# EXAMPLE 7: ALTERNATIVE - FUNCTION PARAMETERS (SAFER APPROACH)
# ============================================================================
print("\n=== EXAMPLE 7: PARAMETER-BASED APPROACH (SAFER) ===")

x = 50  # Global variable

def func(x):
    """
    Alternative approach: pass the global variable as a parameter.
    This is safer than using 'global' keyword because:
    - No side effects on global state
    - Function is more reusable and testable
    - Code behavior is explicit
    """
    print(f'X is {x}')  # Output: X is 50

    x = 200  # This only modifies the local parameter, not global x
    print(f'I JUST LOCALLY CHANGED X TO {x}')  # Output: X is 200
    return x  # Return the modified value


print(x)      # Output: 50 (global x unchanged)
x = func(x)   # Pass x as argument, capture returned value
print(x)      # Output: 200 (global x is updated via assignment)