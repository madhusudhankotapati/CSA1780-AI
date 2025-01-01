X = 'X'
O = 'O'
EMPTY = ' '

def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]
    
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def is_game_over(board):
    return check_winner(board, X) or check_winner(board, O) or all(space != EMPTY for space in board)

def evaluate(board):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing_player):
    if is_game_over(board):
        return evaluate(board)
    
    if is_maximizing_player:
        best = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = X
                best = max(best, minimax(board, depth + 1, False))
                board[i] = EMPTY
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = O
                best = min(best, minimax(board, depth + 1, True))
                board[i] = EMPTY
        return best

def find_best_move(board):
    best_value = -float('inf')
    best_move = -1
    
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = X
            move_value = minimax(board, 0, False)
            board[i] = EMPTY
            
            if move_value > best_value:
                best_value = move_value
                best_move = i
                
    return best_move

def print_board(board):
    for i in range(3):
        print(board[i*3:(i+1)*3])

def play_game():
    board = [EMPTY] * 9  
    print("Tic-Tac-Toe: X goes first\n")
    
    while not is_game_over(board):
        print_board(board)
        
        if board.count(EMPTY) % 2 == 1:  
            print("\nPlayer X's turn:")
            move = find_best_move(board)
            board[move] = X
        else:  
            print("\nPlayer O's turn:")
            move = int(input("Enter your move (0-8): "))
            board[move] = O
        
    print_board(board)
    
    if check_winner(board, X):
        print("Player X wins!")
    elif check_winner(board, O):
        print("Player O wins!")
    else:
        print("It's a draw!")

play_game()
