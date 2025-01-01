def print_board(board):
    print("Current board:")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")
    print()

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]  
    current_player = 'X'

    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
