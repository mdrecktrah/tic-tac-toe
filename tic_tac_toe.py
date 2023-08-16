"""
Pseudocode:
DEFINE function for start of the game:
    OUTPUT Welcome message
    INPUT Name Player 1 (Default: Player1)
    INPUT Name Player 2 (Default: Player2)
    OUTPUT basic rules
        Player1 uses symbol O
        Player2 uses symbol X
        Players take turns placing symbols

DEFINE function to create the board
    Visual idea of board:
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |

DEFINE function for turns
    CALL function for empty board
    FOR maximum of 9 turns
        REPEAT
            OUTPUT display current board
            INPUT player move
            STORE updated board
        UNTIL winning condition is met
    OUTPUT winner or draw        
"""

# Create the board
def create_board():
    board = """
        | 1 | 2 | 3 |\n
        | 4 | 5 | 6 |\n
        | 7 | 8 | 9 |
        """
    return board

# Tic-tac-toe game
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe! Please enter your names.")
    P1_name = str(input("Player 1, what is your name? "))
    P2_name = str(input("Player 2, what is your name? "))
    print(f"{P1_name}, your mark is 'O' and {P2_name}, your mark is 'X'.")
    
    board = create_board()
    print(board)
    