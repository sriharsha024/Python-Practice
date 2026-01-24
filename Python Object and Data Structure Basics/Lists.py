# ===== LIST CREATION =====

# Create a list containing string elements
my_list = ['one', 'two', 'three', 'four', 'five']
print(my_list)
# Output: ['one', 'two', 'three', 'four', 'five']

# Create a list containing mixed data types
list_of_datatypes = ["apple", "banana", 102, 45.67, True]
print(list_of_datatypes)
# Output: ['apple', 'banana', 102, 45.67, True]

# Check the data type of my_list
print(type(my_list))
# Output: <class 'list'>


# ===== ACCESSING LIST ELEMENTS =====

# Access the first element using index 0
print(list_of_datatypes[0])
# Output: apple

# Access the last element using negative indexing
print(list_of_datatypes[-1])
# Output: True

# Slice elements from index 1 to 3 (index 4 is excluded)
print(list_of_datatypes[1:4])
# Output: ['banana', 102, 45.67]


# ===== LIST CONCATENATION =====

# Combine two lists using the + operator
modified_list = my_list + list_of_datatypes
print(modified_list)
# Output: ['one', 'two', 'three', 'four', 'five', 'apple', 'banana', 102, 45.67, True]


# ===== MODIFYING LIST ELEMENTS =====

# Modify the first element of the list
my_list[0] = "ONE"

# Replace elements at index positions 2 and 3
my_list[2:4] = ["THREE", "FOUR"]

print(my_list)
# Output: ['ONE', 'two', 'THREE', 'FOUR', 'five']


# ===== ADDING ELEMENTS TO LIST =====

# Append new elements to the end of the list
my_list.append("SIX")
my_list.append("SEVEN")

# Create an empty list to store removed elements
popped_list = []

print(my_list)
# Output: ['ONE', 'two', 'THREE', 'FOUR', 'five', 'SIX', 'SEVEN']


# ===== REMOVING ELEMENTS FROM LIST =====

# pop() removes the last element AND returns it
popped_list.append(my_list.pop())

print(my_list)
# Output: ['ONE', 'two', 'THREE', 'FOUR', 'five', 'SIX']

print(popped_list)
# Output: ['SEVEN']

# IMPORTANT DIFFERENCE:
# pop()     -> removes AND returns the element
# remove()  -> removes ONLY (returns None)

# remove() deletes "FOUR" from the list but does NOT return it
# So None is appended to popped_list
popped_list.append(my_list.remove("FOUR"))

print(my_list)
# Output: ['ONE', 'two', 'THREE', 'five', 'SIX']


# ===== FINAL OUTPUT CHECK =====

# Print the concatenated list created earlier
print(modified_list)
# Output: ['one', 'two', 'three', 'four', 'five', 'apple', 'banana', 102, 45.67, True]


# ===== LIST SORTING & REVERSING =====

# Create a numeric list
num_list = [5, 2, 9, 1, 5, 6]

# sort() modifies the list in ascending order
num_list.sort()
print(num_list)
# Output: [1, 2, 5, 5, 6, 9]

# reverse() reverses the list in place
num_list.reverse()
print(num_list)
# Output: [9, 6, 5, 5, 2, 1]

# reverse() returns None because it modifies the list in place
print(num_list.reverse())
# Output: None

# count() returns the number of occurrences of a value
print(num_list.count(5))
# Output: 2


# ===== NESTED LIST (MATRIX) =====

# Create a 2D list (matrix)
Matrix = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]]

# Access element from second row, third column
print(Matrix[1][2])
# Output: 6

# Get number of rows in the matrix
print(len(Matrix))
# Output: 3

# Get number of columns in the first row
print(len(Matrix[0]))
# Output: 4
