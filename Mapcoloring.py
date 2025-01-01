regions = ['A', 'B', 'C', 'D']
adjacencies = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

colors = ['Red', 'Green', 'Blue']

def is_valid_assignment(region, color, assignment):
    for neighbor in adjacencies[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [region for region in regions if region not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid_assignment(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]
    
    return None  

assignment = {}
solution = backtrack(assignment)

if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
