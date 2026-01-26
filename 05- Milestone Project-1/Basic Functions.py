"""
=============================================================================
MILESTONE PROJECT 1 - BASIC FUNCTIONS FOR TIC-TAC-TOE GAME
=============================================================================
This module contains basic helper functions for a Tic-Tac-Toe game:
- Display the game board
- Get and validate user input
=============================================================================
"""


# ============================================================================
# 1. DISPLAY GAME BOARD
# ============================================================================
def display(row1, row2, row3):
    """
    Displays the Tic-Tac-Toe game board.
    Each row is a list representing three positions on the board.
    
    Args:
        row1 (list): First row of the board with 3 elements
        row2 (list): Second row of the board with 3 elements
        row3 (list): Third row of the board with 3 elements
    """
    print(row1)
    print(row2)
    print(row3)


# Initialize the game board - each cell starts with empty space
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

# Display the initial empty board
display(row1, row2, row3)


# ============================================================================
# 2. GET AND VALIDATE USER CHOICE
# ============================================================================
def user_choice():
    """
    Prompts the user to enter a valid position (0-9) on the board.
    Validates that:
    1. Input is a digit (not letters or special characters)
    2. Input is within the acceptable range (0-9)
    
    Keeps asking until valid input is received.
    
    Returns:
        int: Valid user choice (0-9)
    """
    choice = "WRONG"
    acceptable_range = range(0, 10)  # Valid positions: 0, 1, 2, ..., 9
    within_range = False
    
    # Keep looping until valid input is received
    while choice.isdigit() == False or within_range == False:
        choice = input("Enter a number (0-9): ")
        
        # Check if input is a digit
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
        
        # Check if digit is within acceptable range
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry the digit is not in acceptable range")
                within_range = False
    
    return int(choice)


# Test the user_choice function
user_choice()