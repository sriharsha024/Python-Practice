# ============================================================================
# COMPARISON, BOOLEAN & LOGICAL OPERATORS - Python Examples
# ============================================================================

# ============================================================================
# 1. COMPARISON OPERATORS (==, !=, >, <, >=, <=)
# ============================================================================

# Equality: checks if both values are equal
print(2 == 2)        # True

# Not equal: checks if values are different
print(3 != 4)        # True

# Greater than
print(5 > 3)         # True

# Less than
print(2 < 5)         # True

# Greater than or equal to
print(4 >= 4)        # True

# Less than or equal to
print(3 <= 2)        # False


# ============================================================================
# 2. STRING COMPARISONS (Case-sensitive)
# ============================================================================

print("Hello" == "")        # False (non-empty vs empty)
print("Hello" == "Hello")  # True  (same text)
print("Hello" == "hello")  # False (case-sensitive)
print('Hello' == "Hello")  # True  (quotes don't matter)


# ============================================================================
# 3. COMPARING DIFFERENT DATA TYPES
# ============================================================================

print('2' == 2)     # False (string vs integer)
print(2 == 2.0)     # True  (int and float with same value)


# ============================================================================
# 4. CONVERTING VALUES TO BOOLEAN USING bool()
# ============================================================================

# Numbers
print(bool(0))      # False (0 is falsy)
print(bool(42))     # True  (non-zero is truthy)

# Strings
print(bool(""))     # False (empty string)
print(bool("Hi"))   # True  (non-empty string)


# ============================================================================
# 5. LOGICAL OPERATORS: and, or, not
# ============================================================================

# 'and' returns the first False value, or last value if all are True
print(2 and 3)      # 3 (both are True → last value)
print(0 and 3)      # 0 (first False)

# 'or' returns the first True value, or last value if all are False
print(2 or 0)       # 2 (first True)
print(0 or 0)       # 0 (all False)

# 'not' reverses the truth value
print(not 2)        # False (2 is True → not True = False)
print(not 0)        # True  (0 is False → not False = True)


# ============================================================================
# 6. CHAINED COMPARISONS
# ============================================================================

# Python allows chained comparisons
print(1 < 2 < 3)            # True (1<2 and 2<3)

# Mixed logical and comparison operators
print(1 < 2 > 1 and 2 >= 3) # False


# ============================================================================
# 7. IMPORTANT NOTE: THIS IS NOT BITWISE OPERATIONS
# ============================================================================

# Logical operators (truth-based)
# and, or, not

# Bitwise operators (binary-level)
print(2 & 3)   # 2  (bitwise AND)
print(2 | 3)   # 3  (bitwise OR)


# ============================================================================
# EXAM-READY SUMMARY
# ============================================================================

# - Comparison operators return True or False
# - bool() converts values based on truthiness
# - 0, "", [], {} → False
# - Non-zero, non-empty → True
# - 'and' and 'or' return operands, not booleans
# - Bitwise (&, |) are different from logical (and, or)
