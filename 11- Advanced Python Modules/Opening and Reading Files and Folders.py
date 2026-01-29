"""
=============================================================================
OS AND SHUTIL MODULES - FILE SYSTEM OPERATIONS
=============================================================================
This script demonstrates how to work with the operating system using:
- os module
- shutil module

Concepts covered:
- Getting current working directory
- Listing files and directories
- Creating and writing files
- Moving files
- Deleting files and folders (comments only for safety)
- Walking through directory trees using os.walk()

These tools are commonly used for automation and system-level tasks.
=============================================================================
"""

import os
import shutil


# ============================================================================
# 1. CURRENT WORKING DIRECTORY AND PATH INFORMATION
# ============================================================================

# Get the current working directory
print("Current Working Directory:")
print(os.getcwd())

# Display os.path module information
print("\nos.path module reference:")
print(os.path)

# List files and folders in the current directory
print("\nContents of current directory:")
print(os.listdir())

# List contents of the C drive (Windows)
print("\nContents of C drive:")
print(os.listdir("C:\\"))


# ============================================================================
# 2. FILE CREATION AND WRITE OPERATION
# ============================================================================

# Create a new file and write text into it
file_obj = open('practice.txt', 'w+')
file_obj.write("This is a test string")
file_obj.close()

print("\nFile 'practice.txt' created and written successfully.")


# ============================================================================
# 3. FILE MOVING USING SHUTIL
# ============================================================================
# Moves the file to another directory
# Uncomment only if the destination path exists

# shutil.move(
#     'practice.txt',
#     "D:\\Python-Practice\\11- Advanced Python Modules"
# )


# ============================================================================
# 4. FILE AND DIRECTORY DELETION (COMMENTED FOR SAFETY)
# ============================================================================
# These commands permanently delete files/folders.
# Always double-check paths before using them.

# os.unlink('file.txt')        # Deletes a file
# os.rmdir('empty_folder')     # Deletes an empty folder
# shutil.rmtree('folder')      # Deletes folder and all contents


# ============================================================================
# 5. SAFE DELETION USING send2trash (OPTIONAL)
# ============================================================================
# This sends files to Recycle Bin instead of permanent deletion

# import send2trash
# send2trash.send2trash("file.txt")


# ============================================================================
# 6. DIRECTORY TREE WALKING USING os.walk()
# ============================================================================
# os.walk() allows recursive traversal of directories

print("\nWalking through directory tree:\n")

for folder, subfolders, files in os.walk(
    "D:\\Python-Practice\\11- Advanced Python Modules\\MainFolder"
):
    print(f"Currently looking at folder:\n{folder}\n")

    print("Subfolders found:")
    for sub_folder in subfolders:
        print(f"  - {sub_folder}")

    print("\nFiles found:")
    for file in files:
        print(f"  - {file}")

    print("\n" + "-" * 50 + "\n")
