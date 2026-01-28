"""
=============================================================================
EXCEPTION HANDLING IN PYTHON - TRY / EXCEPT / ELSE / FINALLY
=============================================================================
This script demonstrates:
- Handling invalid input using try-except
- Using else and finally blocks
- File handling with exception safety
- Continuously asking user input until valid data is entered
=============================================================================
"""


# ============================================================================
# 1. FUNCTION WITH TRY / EXCEPT / ELSE
# ============================================================================
def add(num1, num2):
    """
    Adds two numbers and handles invalid input gracefully.

    Args:
        num1 (int): First number
        num2 (int): Second number

    Demonstrates:
    - try block for risky operations
    - except block for error handling
    - else block for successful execution
    """
    try:
        print("Result:", num1 + num2)
    except TypeError:
        print("Invalid input! Please provide numbers only.")
    else:
        print("Addition completed successfully.")


# Taking user input
num1 = 10
num2 = int(input("Enter a number: "))

add(num1, num2)


# ============================================================================
# 2. FILE HANDLING WITH MULTIPLE EXCEPT BLOCKS
# ============================================================================
try:
    # Open file in write mode
    f = open("08- Errors and Exceptions Handling/testfile.txt", "w")
    f.write("Hi Hello")

    # Move cursor to beginning and read content
    f.seek(0)
    content = f.read()
    print("File Content:", content)

except TypeError:
    print("Type error occurred while working with the file.")
except OSError:
    print("OS error occurred (file handling issue).")
finally:
    print("File operation attempt completed (finally block always runs).")


# ============================================================================
# 3. CONTINUOUS USER INPUT WITH EXCEPTION HANDLING
# ============================================================================
def ask_for_input():
    """
    Continuously asks the user for a number until valid input is given.
    
    Demonstrates:
    - Infinite loop with while True
    - Generic exception handling
    - else block when input is valid
    - finally block that always executes
    """
    while True:
        try:
            result = int(input("Enter a number: "))
        except:
            print("Oops! That was not a valid number.")
        else:
            print("Thank you! You entered:", result)
            break  # Exit loop after successful input
        finally:
            print("Input attempt finished.\n")


# Call the function
ask_for_input()
