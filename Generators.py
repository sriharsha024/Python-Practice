"""
=============================================================================
GENERATORS AND ITERATORS IN PYTHON
=============================================================================
This module demonstrates:
- Normal functions vs generator functions
- Using yield instead of return
- Memory-efficient sequence generation
- Fibonacci generator
- Using next() and iter()
- Generator examples with squares and random numbers
=============================================================================
"""


# ============================================================================
# 1. NORMAL FUNCTION (RETURNS LIST)
# ============================================================================
def create_cubes_1(n):
    """
    Creates and returns a list containing cubes of numbers from 0 to n-1.

    Args:
        n (int): Number of values to generate

    Returns:
        list: List of cubes
    """
    result = []

    for x in range(n):
        result.append(x ** 3)

    return result


cubes_list = create_cubes_1(10)
print("Cubes using normal function:", cubes_list)


# ============================================================================
# 2. GENERATOR FUNCTION (USES YIELD)
# ============================================================================
def create_cubes_2(n):
    """
    Generator that yields cubes of numbers from 0 to n-1.
    Uses yield instead of building a full list.

    Args:
        n (int): Number of values to generate
    """
    for x in range(n):
        yield x ** 3


print("\nGenerator object:", create_cubes_2(10))
print("Cubes using generator:", list(create_cubes_2(10)))


# ============================================================================
# 3. FIBONACCI GENERATOR
# ============================================================================
def gen_fib(n):
    """
    Generates first n Fibonacci numbers.

    Args:
        n (int): Number of Fibonacci terms
    """
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


print("\nFirst 10 Fibonacci numbers:")
for num in gen_fib(10):
    print(num)


# ============================================================================
# 4. SIMPLE GENERATOR AND next()
# ============================================================================
def simple_gen():
    """
    Simple generator yielding numbers from 0 to 2.
    """
    for x in range(3):
        yield x


g = simple_gen()
print("\nGenerator object:", g)

print("Using next():")
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # Uncommenting this will raise StopIteration


# ============================================================================
# 5. ITERATORS WITH STRINGS
# ============================================================================
s = "hello"

# Strings are iterable but not iterators
# print(next(s))  # ❌ Error

s_iter = iter(s)
print("\nIterating through string using iter() and next():")
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


# ============================================================================
# 6. GENERATOR FOR SQUARES
# ============================================================================
def gen_squares(n):
    """
    Generates squares of numbers from 0 to n-1.

    Args:
        n (int): Upper limit
    """
    for x in range(n):
        yield x ** 2


print("\nSquares using generator:")
for x in gen_squares(10):
    print(x)


# ============================================================================
# 7. RANDOM NUMBER GENERATOR
# ============================================================================
import random

def rand_num(low, high, n):
    """
    Generates n random integers between low and high (inclusive).

    Args:
        low (int): Lower bound
        high (int): Upper bound
        n (int): Number of random values
    """
    for _ in range(n):
        yield random.randint(low, high)


print("\nRandom numbers:")
for num in rand_num(1, 50, 20):
    print(num)
