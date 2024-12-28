def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"{len(solutions)} solutions found for {n}-Queens problem:\n")
    for solution in solutions:
        print_solution(solution)
