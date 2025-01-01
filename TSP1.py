from itertools import permutations

def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  
    return total_distance

def travelling_salesman(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    shortest_path = None
    min_distance = float('inf')

    for perm in permutations(cities):
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = perm

    return shortest_path, min_distance


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, distance = travelling_salesman(distance_matrix)
print("Shortest path:", path)
print("Minimum distance:", distance)
