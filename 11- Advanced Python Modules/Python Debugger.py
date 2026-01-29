"""
=============================================================================
PYTHON DEBUGGING WITH PDB (PYTHON DEBUGGER)
=============================================================================
This script demonstrates how to use Python's built-in debugger (pdb) to:
- Pause program execution
- Inspect variables at runtime
- Step through code line by line
- Identify and understand runtime errors

The pdb module is extremely useful for debugging complex programs
where print statements are not sufficient.
=============================================================================
"""

import pdb


# ============================================================================
# 1. VARIABLE INITIALIZATION
# ============================================================================
# Define a list and some integer variables
x = [1, 2, 3]
y = 4
z = 9


# ============================================================================
# 2. NORMAL EXECUTION
# ============================================================================
# This operation works fine because both y and z are integers
result_1 = y + z
print("Result of y + z:", result_1)


# ============================================================================
# 3. START DEBUGGER
# ============================================================================
# The program execution will pause here
# You can now inspect variables and step through code
pdb.set_trace()


# ============================================================================
# 4. ERROR-PRONE OPERATION
# ============================================================================
# This line will raise a TypeError because:
# - x is a list
# - y is an integer
# Python does not allow adding a list and an integer
result_2 = x + y

print("Result of x + y:", result_2)
