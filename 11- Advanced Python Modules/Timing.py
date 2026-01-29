"""
=============================================================================
PERFORMANCE COMPARISON - LIST COMPREHENSION vs MAP()
=============================================================================
This script demonstrates:
- Two ways to convert numbers to strings
- Measuring execution time using time module
- Accurate benchmarking using timeit module
- Understanding performance differences in Python
=============================================================================
"""

import time
import timeit


# ============================================================================
# 1. FUNCTION USING LIST COMPREHENSION
# ============================================================================
def func_one(n):
    """
    Converts numbers from 0 to n-1 into strings
    using list comprehension.

    Args:
        n (int): Upper limit

    Returns:
        list: List of string numbers
    """
    return [str(num) for num in range(n)]


# ============================================================================
# 2. FUNCTION USING map()
# ============================================================================
def func_two(n):
    """
    Converts numbers from 0 to n-1 into strings
    using map() function.

    Args:
        n (int): Upper limit

    Returns:
        list: List of string numbers
    """
    return list(map(str, range(n)))


# ============================================================================
# 3. FUNCTION OUTPUT COMPARISON
# ============================================================================
print("Output using list comprehension:")
print(func_one(10))

print("\nOutput using map():")
print(func_two(10))


# ============================================================================
# 4. PERFORMANCE TEST USING time MODULE (ROUGH MEASUREMENT)
# ============================================================================
print("\n=== Performance Test using time module ===")

start_time_1 = time.time()
result_1 = func_one(10_000_000)
end_time_1 = time.time()
print("Time taken by func_one:", end_time_1 - start_time_1)

start_time_2 = time.time()
result_2 = func_two(10_000_000)
end_time_2 = time.time()
print("Time taken by func_two:", end_time_2 - start_time_2)


# ============================================================================
# 5. ACCURATE BENCHMARKING USING timeit MODULE
# ============================================================================
print("\n=== Performance Test using timeit module ===")

stmt_1 = '''
func_one(100)
'''
setup_1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

time_func_one = timeit.timeit(stmt_1, setup_1, number=1_000_000)
print("func_one time (list comprehension):", time_func_one)


stmt_2 = '''
func_two(100)
'''
setup_2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

time_func_two = timeit.timeit(stmt_2, setup_2, number=1_000_000)
print("func_two time (map):", time_func_two)
