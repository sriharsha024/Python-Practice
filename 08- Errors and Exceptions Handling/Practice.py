"""
=============================================================================
EXCEPTION HANDLING PRACTICE - TRY / EXCEPT / FINALLY
=============================================================================
This script demonstrates:
- Handling TypeError in loops
- Handling ZeroDivisionError
- Using try-except-else-finally with user input
- Ensuring program stability without crashing
=============================================================================
"""


# ============================================================================
# 1. HANDLING ERRORS INSIDE A LOOP
# ============================================================================
for i in ['a', 'b', 'c']:
    try:
        # Attempting an invalid mathematical operation
        print(i ** 2)
    except TypeError:
        # Handles error when non-numeric values are used in math operations
        print("Invalid input: cannot perform mathematical operation on a string.")
    finally:
        # This block always executes
        print("End of this loop iteration.\n")


# ============================================================================
# 2. HANDLING DIVISION BY ZERO
# ============================================================================
x = 5
y = 0

try:
    z = x / y
    print(z)
except ZeroDivisionError:
    # Handles division by zero safely
    print("Error: Division by zero is not allowed.")
finally:
    # Always executes regardless of exception
    print("Division attempt completed.\n")


# ============================================================================
# 3. USER INPUT WITH CONTINUOUS VALIDATION
# ============================================================================
def ask():
    """
    Continuously asks the user for a valid integer input.
    Squares the number once valid input is provided.

    Demonstrates:
    - Infinite loop using while True
    - try-except for input validation
    - else block for successful execution
    - finally block that always runs
    """
    while True:
        try:
            x = int(input("Enter a number: "))
            print("Square of the number:", x ** 2)
        except ValueError:
            # Handles invalid (non-numeric) user input
            print("Invalid input. Please enter a valid integer.")
            continue
        else:
            # Executes only when no exception occurs
            print("Thank you. You entered:", x)
            break
        finally:
            # Always executes after each attempt
            print("Input attempt finished.\n")


# Call the function
ask()
