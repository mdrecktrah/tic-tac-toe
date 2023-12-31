# Version 0.3

# Create the board
def create_board():
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]
    row3 = [7, 8, 9]
    board = [row1, row2, row3]
    return board

# Print the board
def print_board(board):
    print("")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print("")
    return board

# Check if the winning condition is met
def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return(True)
    if board[0][0] == board[1][1] == board[2][2] or\
    board[0][2] == board[1][1] == board[2][0] or\
    board[0][0] == board[1][0] == board[2][0] or\
    board[0][1] == board[1][1] == board[2][1] or\
    board[0][2] == board[1][2] == board[2][2]:
        return(True)
    
# Check if chosen spot is valid and/or still available:
def check_spot(board, spot):
    if 1 <= spot <= 3:
        idx = 0
        spot -= 1
    elif 4 <= spot <= 6:
        idx = 1
        spot -= 4
    elif 7 <= spot <= 9:
        idx = 2
        spot -= 7
    else:
        return False
    
    if board[idx][spot] == "O" or board[idx][spot] == "X":
        return False
    else:
        return True
    
# Coin toss in order to randomize which player starts the game.
def coin_toss(P1_name, P2_name):
    import random
    enabler = str(input("Would you like to randomize which player starts? (Please enter Y(es) or N(o)) ")).lower()
    if enabler == "y" or enabler == "yes":
        player_begin = random.choice([P1_name, P2_name])
        if player_begin == P2_name:
            P1_name, P2_name = P2_name, P1_name
    elif enabler == "n" or enabler == "no":
        return P1_name, P2_name
    else:
        print("Please only enter y or yes for a randomized start or n or no for a regular start.")
        coin_toss(P1_name, P2_name)
    return P1_name, P2_name

# Function to check the given input and set spot for marking
def set_mark(player_name):
    while True:
        try: 
            spot = int(input(f"{player_name}, set your mark (Choose 1-9). "))
            return spot
        except ValueError:
            print("Please only enter a full number from 1 - 9")

# Tic-tac-toe game
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe! Please enter your names.")
    P1_name = str(input("Player 1, what is your name? "))
    P2_name = str(input("Player 2, what is your name? "))
    P1_name, P2_name = coin_toss(P1_name, P2_name)
    print(f"{P1_name}, your mark in this round is 'O' and {P2_name}, your mark is 'X'.")
    
    board = create_board()
    turn = 1

    while turn <= 9:
        print_board(board)
        if turn % 2 != 0:
            #P1_set_mark = int(input(f"{P1_name}, set your mark (Choose 1-9). "))
            P1_set_mark = set_mark(P1_name)
            if check_spot(board, P1_set_mark) == False:
                print("Please choose another position.")
                continue
            else:
                for row in board:
                    for idx in row:
                        if P1_set_mark == idx:
                            if 1 <= P1_set_mark <= 3:
                                row[idx-1] = "O"
                            elif 4 <= P1_set_mark <= 6:
                                row[idx-4] = "O"
                            elif 7 <= P1_set_mark <= 9:
                                row[idx-7] = "O"
            if check_win(board) == True:
                print_board(board)
                print(f"Congratulations {P1_name}, you won!")
                break
        else:
            #P2_set_mark = int(input(f"{P2_name}, set your mark (Choose 1-9). "))
            P2_set_mark = set_mark(P2_name)
            if check_spot(board, P2_set_mark) == False:
                print("Please choose another position.")
                continue
            else:
                for row in board:
                    for idx in row:
                        if P2_set_mark == idx:
                            if 1 <= P2_set_mark <= 3:
                                row[idx-1] = "X"
                            elif 4 <= P2_set_mark <= 6:
                                row[idx-4] = "X"
                            elif 7 <= P2_set_mark <= 9:
                                row[idx-7] = "X"
            if check_win(board) == True:
                print_board(board)
                print(f"Congratulations {P2_name}, you won!")
                break
        turn += 1
    if turn == 10:
        print_board(board)
        print("You reached a draw. Let's go again!")
