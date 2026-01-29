"""
=============================================================================
WEB SCRAPING PRACTICE WITH REQUESTS & BEAUTIFULSOUP
=============================================================================
This script demonstrates web scraping concepts using two popular practice sites:
1. books.toscrape.com   → Scraping book ratings and titles
2. quotes.toscrape.com  → Scraping quotes, authors, tags, and pagination

Concepts Covered:
- Sending HTTP requests using requests
- Parsing HTML with BeautifulSoup
- CSS selectors using .select() and .select_one()
- Pagination handling with while loop
- Extracting unique values using Python sets
=============================================================================
"""

import requests
import bs4


# ============================================================================
# PART 1: SCRAPING BOOKS WITH TWO-STAR RATING (COMMENTED FOR REFERENCE)
# ============================================================================

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
two_star_titles = []

# Loop through first 20 pages
for i in range(1, 21):
    result = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(result.text, "lxml")

    # Select all book containers
    books = soup.select(".product_pod")

    for book in books:
        # Check if book has a Two-star rating
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select_one("h3 a")["title"]
            two_star_titles.append(book_title)

# Print collected book titles
for title in two_star_titles:
    print(title)



# ============================================================================
# PART 2: BASIC SCRAPING FROM QUOTES.TOSCRAPE.COM (SINGLE PAGE)
# ============================================================================
print("\n=== Scraping First Page of Quotes ===\n")

response = requests.get("https://quotes.toscrape.com/")


soup = bs4.BeautifulSoup(response.text, "lxml")

# Extract and display all authors on the page
print("Authors on page:")
authors = soup.select(".author")
for author in authors:
    print(author.text)

# Extract and display all quotes
print("\nQuotes on page:")
quotes = soup.select(".text")
for quote in quotes:
    print(quote.text)

# Extract and display all tags
print("\nTags on page:")
tags = soup.select(".tag")
for tag in tags:
    print(tag.text)


# ============================================================================
# PART 3: SCRAPING ALL UNIQUE AUTHORS USING PAGINATION
# ============================================================================
print("\n=== Collecting ALL Unique Authors Across Pages ===\n")

base_url_1 = "https://quotes.toscrape.com/page/{}/"
unique_authors = set()
page = 1

# Loop through pages until no more content is available
while True:
    result = requests.get(base_url_1.format(page))

    # Stop if page does not exist
    if result.status_code != 200:
        break

    soup = bs4.BeautifulSoup(result.text, "lxml")

    authors = soup.select(".author")

    # Stop if no authors found (extra safety)
    if len(authors) == 0:
        break

    # Add authors to set (ensures uniqueness)
    for author in authors:
        unique_authors.add(author.text.strip())

    page += 1


# ============================================================================
# FINAL OUTPUT
# ============================================================================
print("Unique Authors Found:")
for author in sorted(unique_authors):
    print(author)

print(f"\nTotal Unique Authors: {len(unique_authors)}")
