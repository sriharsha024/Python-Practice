"""
=============================================================================
PYTHON FUNCTIONS DEMONSTRATION
=============================================================================
This module demonstrates various function concepts including:
- Basic function definition and calling
- Default parameters
- Return statements
- Recursion
- String manipulation
- List processing
- Tuple unpacking
=============================================================================
"""

# ============================================================================
# BASIC FUNCTION TEMPLATE
# ============================================================================
# Example template for function definition:
# def name_of_function(args):
#     print("This is a function")


# ============================================================================
# 1. FUNCTION WITH DEFAULT PARAMETERS
# ============================================================================
def greet(name="User"):
    """
    Greets the person whose name is passed as an argument.
    If no name is provided, greets with default 'User'.
    
    Args:
        name (str): The name of the person to greet (default: "User")
    """
    print(f"Hello, {name}!")


# Test greet function with and without arguments
greet("John")  # Output: Hello, John!
greet()        # Output: Hello, User!


# ============================================================================
# 2. FUNCTION WITH RETURN STATEMENT
# ============================================================================
def add_function(a, b):
    """
    Returns the sum of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
    """
    return a + b


result = add_function(5, 12)
print(result)  # Output: 17


# ============================================================================
# 3. RECURSIVE FUNCTION - FACTORIAL
# ============================================================================
def factorial(n):
    """
    Calculates the factorial of a given number using recursion.
    Factorial(n) = n * (n-1) * (n-2) * ... * 1
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


fact_result = factorial(5)
print(fact_result)  # Output: 120


# ============================================================================
# 4. STRING MANIPULATION - PALINDROME CHECK
# ============================================================================
def palindrome_check(s):
    """
    Checks if the given string is a palindrome.
    A palindrome reads the same forwards and backwards (ignoring spaces/case).
    
    Args:
        s (str): String to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    s = s.replace(" ", "").lower()  # Normalize: remove spaces, convert to lowercase
    return s == s[::-1]  # Compare string with its reverse


palindrome_result = palindrome_check("A man a plan a canal Panama")
print("The palindrome_result is:", palindrome_result)  # Output: True

palindrome_result_1 = palindrome_check("1236321")
print("The palindrome_result_1 is:", palindrome_result_1)  # Output: True


# ============================================================================
# 5. ITERATIVE FUNCTION - FIBONACCI SEQUENCE
# ============================================================================
def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


fib_result = fibonacci(9)
print(fib_result)  # Output: 34


# ============================================================================
# 6. PRIME NUMBER CHECKER
# ============================================================================
def is_prime(num):
    """
    Checks if a number is prime.
    A prime number is only divisible by 1 and itself.
    
    Args:
        num (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_result = is_prime(29)
print("The prime result is:", prime_result)  # Output: True

prime_result_1 = is_prime(15)
print("The prime result is:", prime_result_1)  # Output: False


# ============================================================================
# 7. LIST PROCESSING - EVEN/ODD SEPARATOR
# ============================================================================
def even_odd_check_list(num_list):
    """
    Separates numbers into even and odd lists.
    
    Args:
        num_list (list): List of numbers to process
        
    Returns:
        list: List of even numbers
    """
    even_list = []
    odd_list = []
    
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    print("Odd numbers are:", odd_list)
    return even_list


print(even_odd_check_list([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]


# ============================================================================
# 8. TUPLE ITERATION AND ENUMERATION
# ============================================================================
stock_prices = [
    ("Apple", 200),
    ("Google", 1500),
    ("Microsoft", 300),
    ("Amazon", 3500)
]

# Enumerate: Display tuples with their index
print("\n--- Using enumerate() ---")
for item in enumerate(stock_prices):
    print(item)

# Tuple unpacking: Extract ticker and price
print("\n--- Extracting tickers ---")
for ticker, price in stock_prices:
    print(ticker)

# Tuple unpacking with calculation: Display adjusted prices (150% of original)
print("\n--- Adjusted prices (150% of original) ---")
for ticker, price in stock_prices:
    print(f"{ticker} : {price * 1.5}")

work_hours=[('Abby',100),('Billy',900),('Cassie',800)]
def employee_check(work_hours):
    """
    This function returns the name of the employee with the highest work hours.
    """
    current_max=0
    employee_of_month=''
    for employee, hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
    
    return (employee_of_month, current_max)

result=employee_check(work_hours)
print(result)  # Output: ('Cassie', 800)
name, hours=employee_check(work_hours)
print(name)
print(hours)

