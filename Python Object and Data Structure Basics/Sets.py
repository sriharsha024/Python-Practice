# ============================================================================
# SETS BASICS - Python Examples
# ============================================================================
# Sets are unordered collections of unique elements
# They are mutable but cannot contain duplicate values
# Useful for membership testing, removing duplicates, and set operations
# ============================================================================


# ============================================================================
# 1. CREATING AN EMPTY SET AND INITIALIZING WITH ELEMENTS
# ============================================================================

# Create an empty set using set() constructor
my_set = set()
print(my_set)
# Output: set()

# Create a set with initial elements (note: unordered, unique values only)
my_set = {'apple', 'banana', 'cherry'}
print(my_set)
# Output: {'banana', 'cherry', 'apple'} (order may vary)


# ============================================================================
# 2. ADDING ELEMENTS TO A SET
# ============================================================================

# Add a single element to the set
my_set.add('orange')
print(my_set)
# Output: {'banana', 'cherry', 'orange', 'apple'}

# Add duplicate elements - sets ignore duplicates
my_set.add('apple')   # 'apple' is already in the set, so no change
my_set.add('banana')  # 'banana' is already in the set, so no change
print(my_set)
# Output: {'banana', 'cherry', 'orange', 'apple'}


# ============================================================================
# 3. SET SIZE AND MEMBERSHIP TESTING
# ============================================================================

# Get the number of elements in the set
print(len(my_set))
# Output: 4

# Check if an element exists in the set
print('banana' in my_set)
# Output: True

# Check if an element does NOT exist in the set
print('grape' in my_set)
# Output: False


# ============================================================================
# 4. REMOVING ELEMENTS FROM A SET
# ============================================================================

# Remove an element using remove() - raises error if not found
my_set.remove('cherry')
print(my_set)
# Output: {'banana', 'orange', 'apple'}

# Remove an element using discard() - NO error if not found
my_set.discard('grape')  # 'grape' is not in the set, but no error
print(my_set)
# Output: {'banana', 'orange', 'apple'}


# ============================================================================
# 5. ITERATING THROUGH A SET
# ============================================================================

# Loop through all elements in the set
for fruit in my_set:
    print(fruit)
# Output (order may vary):
# banana
# orange
# apple


# ============================================================================
# 6. REMOVING DUPLICATES FROM A LIST USING SETS
# ============================================================================

# Create a list with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]
print(my_list)
# Output: [1, 2, 2, 3, 4, 4, 5]

# Convert list to set to automatically remove duplicates
unique_set = set(my_list)
print(unique_set)
# Output: {1, 2, 3, 4, 5}

# Convert back to list if needed (order may vary)
unique_list = list(unique_set)
print(unique_list)
# Output: [1, 2, 3, 4, 5] (order may vary)


# ============================================================================
# 7. CONVERTING STRINGS TO SETS - UNIQUE CHARACTERS
# ============================================================================

# Convert a string to a set of unique characters
print(set("Mississippi"))
# Output: {'M', 'i', 's', 'p'}