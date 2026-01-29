"""
=============================================================================
REGULAR EXPRESSIONS (re MODULE) - COMPLETE PRACTICE
=============================================================================
This script demonstrates practical usage of Python's re module, including:
- Searching for patterns
- Extracting groups
- Using alternation (OR)
- Wildcards and anchors
- Negated character sets
- Cleaning and extracting text using regex
=============================================================================
"""

import re


# ============================================================================
# 1. SEARCHING FOR A PHONE NUMBER
# ============================================================================
text = "Please contact customer support at 408-888-9868 for assistance."

# Phone number pattern: XXX-XXX-XXXX
pattern = r'\d{3}-\d{3}-\d{4}'

match = re.search(pattern, text)

print("Search result object:", match)

if match:
    print("Matched phone number:", match.group())
    print("Span (start, end):", match.span())
    print("Start index:", match.start())
    print("End index:", match.end())


# ============================================================================
# 2. SEARCH VS FINDALL
# ============================================================================
text_1 = "I lost my phone yesterday. Now I need a new phone."

print("\nUsing re.search() (first match only):")
print(re.search('phone', text_1))

print("\nUsing re.findall() (all matches):")
print(re.findall('phone', text_1))


# ============================================================================
# 3. ITERATING OVER findall RESULTS
# ============================================================================
print("\nIterating over all matches:")
for word in re.findall('phone', text_1):
    print("Found word:", word)


# ============================================================================
# 4. COMMON REGEX CHARACTER CLASSES (REFERENCE)
# ============================================================================
# \d  -> Any digit (0–9)
# \D  -> Any NON-digit character
#
# \w  -> Any alphanumeric character (letters, digits, underscore)
# \W  -> Any NON-alphanumeric character
#
# \s  -> Any whitespace (space, tab, newline)
# \S  -> Any NON-whitespace character


# ============================================================================
# 5. REGEX QUANTIFIERS (HOW MANY TIMES?)
# ============================================================================
# +     -> One or more times
# *     -> Zero or more times
# ?     -> Zero or one time
#
# {3}   -> Exactly 3 times
# {2,4} -> Between 2 and 4 times
# {3,}  -> 3 or more times


# ============================================================================
# 6. GROUPING USING PARENTHESES
# ============================================================================
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)

print("\nFull phone number:", results.group())
print("Area code:", results.group(1))
print("Exchange code:", results.group(2))
print("Line number:", results.group(3))


# ============================================================================
# 7. ALTERNATION (OR CONDITION)
# ============================================================================
print("\nSearching for 'cat' OR 'dog':")
print(re.search(r'cat|dog', "The dog is sleeping on the sofa."))


# ============================================================================
# 8. BASIC PATTERN MATCHING
# ============================================================================
sentence = "The cat sat on the mat beside a rat."

print("\nFinding 'at' pattern:")
print(re.findall(r'at', sentence))

print("\nUsing wildcard . (any single character):")
print(re.findall(r'.at', sentence))

print("\nUsing two wildcards:")
print(re.findall(r'..at', sentence))


# ============================================================================
# 9. ANCHORS (^ START, $ END)
# ============================================================================
print("\nDigit at the start of the string:")
print(re.findall(r'^\d', '5 items are remaining'))

print("\nDigit at the end of the string:")
print(re.findall(r'\d$', 'Your OTP is 8'))


# ============================================================================
# 10. NEGATED CHARACTER SETS
# ============================================================================
print("\nRemoving digits from a sentence:")
print(re.findall(r'[^\d]+', 'Order 78 has 3 items costing 500'))


# ============================================================================
# 11. REMOVING PUNCTUATION FROM A SENTENCE
# ============================================================================
raw_text = "Hello! This, right here, is a clean sentence?"
clean_text = ' '.join(re.findall(r'[^!,.?]+', raw_text))

print("\nSentence without punctuation:")
print(clean_text)


# ============================================================================
# 12. EXTRACTING WORDS USING CHARACTER CLASSES
# ============================================================================
mixed_text = "Python-3.12 is fast_and powerful!"
words = re.findall(r'[\w]+', mixed_text)

print("\nExtracted words:")
print(' '.join(words))
