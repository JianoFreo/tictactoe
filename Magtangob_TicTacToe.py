import random

def print_board(board):
    print("\n")
    print("     0   1   2")  
    print("   +---+---+---+")
    for i, row in enumerate(board):
        print(f" {i} | {' | '.join(row)} |")  
        print("   +---+---+---+")
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def computer_move(board):
    empty_cells = get_empty_cells(board)
    
    for r, c in empty_cells:
        board_copy = [row[:] for row in board]
        board_copy[r][c] = 'O'
        if check_winner(board_copy, 'O'):
            return r, c
    
    for r, c in empty_cells:
        board_copy = [row[:] for row in board]
        board_copy[r][c] = 'X'
        if check_winner(board_copy, 'X'):
            return r, c
    
    if board[1][1] == ' ':
        return 1, 1
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [pos for pos in corners if pos in empty_cells]
    if available_corners:
        return random.choice(available_corners)
    
    return random.choice(empty_cells)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!\n")
    print("You are X and the computer is O.")
    print("Enter row and column numbers (0-2) when it's your turn.\n")
    
    while True:
        print_board(board)
        
        if current_player == 'X':
            try:
                row = int(input(f"Your turn (X). Enter row (0-2): "))
                col = int(input(f"Your turn (X). Enter column (0-2): "))
            except ValueError:
                print("Please enter valid numbers (0, 1, or 2).")
                continue
            
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 0 and 2.")
                continue
            
            if board[row][col] != ' ':
                print("That square is already taken. Choose another.")
                continue
        else:
            print("Computer's turn (O)...")
            row, col = computer_move(board)
            print(f"Computer chooses row {row}, column {col}")
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

play_game()

