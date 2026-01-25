# ============================================================================
# IF, ELIF, ELSE STATEMENTS - Python Conditional Logic Examples
# ============================================================================
# Conditional statements allow you to execute different code blocks based on
# whether a condition is True or False
# ============================================================================


# ============================================================================
# 1. BASIC IF-ELSE STATEMENT
# ============================================================================

# Simple if-else: Execute code block only if condition is True
if True:
    print("This block executes because the condition is True")
else:
    print("This block does not execute")


# ============================================================================
# 2. IF-ELIF-ELSE STATEMENT - MULTIPLE CONDITIONS
# ============================================================================

# Create a variable to test
a = 223

# Check multiple conditions in sequence
# If first condition is True → execute that block and skip the rest
# If first is False → check next elif condition
# If all conditions are False → execute else block
if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")


# ============================================================================
# 3. MODULO OPERATOR - CHECKING EVEN OR ODD NUMBERS
# ============================================================================

# Use modulo (%) operator to find remainder after division
# If a % 2 == 0 → number is even
# If a % 2 == 1 → number is odd
if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")


# ============================================================================
# 4. BOOLEAN VARIABLE IN CONDITIONAL
# ============================================================================

# Use boolean variables directly in if statements
hungry = True

if hungry:
    print("Time to eat!")
else:
    print("Keep working!")


# ============================================================================
# 5. STRING COMPARISON IN IF-ELIF-ELSE
# ============================================================================

# Compare string values to execute different code blocks
loc = 'Store'

if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool!")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I don't know much.")
