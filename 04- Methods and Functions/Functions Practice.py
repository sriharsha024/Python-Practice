"""
=============================================================================
FUNCTION PRACTICE EXERCISES
=============================================================================
This module contains practice functions covering:
- Conditional logic with even/odd numbers
- String comparison and manipulation
- Numeric comparisons and ranges
- List operations and reversing
- Pattern matching in sequences
- String repetition
- Game logic (Blackjack)
=============================================================================
"""


# ============================================================================
# 1. LESSER OF TWO EVENS
# ============================================================================
def lesser_of_two_evens(a, b):
    """
    Returns the lesser of two numbers if both are even.
    If either is odd, returns the greater of the two.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Lesser value if both even, otherwise greater value
    """
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))  # Output: 2 (both even, return lesser)
print(lesser_of_two_evens(2, 5))  # Output: 5 (one odd, return greater)


# ============================================================================
# 2. ANIMAL CRACKERS - CHECK MATCHING FIRST LETTERS
# ============================================================================
def animal_crackers(txt):
    """
    Checks if two words in a string start with the same letter (case-insensitive).
    
    Args:
        txt (str): String containing two words separated by space
        
    Returns:
        bool: True if first letters match, False otherwise
    """
    words = txt.split()
    return words[0][0].lower() == words[1][0].lower()


print(animal_crackers('Levelheaded Llama'))  # Output: True (L and L match)
print(animal_crackers('Crazy Kangaroo'))     # Output: False (C and K don't match)


# ============================================================================
# 3. MAKES TWENTY - CHECK IF NUMBERS SUM TO 20
# ============================================================================
def makes_twenty(n1, n2):
    """
    Checks if either number equals 20 or if they sum to 20.
    
    Args:
        n1 (int): First number
        n2 (int): Second number
        
    Returns:
        bool: True if conditions are met, False otherwise
    """
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False


print(makes_twenty(10, 20))  # Output: True (20 in list)
print(makes_twenty(2, 3))    # Output: False (no condition met)
print(makes_twenty(12, 8))   # Output: True (sum equals 20)


# ============================================================================
# 4. OLD MACDONALD - ALTERNATE CASE STRING MANIPULATION
# ============================================================================
def old_macdonald(name):
    """
    Capitalizes alternating characters in a name (1st, 4th, 7th, etc.).
    Returns an error if name is too short.
    
    Args:
        name (str): Name to process
        
    Returns:
        str: Name with alternating capitalization, or error message
    """
    if len(name) < 4:
        return "Name is too short!"
    else:
        return name[0].upper() + name[1:3] + name[3].upper() + name[4:]


print(old_macdonald('macdonald'))  # Output: MacDonald


# ============================================================================
# 5. MASTER YODA - REVERSE WORD ORDER
# ============================================================================
def master_yoda(string):
    """
    Reverses the order of words in a string (Yoda-style).
    
    Args:
        string (str): String with words separated by spaces
        
    Returns:
        list: List of words in reversed order
    """
    stringlist = string.split(" ")
    stringlist.reverse()
    result = []
    for s in stringlist:
        result.append(s)
    return result


print(master_yoda('I am home'))  # Output: ['home', 'am', 'I']


# ============================================================================
# 6. ALMOST THERE - CHECK PROXIMITY TO 100 OR 200
# ============================================================================
def almost_there(n):
    """
    Checks if a number is within 10 of 100 or 200.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if within 10 of 100 or 200, False otherwise
    """
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(104))  # Output: True (within 10 of 100)
print(almost_there(150))  # Output: False (not close to either)
print(almost_there(209))  # Output: True (within 10 of 200)


# ============================================================================
# 7. HAS 33 - CHECK FOR CONSECUTIVE 3s
# ============================================================================
def has_33(nums):
    """
    Checks if a list contains two consecutive 3s.
    
    Args:
        nums (list): List of integers
        
    Returns:
        bool: True if consecutive 3s found, False otherwise
    """
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))      # Output: True (consecutive 3s)
print(has_33([1, 3, 1, 3]))   # Output: False (3s not consecutive)
print(has_33([3, 1, 3]))      # Output: False (3s separated)


# ============================================================================
# 8. PAPER DOLL - REPEAT EACH CHARACTER
# ============================================================================
def paper_doll(string):
    """
    Repeats each character in a string 3 times.
    
    Args:
        string (str): Input string
        
    Returns:
        str: String with each character repeated 3 times
    """
    result = ''
    for char in string:
        result += char * 3
    return result


print(paper_doll("Hello"))  # Output: HHHeeellllllooo


# ============================================================================
# 9. BLACK JAR (BLACKJACK) - GAME LOGIC
# ============================================================================
def black_jar(n1, n2, n3):
    """
    Simple Blackjack game logic for 3 cards.
    - If sum <= 21, return the sum
    - If sum > 21 and an Ace (11) is present, return sum - 10
    - If sum > 21 with no Ace, return "BUST"
    
    Args:
        n1 (int): First card value
        n2 (int): Second card value
        n3 (int): Third card value
        
    Returns:
        int or str: Hand value or "BUST"
    """
    result = n1 + n2 + n3
    
    if result <= 21:
        return result
    elif result > 21 and (n1 == 11 or n2 == 11 or n3 == 11):
        return result - 10
    elif result > 21:
        return "BUST"


print(black_jar(5, 6, 7))    # Output: 18 (within limit)
print(black_jar(9, 9, 11))   # Output: 19 (Ace reduces hand)
print(black_jar(9, 9, 9))    # Output: BUST (over 21, no Ace)


# ============================================================================
# 10. COUNT PRIMES - COUNT PRIME NUMBERS UP TO N
# ============================================================================
def count_primes(num):
    """
    Counts the number of prime numbers less than or equal to the given number.
    A prime number is only divisible by 1 and itself.
    
    Args:
        num (int): The upper limit (inclusive) for counting primes
        
    Returns:
        int: The count of prime numbers up to and including num
    """
    count = 0

    # Base case: No primes less than 2
    if num < 2:
        return 0

    # Check each number from 2 to num
    for n in range(2, num + 1):
        is_prime = True
        
        # Check if n is divisible by any number from 2 to sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        
        # If n is still prime, increment counter
        if is_prime:
            count += 1
    
    return count


# Test count_primes function
print(count_primes(10))   # Output: 4 (primes: 2, 3, 5, 7)
print(count_primes(25))   # Output: 9 (primes: 2, 3, 5, 7, 11, 13, 17, 19, 23)
print(count_primes(100))
