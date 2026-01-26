"""
=============================================================================
MILESTONE PROJECT 1 - POSITION REPLACEMENT GAME
=============================================================================
This is an interactive game where:
1. Player sees a list of positions
2. Player chooses a position (0, 1, or 2)
3. Player enters a value to place at that position
4. The list is updated and displayed
5. Player can choose to continue or quit

This is a simple precursor to the Tic-Tac-Toe game.
=============================================================================
"""


# ============================================================================
# 1. DISPLAY GAME LIST
# ============================================================================
def display_game(game_list):
    """
    Displays the current state of the game list.
    Shows the player what values are at each position.
    
    Args:
        game_list (list): The current state of the game list
    """
    print("Here is the current list: ")
    print(game_list)


# ============================================================================
# 2. GET VALID POSITION CHOICE
# ============================================================================
def position_choice():
    """
    Prompts the player to choose a position (0, 1, or 2).
    Validates input and keeps asking until valid choice is received.
    
    Returns:
        int: Valid position choice (0, 1, or 2)
    """
    choice = 'wrong'
    
    # Keep asking until valid position is chosen
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0, 1, 2): ")
        
        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice")
    
    return int(choice)


# ============================================================================
# 3. GET REPLACEMENT VALUE AND UPDATE LIST
# ============================================================================
def replacement_choice(game_list, position):
    """
    Prompts the player to enter a value to place at the chosen position.
    Updates the game list with the new value.
    
    Args:
        game_list (list): The current state of the game list
        position (int): The position to update (0, 1, or 2)
        
    Returns:
        list: The updated game list
    """
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list


# ============================================================================
# 4. ASK IF PLAYER WANTS TO CONTINUE
# ============================================================================
def gameon_choice():
    """
    Prompts the player to decide whether to continue or quit the game.
    Validates input (Y or N) and keeps asking until valid choice is received.
    
    Returns:
        bool: True to continue playing, False to quit
    """
    choice = 'wrong'
    
    # Keep asking until valid choice is made
    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N): ")
        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand. Please choose Y or N")
    
    # Convert Y/N to boolean
    if choice == 'Y':
        return True
    else:
        return False


# ============================================================================
# MAIN GAME LOOP
# ============================================================================

game_on = True
game_list = [0, 1, 2]  # Initialize list with positions 0, 1, 2

# Main game loop - continues while player wants to play
while game_on:
    # Display current game state
    display_game(game_list)
    
    # Get player's position choice
    position = position_choice()
    
    # Get replacement value and update the list
    game_list = replacement_choice(game_list, position)
    
    # Display updated game state
    display_game(game_list)
    
    # Ask if player wants to continue
    game_on = gameon_choice()