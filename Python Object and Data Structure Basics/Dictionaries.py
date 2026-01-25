# ============================================================================
# DICTIONARY BASICS - Python Examples
# ============================================================================

# ============================================================================
# 1. BASIC DICTIONARY CREATION AND ACCESS
# ============================================================================

# Create a simple dictionary with key-value pairs
my_dict = {'Name': 'John', 'Age': 30, 'City': 'New York'}

# Print the entire dictionary
print(my_dict)
# Output: {'Name': 'John', 'Age': 30, 'City': 'New York'}

# Access a dictionary value by key
print("The age is " + str(my_dict['Age']))
# Output: The age is 30


# ============================================================================
# 2. USING DICTIONARIES AS LOOKUP TABLES
# ============================================================================

# Create a dictionary for product prices
prices_lookup = {'apple': 2.99, 'banana': 1.99, 'orange': 2.59, 'milk': 3.49}

# Retrieve the price of milk
print(prices_lookup['milk'])
# Output: 3.49


# ============================================================================
# 3. NESTED DICTIONARIES AND MIXED DATA TYPES
# ============================================================================

# Create a dictionary with mixed data types (values can be numbers, lists, or dicts)
d = {'k1': 123, 'k2': [0, 2, 9], 'k3': {'insideKey': 100}}

# Access a nested dictionary
print(d['k3'])
# Output: {'insideKey': 100}

# Access values within nested dictionaries
print(d['k3']['insideKey'])
# Output: 100
# Alternative methods: d['k3'].get('insideKey') or d.get('k3').get('insideKey')

# Access a list value from the dictionary
print(d['k2'][2])
# Output: 9


# ============================================================================
# 4. EXTRACTING AND MANIPULATING NESTED VALUES
# ============================================================================

# Create a dictionary with list values
dict_example = {'key1': ['a', 'b', 'c'], 'key2': ['d', 'e']}

# Extract lists from dictionary
my_list_1 = dict_example['key1']
my_list_2 = dict_example['key2']

# Print extracted lists
print(my_list_1)
# Output: ['a', 'b', 'c']

print(my_list_2)
# Output: ['d', 'e']

# Extract individual elements from the lists
letter_a = my_list_1[0]
letter_b = my_list_2[1]

# Print extracted elements
print(letter_a)
# Output: a

print(letter_b)
# Output: e

# Convert a list element to uppercase
print(dict_example['key1'][2].upper())
# Output: C


# ============================================================================
# 5. MODIFYING DICTIONARIES - ADDING AND UPDATING VALUES
# ============================================================================

# Create a dictionary with initial key-value pairs
dict_2 = {'k1': 100, 'k2': 200}

# Add a new key-value pair to the dictionary
dict_2['k3'] = 300
print(dict_2)
# Output: {'k1': 100, 'k2': 200, 'k3': 300}

# Update an existing value
dict_2['k1'] = dict_2['k1'] - 50
print(dict_2)
# Output: {'k1': 50, 'k2': 200, 'k3': 300}


# ============================================================================
# 6. DICTIONARY METHODS - KEYS, VALUES, AND ITEMS
# ============================================================================

# Print all keys in the dictionary
print(dict_2.keys())
# Output: dict_keys(['k1', 'k2', 'k3'])

# Print all values in the dictionary
print(dict_2.values())
# Output: dict_values([50, 200, 300])

# Print all key-value pairs as tuples
print(dict_2.items())
# Output: dict_items([('k1', 50), ('k2', 200), ('k3', 300)])