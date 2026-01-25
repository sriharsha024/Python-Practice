"""
=============================================================================
SIMPLE GUESSING GAME
=============================================================================
This is a simple number guessing game where:
- A player picks one of three positions (0, 1, or 2)
- One position contains 'O' (correct answer)
- The other positions contain spaces
- The list is shuffled before the player guesses
=============================================================================
"""

from random import shuffle


# ============================================================================
# FUNCTION 1: SHUFFLE LIST
# ============================================================================
def shuffle_list(mylist):
    """
    Shuffles the given list in place using random.shuffle().
    
    Args:
        mylist (list): The list to shuffle
        
    Returns:
        list: The shuffled list
    """
    shuffle(mylist)
    return mylist


# ============================================================================
# FUNCTION 2: GET PLAYER GUESS
# ============================================================================
def player_guess():
    """
    Prompts the player to guess a number (0, 1, or 2).
    Validates input and keeps asking until valid input is received.
    
    Returns:
        int: Player's guess (0, 1, or 2)
    """
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Enter a number 0, 1 or 2: ")

    return int(guess)


# ============================================================================
# FUNCTION 3: CHECK PLAYER'S GUESS
# ============================================================================
def check_guess(mylist, guess):
    """
    Checks if the player's guess matches the correct position.
    The correct position contains 'O'.
    
    Args:
        mylist (list): The shuffled list with the answer
        guess (int): Player's guessed position (0, 1, or 2)
    """
    if mylist[guess] == 'O':
        print("Correct Guess!")
    else:
        print("Wrong Guess! Try Again.")
        print(mylist)


# ============================================================================
# MAIN GAME LOGIC
# ============================================================================

# Initialize the game list with one 'O' (correct answer) and empty spaces
mylist = [' ', 'O', ' ']

# Shuffle the list so the player doesn't know where 'O' is
mixedup_list = shuffle_list(mylist)

# Get the player's guess
guess = player_guess()

# Check if the guess is correct
check_guess(mixedup_list, guess)