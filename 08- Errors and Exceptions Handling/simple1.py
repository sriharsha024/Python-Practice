"""
=============================================================================
SIMPLE EXCEPTION HANDLING DEMONSTRATION
=============================================================================
This module demonstrates basic exception handling in Python.

Concepts covered:
- Using try and except blocks to handle runtime errors
- Handling ZeroDivisionError safely
- Using finally to execute cleanup or final statements
- Writing clean, readable, and pylint-compliant code
=============================================================================
"""

# ---------------------------------------------------------------------------
# NOTE:
# The commented code below shows simple variable assignment and printing.
# It is kept inside a multiline comment for reference purposes only.
# ---------------------------------------------------------------------------
"""
a = 10
b = 24
print(a)
print(b)
"""


# ---------------------------------------------------------------------------
# CONSTANT VARIABLE DEFINITIONS
# ---------------------------------------------------------------------------
# Constants are written in uppercase as per Python style guidelines
A = 10
B = 0


# ---------------------------------------------------------------------------
# EXCEPTION HANDLING USING TRY / EXCEPT / FINALLY
# ---------------------------------------------------------------------------
try:
    # Attempting a division operation that may cause an error
    RESULT = A / B
    print("Result:", RESULT)

except ZeroDivisionError:
    # This block executes if division by zero occurs
    print("Error: Division by zero is not allowed.")

finally:
    # This block always executes, regardless of whether an error occurs
    print("Execution completed.")
