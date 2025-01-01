import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name          
        self.parent = parent     
        self.g = g                
        self.h = h      
        self.f = g + h           

    def __lt__(self, other):
        return self.f < other.f


def a_star(graph, start, goal, heuristic):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, g=0, h=heuristic[start])
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list) 
        
        
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  
        
        closed_list.add(current_node.name)
        
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue
            g = current_node.g + cost
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, parent=current_node, g=g, h=h)
            
            if not any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0  
}

start = 'A'
goal = 'D'
path = a_star(graph, start, goal, heuristic)

if path:
    print(f"Path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}.")
