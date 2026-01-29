"""
=============================================================================
WORKING WITH ZIP FILES - zipfile MODULE
=============================================================================
This script demonstrates:
- Creating files programmatically
- Compressing multiple files into a ZIP archive
- Using ZIP_DEFLATED compression
- Extracting contents from a ZIP file

This is commonly used for:
- Backups
- File packaging
- Sharing multiple files as one archive
=============================================================================
"""

import zipfile


# ============================================================================
# 1. CREATE SAMPLE FILES
# ============================================================================

# Create first file
with open('file_one.txt', 'w+') as f:
    f.write('ONE FILE')

# Create second file
with open('file_two.txt', 'w+') as f:
    f.write('TWO FILE')


# ============================================================================
# 2. CREATE A ZIP FILE AND ADD FILES
# ============================================================================

# Create a ZipFile object in write mode
compressed_file = zipfile.ZipFile('comp_file.zip', 'w')

# Add files to the ZIP archive with compression
compressed_file.write(
    'file_one.txt',
    compress_type=zipfile.ZIP_DEFLATED
)

compressed_file.write(
    'file_two.txt',
    compress_type=zipfile.ZIP_DEFLATED
)

# Always close the zip file after writing
compressed_file.close()


# ============================================================================
# 3. EXTRACT FILES FROM ZIP ARCHIVE
# ============================================================================

# Open the zip file in read mode
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')

# Extract all contents into the specified folder
zip_obj.extractall('extracted_content')

# Close the zip file
zip_obj.close()

print("Files compressed and extracted successfully!")
