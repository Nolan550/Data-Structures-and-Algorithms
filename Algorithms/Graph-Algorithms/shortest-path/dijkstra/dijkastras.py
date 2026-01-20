import heapq

def dijkstra(graph, start):
   

    
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    
    priority_queue = [(0, start)]

    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        
        if current_distance > distances[current_node]:
            continue

        
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous


def get_shortest_path(previous, start, end):
  

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return []




graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

start_node = 'A'

distances, previous = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node in distances:
    print(f"{start_node} → {node} = {distances[node]}")

print("\nShortest paths:")
for node in graph:
    path = get_shortest_path(previous, start_node, node)
    print(f"{start_node} → {node} : {' -> '.join(path)}")
