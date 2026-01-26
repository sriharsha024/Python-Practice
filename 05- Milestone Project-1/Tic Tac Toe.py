"""
=============================================================================
MILESTONE PROJECT 1 - TIC TAC TOE GAME
=============================================================================
This is a complete Tic Tac Toe game for two players (X and O).

Game Features:
- Two-player turn-based gameplay
- Input validation for position selection
- Win detection for rows, columns, and diagonals
- Tie detection when board is full
- Screen clearing for better display
- Option to play multiple games

Board Positions (1-9):
    1 | 2 | 3
   -----------
    4 | 5 | 6
   -----------
    7 | 8 | 9
=============================================================================
"""

import os


# ============================================================================
# 1. CLEAR SCREEN
# ============================================================================
def clear():
    """
    Clears the terminal screen.
    Uses 'cls' for Windows and 'clear' for Unix-like systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# ============================================================================
# 2. DISPLAY GAME BOARD
# ============================================================================
def display_board(board):
    """
    Displays the Tic Tac Toe board in a 3x3 grid format.
    Board is represented as a list of 9 elements (indices 0-8).
    
    Args:
        board (list): List of 9 elements containing 'X', 'O', or ' ' (space)
    """
    print(board[0], '|', board[1], '|', board[2])
    print('--|---|--')
    print(board[3], '|', board[4], '|', board[5])
    print('--|---|--')
    print(board[6], '|', board[7], '|', board[8])


# ============================================================================
# 3. GET VALID PLAYER POSITION
# ============================================================================
def player_choice(board):
    """
    Prompts the current player to choose a position (1-9) on the board.
    Validates that:
    1. Input is a digit between 1 and 9
    2. The chosen position is not already occupied
    
    Args:
        board (list): Current state of the game board
        
    Returns:
        int: Valid position index (0-8) for the board list
    """
    choice = ''
    while choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or board[int(choice) - 1] != ' ':
        choice = input("Choose a position (1-9): ")
    
    return int(choice) - 1  # Convert to 0-based index


# ============================================================================
# 4. PLACE PLAYER MARKER
# ============================================================================
def place_marker(board, marker, position):
    """
    Places the player's marker (X or O) at the specified position.
    
    Args:
        board (list): Current state of the game board
        marker (str): The marker to place ('X' or 'O')
        position (int): The board index where marker should be placed (0-8)
    """
    board[position] = marker


# ============================================================================
# 5. CHECK FOR WIN
# ============================================================================
def win_check(board, mark):
    """
    Checks if the specified marker has won the game.
    Checks all possible winning combinations:
    - 3 rows, 3 columns, 2 diagonals (8 total)
    
    Args:
        board (list): Current state of the game board
        mark (str): The marker to check for ('X' or 'O')
        
    Returns:
        bool: True if the marker has won, False otherwise
    """
    return (
        # Check rows
        (board[0] == board[1] == board[2] == mark) or
        (board[3] == board[4] == board[5] == mark) or
        (board[6] == board[7] == board[8] == mark) or
        # Check columns
        (board[0] == board[3] == board[6] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        # Check diagonals
        (board[0] == board[4] == board[8] == mark) or
        (board[2] == board[4] == board[6] == mark)
    )


# ============================================================================
# 6. CHECK IF BOARD IS FULL
# ============================================================================
def full_board(board):
    """
    Checks if the game board is completely filled (no empty spaces).
    
    Args:
        board (list): Current state of the game board
        
    Returns:
        bool: True if board is full, False otherwise
    """
    return ' ' not in board


# ============================================================================
# 7. ASK TO PLAY AGAIN
# ============================================================================
def replay():
    """
    Prompts the players to decide whether to play another game.
    
    Returns:
        bool: True if players want to play again, False to quit
    """
    return input("Play again? (Y/N): ").upper() == 'Y'


# ============================================================================
# MAIN GAME LOOP
# ============================================================================

print("Welcome to Tic Tac Toe!")

# Outer loop: allows multiple games
while True:
    # Initialize game state
    board = [' '] * 9  # Create empty board (9 spaces)
    current_player = 'X'  # X always starts first
    game_on = True
    
    # Inner loop: main game play
    while game_on:
        # Clear screen and display current board
        clear()
        display_board(board)
        
        # Current player's turn
        print(f"Player {current_player}'s turn")
        position = player_choice(board)
        place_marker(board, current_player, position)
        
        # Check for win
        if win_check(board, current_player):
            clear()
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_on = False
        # Check for tie
        elif full_board(board):
            clear()
            display_board(board)
            print("🤝 It's a Tie!")
            game_on = False
        # Switch player
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    
    # Ask if players want to play again
    if not replay():
        break
