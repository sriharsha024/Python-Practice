# ============================================================================
# BOOLEANS BASICS - Python Examples
# ============================================================================
# Booleans are a data type with only two possible values: True and False
# They are fundamental for conditional statements and control flow
# ============================================================================


# ============================================================================
# 1. BOOLEAN VALUES AND TYPE
# ============================================================================

# Print the two boolean values
print(True)
# Output: True

print(False)
# Output: False

# Check the data type of boolean values
print(type(True))
# Output: <class 'bool'>

print(type(False))
# Output: <class 'bool'>


# ============================================================================
# 2. COMPARISON OPERATORS - CREATING BOOLEANS
# ============================================================================

# Greater than operator
print(1 > 3)
# Output: False

# Greater than or equal to operator
print(3 >= 2)
# Output: True

# Equality operator
print(2 == 2)
# Output: True


# ============================================================================
# 3. BOOLEAN LOGICAL OPERATIONS - AND, OR, NOT
# ============================================================================

# AND operation: Returns True only if both operands are True
print(True and False)
# Output: False

print(True and True)
# Output: True

# OR operation: Returns True if at least one operand is True
print(True or False)
# Output: True

print(False or False)
# Output: False

# NOT operation: Inverts the boolean value (negation)
print(not True)
# Output: False

print(not False)
# Output: True


# ============================================================================
# 4. CONVERTING VALUES TO BOOLEAN USING bool()
# ============================================================================

# Numbers: Non-zero values are True, zero is False
print(bool(1))
# Output: True

print(bool(0))
# Output: False


# ============================================================================
# 5. TRUTHINESS - HOW PYTHON EVALUATES EMPTY vs NON-EMPTY OBJECTS
# ============================================================================

# Rule: Empty objects → False | Non-empty objects → True

# Non-empty string is truthy (True)
print(bool("Hello"))
# Output: True

# Empty string is falsy (False)
print(bool(""))
# Output: False

# Non-empty list is truthy (True)
print(bool([1, 2, 3]))
# Output: True

# Empty list is falsy (False)
print(bool([]))
# Output: False