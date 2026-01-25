# ============================================================================
# FILE I/O BASICS - Python Examples
# ============================================================================
# Working with files: Reading, writing, and appending data
# Using the 'with' statement for safe file handling
# ============================================================================


# ============================================================================
# 1. WRITING TO A FILE - CREATE AND WRITE CONTENT
# ============================================================================

# Use 'with' statement for automatic file closing (best practice)
with open('myfile.txt', 'w') as file:
    file.write("Hello World this is a text file.\n")
    file.write("this is the second line.\n")
    file.write("This is the third line.")


# ============================================================================
# 2. READING FROM A FILE - READ ALL CONTENT AT ONCE
# ============================================================================

# Method 1: Traditional approach (manual closing) - NOT RECOMMENDED
myfile = open('myfile.txt', 'r')
content = myfile.read()
print(content)
myfile.close()
# Output:
# Hello World this is a text file.
# this is the second line.
# This is the third line.



# ============================================================================
# 3. READING FILE LINE BY LINE - READLINE AND READLINES
# ============================================================================

print("To avoid this error, ensure the file exists before reading.")

# Open file in 'r+' mode (read and write)
myfile = open('myfile.txt', 'r+')

# Move cursor to the beginning of the file
myfile.seek(0)

# Read the first line only (including newline character)
line = myfile.readline()
print(line)
# Output: This is a new file.

# Read all remaining lines as a list of strings
remaining_lines = myfile.readlines()
print(remaining_lines)
# Output: ['All previous content is gone.\n', 'This is the second line of the new file.\n', 'This is the third line of the new file.']

# Always close the file when done (since we're not using 'with' statement here)
myfile.close()
#     print(content)
# FileNotFoundError: [Errno 2] No such file or directory: 'myyfilee.txt'



# ============================================================================
# 4. WHY USE 'with' STATEMENT - BEST PRACTICE FOR FILE HANDLING
# ============================================================================

# ❌ WITHOUT 'with' (manual closing - problematic):
# file = open('myfile.txt', 'r')
# content = file.read()
# print(content)
# file.close()   # ❗ You must remember this
#
# Problems:
# - If an error occurs → close() may never run
# - File can stay open → memory/resource leak

# ✅ WITH 'with' (BEST practice):
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)

# What Python does automatically:
# 1. Opens the file
# 2. Assigns it to the variable 'file'
# 3. Runs your code block
# 4. Closes the file automatically (even if an error occurs)


# ============================================================================
# 5. FILE MODES - UNDERSTANDING 'r', 'w', 'a', 'r+', 'w+'
# ============================================================================

# Mode Reference Table:
# ┌─────┬──────────────┬─────────────────┬──────────┬──────────────────────────┐
# │Mode │ Meaning      │ File must exist? │ Can read │ Can write                │
# ├─────┼──────────────┼─────────────────┼──────────┼──────────────────────────┤
# │ 'r' │ Read         │ ✅ Yes           │ ✅ Yes   │ ❌ No                    │
# │ 'w' │ Write        │ ❌ No            │ ❌ No    │ ✅ Yes (overwrites)      │
# │ 'a' │ Append       │ ❌ No            │ ❌ No    │ ✅ Yes (adds at end)     │
# │'r+' │ Rd + Wr      │ ✅ Yes           │ ✅ Yes   │ ✅ Yes                   │
# │'w+' │ Wr + Rd      │ ❌ No            │ ✅ Yes   │ ✅ Yes (overwrites)      │
# └─────┴──────────────┴─────────────────┴──────────┴──────────────────────────┘


# ============================================================================
# 6. READING A FILE
# ============================================================================

# Read the entire file content
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)


# ============================================================================
# 7. USING 'w+' MODE - WRITE AND READ IN ONE OPERATION
# ============================================================================

# 'w+' mode: Creates a new file (overwrites if exists) and allows both reading and writing
with open('myfile_w_plus.txt', 'w+') as file:
    # Write content to the file
    file.write("This file was created with w+ mode.\n")
    file.write("We can write to it and read from it.\n")
    
    # Move cursor back to beginning to read the content we just wrote
    file.seek(0)
    
    # Read the content we just wrote
    content = file.read()
    print("Content read in w+ mode:")
    print(content)
    # Output: This file was created with w+ mode.
    #         We can write to it and read from it.


# ============================================================================
# 8. APPENDING TO A FILE - ADD CONTENT WITHOUT OVERWRITING
# ============================================================================

# Append mode 'a' adds new content to the end of the file
with open('myfile.txt', 'a') as file:
    file.write("\nThis is an appended line.")

# Read the file again to see the appended content
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)


# ============================================================================
# 9. OVERWRITING A FILE - WRITE MODE CLEARS PREVIOUS CONTENT
# ============================================================================

# Write mode 'w' overwrites all previous content
with open('myfile.txt', 'w') as file:
    file.write("This is a new file.\nAll previous content is gone.")
    file.write("\nThis is the second line of the new file.")
    file.write("\nThis is the third line of the new file.")

# Read the file to confirm it was overwritten
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)


# ============================================================================
# 10. HANDLING FILE NOT FOUND ERRORS
# ============================================================================

# Uncomment below to see what happens when file doesn't exist
# with open('myyfilee.txt', 'r') as file:
#     content = file.read()
#     print(content)
# FileNotFoundError: [Errno 2] No such file or directory: 'myyfilee.txt'

