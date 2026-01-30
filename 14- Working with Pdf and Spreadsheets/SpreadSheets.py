# ---------------------------------------------------
# CSV FILE HANDLING IN PYTHON
# Tools commonly used:
# 1. csv module (built-in)
# 2. pandas
# 3. openpyxl (Excel)
# 4. Google Sheets Python API
# ---------------------------------------------------

import csv

# ---------------------------------------------------
# READ DATA FROM CSV FILE
# ---------------------------------------------------

# Open the CSV file with UTF-8 encoding
data = open(
    '14- Working with Pdf and Spreadsheets\\example.csv',
    encoding='utf-8'
)

# Create a CSV reader object
csv_data = csv.reader(data)

# Convert CSV reader object into a list
data_lines = list(csv_data)

# Print total number of rows in the CSV file
print("Total rows:", len(data_lines))

# Print the second row (index starts from 0)
print("Second row:", data_lines[1])


# ---------------------------------------------------
# DISPLAY FIRST FEW ROWS
# ---------------------------------------------------

# Print first 6 rows of the CSV file
for line in data_lines[:6]:
    print(line)


# ---------------------------------------------------
# ACCESS SPECIFIC COLUMN DATA
# ---------------------------------------------------

# Print email column of second row (column index 3)
print("Email from second row:", data_lines[1][3])


# ---------------------------------------------------
# EXTRACT ALL EMAIL ADDRESSES
# ---------------------------------------------------

all_emails = []

# Skip header row and collect emails from first 15 records
for line in data_lines[1:16]:
    all_emails.append(line[3])

# Display all extracted email addresses
for email in all_emails:
    print(email)


# ---------------------------------------------------
# CREATE FULL NAMES FROM FIRST AND LAST NAME COLUMNS
# ---------------------------------------------------

full_names = []

# Combine first name and last name columns
for line in data_lines[1:16]:
    full_names.append(line[1] + " " + line[2])

# Display full names
for name in full_names:
    print(name)


# ---------------------------------------------------
# WRITE DATA TO A NEW CSV FILE
# ---------------------------------------------------

# Open a CSV file in write mode
file_to_output = open(
    '14- Working with Pdf and Spreadsheets\\save_file.csv',
    mode='w',
    newline=''
)

# Create CSV writer object
csv_writer = csv.writer(file_to_output, delimiter=',')

# Write header row
csv_writer.writerow(['a', 'v', 'r'])

# Write multiple rows of data
csv_writer.writerows([
    ['g', 't', 'i'],
    ['y', 'e', 'd']
])

# Close the file
file_to_output.close()


# ---------------------------------------------------
# APPEND DATA TO EXISTING CSV FILE
# ---------------------------------------------------

# Open the same CSV file in append mode
f = open(
    '14- Working with Pdf and Spreadsheets\\save_file.csv',
    mode='a',
    newline=''
)

# Create CSV writer object
csv_writer = csv.writer(f, delimiter=',')

# Append new rows to the file
csv_writer.writerows([
    ['d', 'o', 'g'],
    ['c', 'a', 't']
])

# Close the file
f.close()
