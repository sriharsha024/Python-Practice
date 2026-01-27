"""
=============================================================================
SPECIAL METHODS (MAGIC METHODS / DUNDER METHODS)
=============================================================================
Special methods are Python methods with double underscores on both sides.
They provide hooks to define how objects behave with built-in operations.

Common Special Methods:
- __init__      : Constructor - initializes object attributes
- __str__       : Returns a string representation for str() and print()
- __repr__      : Returns official string representation (for developers)
- __len__       : Returns length for len() function
- __del__       : Destructor - called when object is deleted
- __eq__        : Defines equality comparison (==)
- __lt__        : Defines less than comparison (<)
- __add__       : Defines addition (+) operator
- __getitem__   : Allows indexing (obj[index])
=============================================================================
"""


# ============================================================================
# BOOK CLASS - DEMONSTRATING SPECIAL METHODS
# ============================================================================
class Book():
    """
    A Book class that demonstrates special methods.
    Shows how to customize string representation and behavior.
    """
    
    def __init__(self, title, author, pages):
        """
        Constructor - initializes a Book object with title, author, and pages.
        
        Args:
            title (str): The title of the book
            author (str): The author's name
            pages (int): Number of pages in the book
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        Called by print() and str() functions.
        
        Returns:
            str: Formatted book information
        """
        return f"Book Title: '{self.title}' | Author: '{self.author}' | Pages: {self.pages}"
    
    def __len__(self):
        """
        Returns the length of the book (number of pages).
        Allows len(book_object) to work.
        
        Returns:
            int: The number of pages in the book
        """
        return self.pages
    
    def __del__(self):
        """
        Destructor - called when a Book object is deleted.
        Useful for cleanup operations or logging.
        """
        print(f"Book object '{self.title}' has been deleted from memory")


# ============================================================================
# CREATE BOOK INSTANCE AND TEST SPECIAL METHODS
# ============================================================================

# Create a Book instance
book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 120)

# Test __str__ - calls __str__() method automatically
print(book_1)
# Output: Book Title: 'The Great Gatsby' | Author: 'F. Scott Fitzgerald' | Pages: 120

# Test __len__ - allows using len() function on custom object
print(len(book_1))
# Output: 120

# Test __del__ - destructor is called when object is deleted
del book_1
# Output: Book object 'The Great Gatsby' has been deleted from memory

# Attempting to access deleted object will raise NameError
# print(book_1)  # This would cause: NameError: name 'book_1' is not defined