"""
=============================================================================
FUNCTIONS AS OBJECTS, NESTED FUNCTIONS, AND DECORATORS
=============================================================================
This script demonstrates:
- Functions as objects
- Assigning functions to variables
- Nested functions
- Returning functions from functions
- Passing functions as arguments
- Decorators and decorator syntax
=============================================================================
"""


# ============================================================================
# 1. FUNCTIONS ARE OBJECTS
# ============================================================================
def func():
    """
    Simple function that returns an integer.
    """
    return 1


print("Calling func():", func())

# Assigning function to a variable (no parentheses)
x = func
print("Printing function object x:", x)
print("Calling x():", x())


# ============================================================================
# 2. ASSIGNING AND DELETING FUNCTION NAMES
# ============================================================================
def hello():
    """
    Returns a greeting string.
    """
    return "Hello"


print("Calling hello():", hello())

greet = hello
print("Calling greet():", greet())

# Delete original function name
del hello

# hello() would cause an error now
# print(hello())

print("Calling greet() after deleting hello():", greet())


# ============================================================================
# 3. NESTED FUNCTIONS (BASIC)
# ============================================================================
def hello_1(name="John"):
    """
    Demonstrates nested functions.
    """
    print("Inside hello_1 function")

    def greet():
        print("Inside greet function")

    def welcome():
        print("Inside welcome function")

    greet()
    welcome()
    print("End of hello_1 function")


hello_1()


# ============================================================================
# 4. RETURNING FUNCTIONS BASED ON CONDITION
# ============================================================================
def hello_2(name="John"):
    """
    Returns a function based on the input name.
    """
    print("Inside hello_2 function")

    def greet():
        print("Hello John")

    def welcome():
        print("Welcome Guest")

    if name == "John":
        return greet
    else:
        return welcome


returned_func = hello_2("John")
print("Returned function:", returned_func)
returned_func()

returned_func = hello_2("Johnn")
print("Returned function:", returned_func)
returned_func()


# ============================================================================
# 5. FUNCTIONS RETURNING FUNCTIONS
# ============================================================================
def cool():
    """
    Returns another function.
    """
    def super_cool():
        return "I am very cool"

    return super_cool


some_func = cool()
print("Calling returned function:", some_func())
print("Function object:", some_func)


# ============================================================================
# 6. PASSING FUNCTIONS AS ARGUMENTS
# ============================================================================
def hello_3():
    """
    Simple greeting function.
    """
    return "Hi Jose"


def other(some_function):
    """
    Accepts another function as an argument and executes it.
    """
    print("Inside other function")
    print("Result from passed function:", some_function())


print("Function object hello_3:", hello_3)
print("Calling hello_3():", hello_3())
other(hello_3)


# ============================================================================
# 7. DECORATORS (MANUAL)
# ============================================================================
def new_decorator(original_func):
    """
    Decorator that adds behavior before and after a function call.
    """
    def wrapper():
        print("Before executing the function")
        original_func()
        print("After executing the function")

    return wrapper


def func_needs_decorator():
    """
    Function without decoration.
    """
    print("This function needs decoration")


print("\nCalling original function:")
func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
print("\nCalling decorated function manually:")
decorated_func()


# ============================================================================
# 8. DECORATORS USING @ SYNTAX
# ============================================================================
@new_decorator
def func_needs_decorator():
    """
    Function decorated using @ syntax.
    """
    print("This function is decorated using @ syntax")


print("\nCalling decorated function using @ syntax:")
func_needs_decorator()
