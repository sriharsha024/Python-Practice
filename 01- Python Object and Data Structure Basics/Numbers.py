# ===== BASIC ARITHMETIC OPERATIONS =====

# Print a welcome message
print("My first Python program ")

# Addition: 2 + 1 = 3
print(2 + 1)

# Multiplication: 2 * 2 = 4
print(2 * 2)

# Subtraction: 3 - 1 = 2
print(3 - 1)

# Division: 6 / 2 = 3.0 (always returns a float)
print(6 / 2)

# Floor division: 7 // 3 = 2 (rounds down to nearest integer)
print(7 // 3)

# Modulus: 7 % 3 = 1 (returns the remainder of division)
print(7 % 3)

# Exponentiation: 2 ** 3 = 8 (2 raised to the power of 3)
print(2 ** 3)

# ===== OPERATOR PRECEDENCE =====

# Multiplication has higher precedence than addition
# Calculated as: 2 + (3 * 4) = 2 + 12 = 14
print(2 + 3 * 4)

# Parentheses override default precedence
# Calculated as: (2 + 3) * (4 * 8) = 5 * 32 = 160
print((2 + 3) * (4 * 8))

# ===== VARIABLES AND OPERATIONS =====

# Store integer and float values in variables
a = 10  # Integer variable
b = 5   # Integer variable
c = 2.5  # Float variable

# Check the data type of variable a (should be int)
print(type(a))  # Outputs: <class 'int'>

# Check the data type of variable c (should be float)
print(type(c))  # Outputs: <class 'float'>

# Add the two integer variables
print(a + b)  # Outputs: 15

# Multiply the two integer variables
print(a * b)  # Outputs: 50

# ===== FLOATING-POINT PRECISION =====

# Floating-point arithmetic can have precision issues due to binary representation
# This demonstrates the IEEE 754 floating-point standard limitations
# Expected result: 0.0
# Actual result: 2.7755575615628914e-17 (very close to zero, but not exact)
print(0.1 + (0.2 - 0.3))

# ===== VARIABLE REASSIGNMENT =====

# Assign an integer value to my_dogs
my_dogs = 2
print(my_dogs)  # Outputs: 2

# Reassign my_dogs to a list of strings (variable can hold different data types)
my_dogs = ["Sammy", "Frankie"]
print(my_dogs)  # Outputs: ['Sammy', 'Frankie']

# Check the data type of my_dogs (should be list)
print(type(my_dogs))  # Outputs: <class 'list'>

# ===== MATHEMATICAL VERIFICATION =====

# Verify the relationship: (quotient * divisor) + remainder = dividend
# Breaking down 7 ÷ 3: quotient=2, remainder=1
# Verify: (7 // 3) * 3 + (7 % 3) = 2 * 3 + 1 = 6 + 1 = 7
print((((7 // 3) * 3) + (7 % 3)) == 7)  # Outputs: True

# ===== TAX CALCULATION EXAMPLE =====

# Define the annual income
my_income = 1000  # Income in dollars

# Define the tax rate as a decimal (0.25 = 25%)
tax_rate = 0.25

# Calculate taxes owed by multiplying income by tax rate
my_taxes = my_income * tax_rate

# Display the calculated tax amount
print(my_taxes)  # Outputs: 250.0