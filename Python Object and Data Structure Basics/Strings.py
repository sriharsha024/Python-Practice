# ===== STRING BASICS =====
# Strings are sequences of characters enclosed in single or double quotes

# Create a string using double quotes
my_string = "Hello, World!"
print(my_string)  # Outputs: Hello, World!

# Create a string using single quotes
another_string = 'Python is fun!'   
print(another_string)  # Outputs: Python is fun!

# Use double quotes when the string contains a single quote
other_string = "It's a beautiful day!"
print(other_string)  # Outputs: It's a beautiful day!

# Demonstrating floating-point precision issue
print(0.1 + 0.2 - 0.3)  # Outputs: 5.551115123125783e-17


# ===== ESCAPE CHARACTERS =====
# Escape characters allow you to include special characters in strings

# \n creates a new line
print("Hello \nWorld!")  # Outputs:
                        # Hello
                        # World!

# \t creates a tab (indentation)
print("Hello \tWorld!")  # Outputs: Hello    World!

# \\ represents a single backslash
print("Hello \\ World!")  # Outputs: Hello \ World!

# \" allows double quotes inside a double-quoted string
print("She said, \"Hello!\"")  # Outputs: She said, "Hello!"

# \' allows single quotes inside a single-quoted string
print('It\'s a beautiful day!')  # Outputs: It's a beautiful day!


# ===== STRING SLICING =====
# Slicing syntax: [start:stop:step] - extracts substrings from a string

sample_text = "Python Programming"  

# Access the first character at index 0
print(sample_text[0])   # Outputs: P

# Access the last character (index -1)
print(sample_text[-1])  # Outputs: g

# Slice from index 0 to 6 (exclusive) - same as sample_text[:6]
print(sample_text[0:6])  # Outputs: Python

# Slice from index 7 to the end of the string
print(sample_text[7:])   # Outputs: Programming

# Slice with step of 2 (every 2nd character)
print(sample_text[::2])  # Outputs: Pto rgamn

# Slice in reverse order (step of -1)
print(sample_text[::-1])  # Outputs: gnimmargorP nohtyP

# Slice from index -11 to -1 with a step of 2
print(sample_text[-11:-1:2])  # Outputs: Pormi

# Slice with step of 3 (every 3rd character)
print(sample_text[::3])  # Outputs: Ph oai


# ===== STRING IMMUTABILITY =====
# Strings are immutable: they cannot be changed after creation

name = "john"
print(name)  # Outputs: john

# This would raise an error because strings cannot be modified:
# name[0] = "J"  # TypeError: 'str' object does not support item assignment

# To modify a string, create a new string by concatenating parts
name = "J" + name[1:3] + "a" + name[3:]
print(name)  # Outputs: Johan


# ===== STRING CONCATENATION AND REPETITION =====

# Concatenate strings using the + operator
greeting = "Hello, "
greeting += name
print(greeting)  # Outputs: Hello, Johan

# Repeat a string using the * operator
letter = 'A'
print(letter * 10)  # Outputs: AAAAAAAAAA

# String concatenation vs. numeric addition
a = '2'
b = '3'
print(a + b)  # Outputs: 23 (string concatenation, not addition)


# ===== STRING METHODS =====
# String methods are built-in functions that operate on strings

text = "  Hello, Python!  "

# lower() converts all characters to lowercase
print(text.lower())  # Outputs:   hello, python!

# upper() converts all characters to uppercase
print(text.upper())  # Outputs:   HELLO, PYTHON!

# strip() removes leading and trailing whitespace
print(text.strip())  # Outputs: Hello, Python!

# lstrip() removes whitespace only from the left (beginning)
print(text.lstrip())  # Outputs: Hello, Python!  

# rstrip() removes whitespace only from the right (end)
print(text.rstrip())  # Outputs:   Hello, Python!

# replace() substitutes all occurrences of a substring
print(text.replace("Python", "World"))  # Outputs:   Hello, World!  

# split() divides the string by a delimiter and returns a list
# Split by comma
print(text.split(","))  # Outputs: ['  Hello', ' Python!  ']

# Split by the character 'o'
print(text.split("o"))  # Outputs: ['  Hell', ', Pyth', 'n!  ']

# Split by whitespace (default behavior)
print(text.split())   # Outputs: ['Hello,', 'Python!']

# find() returns the index of the first occurrence of a substring
print(text.find("Python"))  # Outputs: 9

# startswith() checks if the string begins with the specified substring
print(text.startswith("  Hello"))  # Outputs: True

# endswith() checks if the string ends with the specified substring
print(text.endswith("!  "))  # Outputs: True

# count() returns the number of occurrences of a substring
print(text.count("o"))  # Outputs: 2

# len() returns the total number of characters in the string (including spaces)
print(len(text))  # Outputs: 18


# ===== STRING FORMATTING =====
# String formatting allows you to insert variables into strings

name = "Alice"
age = 30

# Method 1: String concatenation (older approach)
formatted_string_0 = "My name is " + name + " and I am " + str(age) + " years old."
print(formatted_string_0)  # Outputs: My name is Alice and I am 30 years old.

# Method 2: format() method with positional placeholders
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Outputs: My name is Alice and I am 30 years old.

# Method 3: f-string (formatted string literal) - most modern approach
print(f'My name is {name} and I am {age} years old.')  # Outputs: My name is Alice and I am 30 years old.

# format() with positional arguments
print('The {} {} {}'.format('fox', 'brown', 'quick'))  # Outputs: The fox brown quick

# format() with index-based positioning (reorder arguments)
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # Outputs: The quick brown fox

# ===== NUMERIC FORMATTING =====
# Format numbers with specific decimal places

result = 100 / 777

# Format with 3 decimal places
print("{:.3f}".format(result))  # Outputs: 0.129

# Format with named parameter
print("The result is {r}".format(r=result))  # Outputs: The result is 0.12870669...

# Format with named parameter and 2 decimal places
print("The result is {r:1.2f}".format(r=result))  # Outputs: The result is 0.13

# ===== FINANCIAL FORMATTING =====
# Format monetary values with proper decimal precision

balance_amount = 85.686522

# Format balance with 2 decimal places (common for currency)
print("{b:1.2f}".format(b=balance_amount))  # Outputs: 85.69