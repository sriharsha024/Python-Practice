# ============================================================================
# USEFUL OPERATORS AND FUNCTIONS - Python Examples
# ============================================================================
# Common operators and built-in functions for working with sequences,
# random numbers, and user input
# ============================================================================


# ============================================================================
# 1. RANGE() - GENERATE SEQUENCES OF NUMBERS
# ============================================================================

# range(start, stop, step) generates numbers from start to stop-1
# Convert to tuple or list to see the generated values
print(tuple(range(0, 20, 3)))
# Output: (0, 3, 6, 9, 12, 15, 18)

print(list(range(0, 20, 3)))
# Output: [0, 3, 6, 9, 12, 15, 18]


# ============================================================================
# 2. ENUMERATING A STRING - GET INDEX AND CHARACTER
# ============================================================================

# Method 1: Manual indexing with counter
name = "John Doe"
index = 0

for letter in name:
    print(index, name[index])
    index += 1
# Output:
# 0 J
# 1 o
# 2 h
# ... and so on

# Method 2: Using enumerate() - automatic index tracking
for letter in enumerate(name):
    print(letter)
# Output:
# (0, 'J')
# (1, 'o')
# (2, 'h')
# ... and so on


# ============================================================================
# 3. ZIP() - COMBINE MULTIPLE LISTS ELEMENT BY ELEMENT
# ============================================================================

# Create multiple lists
my_list_1 = ['apple', 'banana', 'cherry']
my_list_2 = [1, 2, 3]
my_list_3 = [200, 300, 400]

# zip() combines lists into tuples of corresponding elements
zipped = zip(my_list_2, my_list_1, my_list_3)

# Iterate through zipped tuples
for item in zipped:
    print(item)
# Output:
# (1, 'apple', 200)
# (2, 'banana', 300)
# (3, 'cherry', 400)


# ============================================================================
# 4. IN OPERATOR - MEMBERSHIP TESTING
# ============================================================================

# Check if a value exists in a list
print(20 in [1, 2, 3, 4, 5])
# Output: False

# Check if a substring exists in a string
print('a' in 'apple')
# Output: True


# ============================================================================
# 5. BUILT-IN FUNCTIONS FOR SEQUENCES - MIN, MAX, SUM, LEN, SORTED
# ============================================================================

# Create a list of numbers
mylist = [1000, 250, 309, 5240, 320]

# Check membership
print(20 in mylist)
# Output: False

# Find minimum value
print(min(mylist))
# Output: 250

# Find maximum value
print(max(mylist))
# Output: 5240

# Calculate sum of all elements
print(sum(mylist))
# Output: 7119

# Get number of elements
print(len(mylist))
# Output: 5

# Return sorted list (ascending order)
print(sorted(mylist))
# Output: [250, 309, 320, 1000, 5240]


# ============================================================================
# 6. RANDOM SHUFFLE - RANDOMIZE LIST ORDER
# ============================================================================

# Import shuffle function from random module
from random import shuffle

# Create a list to shuffle
list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Shuffle modifies the list in-place (changes original list)
shuffle(list_to_shuffle)
print(list_to_shuffle)
# Output: [randomized order, e.g., [3, 7, 1, 9, 2, 8, 4, 6, 5]]

# Shuffle again
shuffle(list_to_shuffle)
print(list_to_shuffle)
# Output: [different randomized order]


# ============================================================================
# 7. RANDOM RANDINT - GENERATE RANDOM INTEGER
# ============================================================================

# Import randint function from random module
from random import randint

# Generate random integer between 1 and 100 (inclusive)
random_number = randint(1, 100)
print(random_number)
# Output: random number between 1 and 100


# ============================================================================
# 8. USER INPUT - GETTING DATA FROM USER WITH TYPE CONVERSION
# ============================================================================

# Get string input from user
name = str(input("Enter your name: "))
print("Hello, {}".format(name))
# Input: John
# Output: Hello, John


# Get integer input from user
age = int(input("Enter your age: "))
print("You are {} years old".format(age))

# Age categorization based on age input
if age < 18:
    print("You are a minor")
elif age <= 60:
    print("You are an adult")
else:
    print("You are a senior citizen")


# Get float input for height
height = float(input("Enter your height in cm: "))
print("You are {} cm tall".format(height))

# Height categorization based on height input
if height < 150:
    print("Height category: Short")
elif height <= 180:
    print("Height category: Average")
else:
    print("Height category: Tall")


# Get float input for weight
weight = float(input("Enter your weight in kg: "))
print("You weigh {} kg".format(weight))

# Weight categorization based on weight input
if weight < 50:
    print("Weight category: Underweight")
elif weight <= 80:
    print("Weight category: Normal")
else:
    print("Weight category: Overweight")


# ============================================================================
# 9. LIST COMPREHENSION - CREATE LISTS WITH CONCISE SYNTAX
# ============================================================================

# List Comprehension 1: Create a list from a string
# Syntax: [expression for item in iterable]
my_list_4 = [char for char in 'hsfjkjnsvk']
print(my_list_4)
# Output: ['h', 's', 'f', 'j', 'k', 'j', 'n', 's', 'v', 'k']

# List Comprehension 2: Create a list of squared numbers
# Syntax: [expression for item in iterable]
my_list_5 = [num**2 for num in range(0, 11)]
print(my_list_5)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List Comprehension 3: Create a filtered list
# Syntax: [expression for item in iterable if condition]
filtered_list = [num for num in range(0, 20) if num % 3 == 0]
print(filtered_list)
# Output: [0, 3, 6, 9, 12, 15, 18]