# ============================================================================
# FOR LOOPS - Python Iteration Examples
# ============================================================================
# For loops allow you to iterate over sequences like lists, tuples, strings,
# dictionaries, and ranges. They execute a code block for each item.
# ============================================================================


# ============================================================================
# 1. BASIC FOR LOOP WITH RANGE() - ITERATE SPECIFIED NUMBER OF TIMES
# ============================================================================

# range(5) generates numbers: 0, 1, 2, 3, 4
for i in range(5):
    print("Iteration:", i)
# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4


# ============================================================================
# 2. LOOPING THROUGH A LIST - ITERATE OVER EACH ELEMENT
# ============================================================================

# Create a list of fruits
my_list = ['apple', 'banana', 'cherry']

# Loop through each fruit in the list
for fruit in my_list:
    print("Fruit:", fruit)
# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry


# ============================================================================
# 3. RANGE WITH STEP - ITERATE WITH CUSTOM INCREMENT
# ============================================================================

# range(start, stop, step) - generates numbers from start to stop-1, incrementing by step
# range(0, 10, 2) generates: 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print("Even number:", i)
# Output: 0, 2, 4, 6, 8


# ============================================================================
# 4. LOOPING THROUGH A STRING - ITERATE OVER EACH CHARACTER
# ============================================================================

# Strings are iterable - loop through each character
for char in "Hello":
    print("Character:", char)
# Output:
# Character: H
# Character: e
# Character: l
# Character: l
# Character: o


# ============================================================================
# 5. ENUMERATE() - GET INDEX AND VALUE SIMULTANEOUSLY
# ============================================================================

# enumerate() provides both the index and the value
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)
# Output:
# Index: 0 Value: apple
# Index: 1 Value: banana
# Index: 2 Value: cherry


# ============================================================================
# 6. CONDITIONAL LOGIC INSIDE LOOPS - IF-ELSE WITH FOR
# ============================================================================

# Create a list of numbers
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check if each number is even or odd
for num in mylist:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print("{} is odd".format(num))
# Output:
# 1 is odd
# 2 is even
# 3 is odd
# ... and so on


# ============================================================================
# 7. STRING REPETITION IN LOOPS
# ============================================================================

# The * operator repeats strings
for num in mylist:
    print("Hi " * num)
# Output:
# Hi  (1 time)
# Hi Hi  (2 times)
# Hi Hi Hi  (3 times)
# ... and so on


# ============================================================================
# 8. ACCUMULATION - SUMMING VALUES IN A LOOP
# ============================================================================

# Initialize accumulator variable
list_sum = 0

# Add each number to the sum and print current sum
for num in mylist:
    list_sum = list_sum + num
    print("Current Sum:", list_sum)

# Print final sum
print("The sum is:", list_sum)
# Output:
# Current Sum: 1
# Current Sum: 3
# Current Sum: 6
# ... and so on
# The sum is: 55


# ============================================================================
# 9. LOOPING THROUGH A STRING CHARACTER BY CHARACTER
# ============================================================================

# Iterate through each character in a string
for letter in "Sri Harsha":
    print(letter)
# Output:
# S
# r
# i
#  (space)
# H
# ... and so on


# ============================================================================
# 10. LOOPING THROUGH A TUPLE
# ============================================================================

# Tuples are immutable sequences (like lists, but can't be changed)
tuple_example = (1, 2, 3)

for item in tuple_example:
    print(item)
# Output:
# 1
# 2
# 3


# ============================================================================
# 11. TUPLE UNPACKING IN LOOPS - UNPACK TUPLES FROM LIST OF TUPLES
# ============================================================================

# Create a list of tuples (each tuple has 2 elements)
my_list_1 = [(1, 6), (3, 5), (4, 2)]

# Method 1: Unpack each tuple into separate variables
for a, b in my_list_1:
    print(a)
    print(b)
# Output:
# 1
# 6
# 3
# 5
# 4
# 2

# Method 2: Loop without unpacking (get whole tuple)
for item in my_list_1:
    print(item)
# Output:
# (1, 6)
# (3, 5)
# (4, 2)

# Get the number of tuples in the list
print(len(my_list_1))
# Output: 3


# ============================================================================
# 12. LOOPING THROUGH DICTIONARIES - KEYS, VALUES, AND ITEMS
# ============================================================================

# Create a dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 12A. LOOPING DIRECTLY OVER DICTIONARY - GETS KEYS ONLY (DEFAULT)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# By default, looping over a dictionary gives only the KEYS
for item in d:
    print(item)
# Output:
# k1
# k2
# k3
# 📌 Note: item here is actually a key, not a key-value pair
# Equivalent to: for item in d.keys()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 12B. LOOPING WITH .items() - GETS BOTH KEYS AND VALUES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# .items() returns key-value pairs that are unpacked into key and value
for key, value in d.items():
    print("Key:", key)
    print("Value:", value)
# Output:
# Key: k1
# Value: 1
# Key: k2
# Value: 2
# Key: k3
# Value: 3
# 📌 Note: .items() returns tuples, which are automatically unpacked


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 12C. LOOPING WITH .keys() - EXPLICITLY GET KEYS ONLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# .keys() explicitly returns only the keys (same as looping directly)
for key in d.keys():
    print("Key:", key)
# Output:
# Key: k1
# Key: k2
# Key: k3


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 12D. LOOPING WITH .values() - GET VALUES ONLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# .values() returns only the values from the dictionary
for value in d.values():
    print("Value:", value)
# Output:
# Value: 1
# Value: 2
# Value: 3


# ============================================================================
# DICTIONARY LOOPING REFERENCE TABLE
# ============================================================================
# ┌─────────────────────┬────────────────┬──────────────────────────────────┐
# │ Loop Method         │ What you get   │ Use case                         │
# ├─────────────────────┼────────────────┼──────────────────────────────────┤
# │ for x in d:         │ Keys only      │ When you only need keys          │
# │ for x in d.keys():  │ Keys only      │ Explicit version of above        │
# │ for x in d.values():│ Values only    │ When you only need values        │
# │ for k, v in d.i():  │ Keys & values  │ When you need both simultaneously│
# └─────────────────────┴────────────────┴──────────────────────────────────┘  