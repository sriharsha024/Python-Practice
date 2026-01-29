"""
=============================================================================
COLLECTIONS MODULE DEMONSTRATION
=============================================================================
This script demonstrates the usage of Python's built-in `collections` module.

Concepts covered:
- Counter: Counting occurrences of elements
- defaultdict: Handling missing keys gracefully
- namedtuple: Creating lightweight object-like tuples

These tools help write cleaner, safer, and more readable Python code.
=============================================================================
"""

# ============================================================================
# 1. COUNTER - COUNTING ELEMENT OCCURRENCES
# ============================================================================
from collections import Counter

# Tuple with repeated numbers
my_list = (
    1, 1, 2, 3, 4, 1, 2, 3, 2, 4,
    5, 6, 7, 1, 2, 3, 1, 4, 2,
    3, 7, 8, 9, 0, 9, 8, 6, 5
)

# Count frequency of each element
count_result = Counter(my_list)
print("Element frequency in my_list:")
print(count_result)

# Get the two most common elements
print("\nTwo most common elements:")
print(count_result.most_common(2))


# ============================================================================
# 2. COUNTER WITH STRINGS
# ============================================================================
string = "aaajnkdjnkklljoijrkjaaireoeinnlklallkkkjlgkjknkbn"

# Count character occurrences
print("\nCharacter frequency in string:")
print(Counter(string))


# ============================================================================
# 3. COUNTER WITH SENTENCE (WORD FREQUENCY)
# ============================================================================
sentence = "The dog is running. The cat is also running"

# Convert to lowercase and split into words
word_count = Counter(sentence.lower().split())

print("\nWord frequency in sentence:")
print(word_count)


# ============================================================================
# 4. DEFAULTDICT - HANDLING MISSING KEYS
# ============================================================================
from collections import defaultdict

# Normal dictionary example
normal_dict = {'a': 10, 'b': 20}
print("\nAccessing existing key from normal dictionary:")
print(normal_dict['a'])

# Accessing a missing key would raise KeyError
# print(normal_dict['wrong'])  # Uncommenting this will cause an error

# defaultdict automatically assigns a default value
default_dict = defaultdict(lambda: 0)

# Assign value to a key
default_dict['wing'] = 250

print("\ndefaultdict contents:")
print(default_dict)

print("Value for existing key 'wing':")
print(default_dict['wing'])

print("Value for missing key 'wings' (auto-created):")
print(default_dict['wings'])  # Returns 0 instead of KeyError


# ============================================================================
# 5. NAMEDTUPLE - LIGHTWEIGHT OBJECTS
# ============================================================================
from collections import namedtuple

# Create a namedtuple called Dog
Dog = namedtuple("Dog", ['age', 'breed', 'name'])

# Create an instance of Dog
sammy = Dog(age=5, breed="Husky", name="Sam")

print("\nNamedTuple example:")
print("Type of sammy:", type(sammy))
print("Dog details:", sammy)

# Access attributes like object properties
print("Dog age:", sammy.age)
print("Dog breed:", sammy.breed)

# Access values using index (tuple behavior)
print("Dog name (index access):", sammy[2])
