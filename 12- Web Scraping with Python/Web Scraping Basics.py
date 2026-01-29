"""
=============================================================================
WEB SCRAPING WITH REQUESTS AND BEAUTIFULSOUP (WIKIPEDIA EXAMPLE)
=============================================================================
This script demonstrates:
- Sending HTTP requests with a custom User-Agent
- Parsing HTML using BeautifulSoup
- Extracting page title, headings, and paragraphs
- Using CSS selectors with soup.select()
- Respecting website scraping policies
=============================================================================
"""

import requests
import bs4


# ============================================================================
# 1. DEFINE TARGET URL AND HEADERS
# ============================================================================
url = "https://en.wikipedia.org/wiki/Grace_Hopper"

headers = {
    "User-Agent": "Python Web Scraper for Learning (contact: student@example.com)"
}


# ============================================================================
# 2. SEND HTTP REQUEST
# ============================================================================
response = requests.get(url, headers=headers)

print("Response object type:", type(response))
print("HTTP Status Code:", response.status_code)


# ============================================================================
# 3. PARSE HTML CONTENT
# ============================================================================
soup = bs4.BeautifulSoup(response.text, "lxml")


# ============================================================================
# 4. EXTRACT PAGE TITLE
# ============================================================================
title_tag = soup.select('title')
print("\nPage <title> tag:")
print(title_tag)
print("Title text:", title_tag[0].getText())


# ============================================================================
# 5. EXTRACT MAIN HEADING (H1)
# ============================================================================
main_heading = soup.select('h1')[0].getText()
print("\nMain Heading (H1):")
print(main_heading)


# ============================================================================
# 6. EXTRACT FIRST PARAGRAPH
# ============================================================================
first_paragraph = soup.select('p')[10].getText()
print("\nFirst Paragraph:")
print(first_paragraph)


# ============================================================================
# 7. EXAMPLE: PRINT ONLY CLEAN TEXT (NOT FULL HTML)
# ============================================================================
print("\nClean text preview (first 500 characters):")
print(soup.get_text()[6000:6500])

first_item=soup.select(".vector-toc")[0]
for item in soup.select(".vector-toc"):
    print(item.text)

image=soup.select('img')[3]
image_url = image['src']
full_image_url = "https:" + image_url
print("Full Image URL:")
print(full_image_url)
image_link = requests.get(full_image_url, headers=headers)

with open("grace_hopper.jpg", "wb") as f:
    f.write(image_link.content)

f.close()
print("Image downloaded successfully!")
