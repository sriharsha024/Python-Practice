import PyPDF2

# ---------------------------------------------------
# READ PDF AND EXTRACT TEXT FROM FIRST PAGE
# ---------------------------------------------------

# Open the PDF file in binary read mode
file = open(
    '14- Working with Pdf and Spreadsheets\\Working_Business_Proposal.pdf',
    'rb'
)

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(file)

# Print total number of pages in the PDF
print("Total pages in PDF:", len(pdf_reader.pages))

# Access the first page (index starts from 0)
page_one = pdf_reader.pages[0]

# Extract text from the first page
page_one_text = page_one.extract_text()

# Display extracted text
print(page_one_text)

# Close the file after reading
file.close()


# ---------------------------------------------------
# CREATE A NEW PDF USING THE FIRST PAGE
# ---------------------------------------------------

# Reopen the original PDF
file = open(
    '14- Working with Pdf and Spreadsheets\\Working_Business_Proposal.pdf',
    'rb'
)

# Read the PDF again
pdf_reader = PyPDF2.PdfReader(file)

# Get the first page
page_one = pdf_reader.pages[0]

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Print the type of page object
print("Page object type:", type(page_one))

# Add the first page to the new PDF
pdf_writer.add_page(page_one)

# Open a new PDF file in write-binary mode
pdf_output = open(
    '14- Working with Pdf and Spreadsheets\\New_Doc.pdf',
    'wb'
)

# Write the page into the new PDF file
pdf_writer.write(pdf_output)

# Close all open files
file.close()
pdf_output.close()


# ---------------------------------------------------
# EXTRACT TEXT FROM ALL PAGES
# ---------------------------------------------------

# Open the PDF file again
file = open(
    '14- Working with Pdf and Spreadsheets\\Working_Business_Proposal.pdf',
    'rb'
)

# Create PDF reader object
pdf_reader = PyPDF2.PdfReader(file)

# List to store text from each page
pdf_text = []

# Loop through all pages in the PDF
for page_number in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_number]
    text = page.extract_text()
    pdf_text.append(text)

# Close the file
file.close()

# Print text of the first page as sample output
print("Text from page 1:")
print(pdf_text[0])
