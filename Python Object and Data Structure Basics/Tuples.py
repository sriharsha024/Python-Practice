# ============================================================================
# TUPLES BASICS - Python Examples
# ============================================================================
# Tuples are ordered, immutable data structures (cannot be changed after creation)
# They are similar to lists but offer better performance and security
# ============================================================================


# ============================================================================
# 1. BASIC TUPLE CREATION AND PROPERTIES
# ============================================================================

# Create a tuple with multiple string elements
my_tuple = ('one', 'two', 'three', 'four', 'five')

# Print the entire tuple
print(my_tuple)
# Output: ('one', 'two', 'three', 'four', 'five')

# Check the type of the variable
print(type(my_tuple))
# Output: <class 'tuple'>

# Get the number of elements in the tuple
print(len(my_tuple))
# Output: 5


# ============================================================================
# 2. ACCESSING TUPLE ELEMENTS - INDEXING AND SLICING
# ============================================================================

# Access first element (index 0)
print(my_tuple[0])
# Output: one

# Access last element using negative indexing
print(my_tuple[-1])
# Output: five

# Access a range of elements using slicing [start:end)
print(my_tuple[1:4])
# Output: ('two', 'three', 'four')


# ============================================================================
# 3. IMMUTABILITY - WHY TUPLES CANNOT BE MODIFIED
# ============================================================================

# Tuples are immutable, so direct modification raises an error
# Uncomment the line below to see the TypeError
# my_tuple[0] = 'ONE'
# TypeError: 'tuple' object does not support item assignment

# However, you can concatenate tuples to create a NEW tuple
new_tuple = my_tuple + ('six', 'seven')
print(new_tuple)
# Output: ('one', 'two', 'three', 'four', 'five', 'six', 'seven')


# ============================================================================
# 4. TUPLE METHODS - COUNT AND INDEX
# ============================================================================

# Create a tuple with repeated elements
t = ('a', 'b', 'a', 'c', 'd', 'a')

# Count occurrences of a specific element
print(t.count('a'))
# Output: 3

# Find the index (position) of an element
print(t.index('d'))
# Output: 4


# ============================================================================
# 5. SINGLE ELEMENT TUPLE - THE IMPORTANCE OF THE COMMA
# ============================================================================

# Create a single element tuple (MUST include trailing comma)
single_element_tuple = ('only_one',)
print(type(single_element_tuple))
# Output: <class 'tuple'>

# Without the comma, it's just a string in parentheses, NOT a tuple
not_a_tuple = ('only_one')
print(type(not_a_tuple))
# Output: <class 'str'>


# ============================================================================
# 6. TUPLE UNPACKING - ASSIGNING ELEMENTS TO MULTIPLE VARIABLES
# ============================================================================

# Unpack tuple elements into individual variables
a, b, c, y, f = my_tuple

# Print unpacked variables
print(a)
# Output: one

print(y)
# Output: four
