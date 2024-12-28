from heapq import heappush, heappop

def manhattan_distance(board):
    return sum(abs(i // 3 - (val - 1) // 3) + abs(i % 3 - (val - 1) % 3)
               for i, val in enumerate(sum(board, [])) if val)

def swap(board, x1, y1, x2, y2):
    new_board = [row[:] for row in board]
    new_board[x1][y1], new_board[x2][y2] = new_board[x2][y2], new_board[x1][y1]
    return new_board

def find_zero(board):
    for i, row in enumerate(board):
        if 0 in row:
            return i, row.index(0)

def a_star_search(initial_board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    open_set = [(manhattan_distance(initial_board), 0, initial_board, None)]
    visited = set()

    while open_set:
        _, moves, current_board, previous = heappop(open_set)
        if current_board == goal:
            return reconstruct_path(current_board, previous)
        visited.add(str(current_board))

        x, y = find_zero(current_board)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor = swap(current_board, x, y, nx, ny)
                if str(neighbor) not in visited:
                    heappush(open_set, (moves + 1 + manhattan_distance(neighbor), moves + 1, neighbor, (current_board, previous)))

    return None

def reconstruct_path(board, previous):
    path = []
    while board:
        path.append(board)
        board, previous = previous if previous else (None, None)
    return path[::-1]

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    solution = a_star_search(initial_board)

    if solution:
        print(f"Solution found in {len(solution) - 1} moves:\n")
        for step in solution:
            print('\n'.join(' '.join(map(str, row)) for row in step) + '\n')
    else:
        print("No solution found.")
