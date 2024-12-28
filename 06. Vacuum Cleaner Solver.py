def vacuum_cleaner(start_state, goal_state):
    from collections import deque

    n = len(start_state)
    queue = deque([(start_state, 0, [])])  # (state, position, path)
    visited = set()

    while queue:
        current_state, position, path = queue.popleft()

        if current_state == goal_state:
            return path

        if (tuple(current_state), position) in visited:
            continue

        visited.add((tuple(current_state), position))

        # Clean current position if dirty
        if current_state[position] == 1:
            new_state = current_state[:]
            new_state[position] = 0
            queue.append((new_state, position, path + [f"Clean room {position}"]))

        # Move to the left
        if position > 0:
            queue.append((current_state, position - 1, path + [f"Move left to room {position - 1}"]))

        # Move to the right
        if position < n - 1:
            queue.append((current_state, position + 1, path + [f"Move right to room {position + 1}"]))

    return None

if __name__ == "__main__":
    initial_state = [1, 0, 1, 1, 0]  # Example: 1 is dirty, 0 is clean
    goal_state = [0] * len(initial_state)  # All rooms clean

    solution = vacuum_cleaner(initial_state, goal_state)

    if solution:
        print("Solution to the Vacuum Cleaner problem:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
