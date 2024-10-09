TASK 2:

import math

# Initialize the game board (3x3 grid)
def create_board():
    return [' ' for _ in range(9)]

# Display the current game board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check if the game board is full (draw)
def check_draw(board):
    return ' ' not in board

# Evaluate the game board (return scores)
def evaluate(board):
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1 # Human wins
    else:
        return 0  # Draw

# Minimax function with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)
    
    # If the game is over, return the score
    if score == 1 or score == -1 or check_draw(board):
        return score
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_move = -1
    best_value = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_value = minimax(board, 0, False)
            board[i] = ' '
            if move_value > best_value:
                best_move = i
                best_value = move_value
    return best_move

# Main game loop
def play_game():
    board = create_board()
    human_turn = True
    print("Tic-Tac-Toe: Human is 'X', AI is 'O'")
    print_board(board)

    while True:
        # Human turn
        if human_turn:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                human_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is making a move...")
            move = find_best_move(board)
            board[move] = 'O'
            human_turn = True
        
        print_board(board)

        # Check for a winner or draw
        if check_winner(board, 'X'):
            print("Human wins!")
            break
        elif check_winner(board, 'O'):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()

OUTPUT:

Tic-Tac-Toe: Human is 'X', AI is 'O'
|   |   |   |
|   |   |   |
|   |   |   |
Enter your move (1-9): 3
|   |   | X |
|   |   |   |
|   |   |   |
AI is making a move...
|   |   | X |
|   | O |   |
|   |   |   |
Enter your move (1-9): 7
|   |   | X |
|   | O |   |
| X |   |   |
AI is making a move...
|   | O | X |
|   | O |   |
| X |   |   |
Enter your move (1-9): 8
|   | O | X |
|   | O |   |
| X | X |   |
AI is making a move...
|   | O | X |
|   | O |   |
| X | X | O |
Enter your move (1-9): 1
| X | O | X |
|   | O |   |
| X | X | O |
AI is making a move...
| X | O | X |
| O | O |   |
| X | X | O |
Enter your move (1-9): 6
| X | O | X |
| O | O | X |
| X | X | O |
It's a draw!

=== Code Execution Successful ===