from collections import deque

def bfs(graph, start):
    visited = set()          # To track visited nodes
    queue = deque()          # FIFO queue

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')
