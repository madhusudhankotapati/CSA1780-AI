from collections import deque

def is_valid(state):
    m_left, c_left, m_right, c_right, boat = state
    if any(x < 0 for x in (m_left, c_left, m_right, c_right)):
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_next_states(state):
    m_left, c_left, m_right, c_right, boat = state
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    next_states = []

    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals():
    initial_state = (3, 3, 0, 0, 'left')
    goal_state = (0, 0, 3, 3, 'right')

    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        if current_state in visited:
            continue

        visited.add(current_state)
        for next_state in get_next_states(current_state):
            queue.append((next_state, path + [current_state]))

    return None

if __name__ == "__main__":
    solution = solve_missionaries_cannibals()

    if solution:
        print("Solution to the Missionaries and Cannibals problem:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")
