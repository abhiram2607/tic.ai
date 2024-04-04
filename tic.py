import math
# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to evaluate the board state for the AI player using a heuristic scoring function
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

# Minimax algorithm implementation with Alpha-Beta Pruning and depth-limited search
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or check_win(board, 'X') or check_win(board, 'O'):
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to determine the AI's best move using Minimax with Alpha-Beta Pruning and depth-limited search
def get_best_move(board):
    best_val = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 5, alpha, beta, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Game loop
while True:
    print_board(board)
    x, y = map(int, input("Enter your move (row col): ").split())
    if board[x][y] != ' ':
        print("Invalid move! Try again.")
        continue
    board[x][y] = 'O'

    if check_win(board, 'O'):
        print_board(board)
        print("You win!")
        break

    if all([cell != ' ' for row in board for cell in row]):
        print_board(board)
        print("It's a draw!")
        break

    ai_move = get_best_move(board)
    board[ai_move[0]][ai_move[1]] = 'X'

    if check_win(board, 'X'):
        print_board(board)
        print("AI wins!")
        break
