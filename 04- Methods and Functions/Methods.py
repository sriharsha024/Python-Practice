"""
=============================================================================
LIST METHODS DEMONSTRATION
=============================================================================
This module demonstrates various built-in methods available for Python lists.
Each method shows how to manipulate and interact with list objects.
=============================================================================
"""

# Initialize a list with sample integers
mylist = [1, 2, 3, 4, 5]


# ============================================================================
# 1. APPEND - Add a single element to the end of the list
# ============================================================================
mylist.append(6)
print(mylist)  # Output: [1, 2, 3, 4, 5, 6]


# ============================================================================
# 2. REMOVE - Remove the first occurrence of a specific value
# ============================================================================
mylist.remove(3)
print(mylist)  # Output: [1, 2, 4, 5, 6]


# ============================================================================
# 3. POP - Remove and return the last item from the list
# ============================================================================
mylist.pop()
print(mylist)  # Output: [1, 2, 4, 5]


# ============================================================================
# 4. INSERT - Insert an element at a specified index position
# ============================================================================
mylist.insert(2, 10)
print(mylist)  # Output: [1, 2, 10, 4, 5]


# ============================================================================
# 5. SORT - Sort the list in ascending order (modifies original list)
# ============================================================================
mylist.sort()
print(mylist)  # Output: [1, 2, 4, 5, 10]


# ============================================================================
# 6. REVERSE - Reverse the order of elements in the list
# ============================================================================
mylist.reverse()
print(mylist)  # Output: [10, 5, 4, 2, 1]


# ============================================================================
# 7. COUNT - Count occurrences of a specific element
# ============================================================================
count_of_2 = mylist.count(2)
print(count_of_2)  # Output: 1


# ============================================================================
# 8. EXTEND - Add multiple elements from an iterable to the list
# ============================================================================
mylist.extend([7, 8, 9])
print(mylist)  # Output: [10, 5, 4, 2, 1, 7, 8, 9]


# ============================================================================
# 9. INDEX - Find the index of the first occurrence of a value
# ============================================================================
index_of_4 = mylist.index(4)
print(index_of_4)  # Output: 2


# ============================================================================
# 10. COPY - Create a shallow copy of the list
# ============================================================================
list1 = mylist.copy()
print(list1)  # Output: [10, 5, 4, 2, 1, 7, 8, 9]


# ============================================================================
# 11. CLEAR - Remove all items from the list
# ============================================================================
mylist.clear()
print(mylist)  # Output: [] # mylist is now empty

from platform import python_version
print("Python Version:", python_version())  # Output: Python Version: X.X.X