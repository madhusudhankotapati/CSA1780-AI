from collections import deque

def water_jug_bfs(capacity, target):
    a, b = capacity
    visited = set()
    queue = deque([((0, 0), [])])  # ((current state of jugs), path)

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            return path

        # Generate possible moves
        possible_moves = [
            (a, jug2),  # Fill Jug 1
            (jug1, b),  # Fill Jug 2
            (0, jug2),  # Empty Jug 1
            (jug1, 0),  # Empty Jug 2
            (jug1 - min(jug1, b - jug2), jug2 + min(jug1, b - jug2)),  # Pour Jug 1 -> Jug 2
            (jug1 + min(jug2, a - jug1), jug2 - min(jug2, a - jug1)),  # Pour Jug 2 -> Jug 1
        ]

        for move in possible_moves:
            if move not in visited:
                queue.append((move, path))

    return None

if __name__ == "__main__":
    jug_capacity = (4, 3)  # Capacities of the two jugs
    target_amount = 2  # Target amount of water

    solution = water_jug_bfs(jug_capacity, target_amount)

    if solution:
        print("Solution to the Water Jug Problem:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")
