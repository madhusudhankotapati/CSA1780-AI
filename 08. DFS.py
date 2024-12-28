def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    traversal = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))

    return traversal

if __name__ == "__main__":
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    result = dfs(graph, start_node)

    print("DFS traversal starting from node", start_node, ":", result)
