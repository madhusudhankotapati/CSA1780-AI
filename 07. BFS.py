from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

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
    result = bfs(graph, start_node)

    print("BFS traversal starting from node", start_node, ":", result)
