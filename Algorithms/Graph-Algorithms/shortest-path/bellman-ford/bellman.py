from typing import Dict, List, Tuple, Optional
import math


def bellman_ford_adj(
    graph: Dict[int, List[Tuple[int, float]]],  # {u: [(v, w), ...]}
    source: int
) -> Tuple[Optional[Dict[int, float]], Optional[Dict[int, int]], Optional[str]]:
    """
    Bellman-Ford using adjacency list representation
    """
    # Get all vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for v, _ in neighbors:
            vertices.add(v)
    
    distance = {v: math.inf for v in vertices}
    distance[source] = 0
    
    predecessor = {v: None for v in vertices}
    
    # Relax |V|-1 times
    for _ in range(len(vertices) - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u]:
                if (distance[u] != math.inf and 
                    distance[u] + weight < distance[v]):
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
                    updated = True
        if not updated:
            break
    
    # Check for negative cycle
    for u in graph:
        for v, weight in graph[u]:
            if (distance[u] != math.inf and 
                distance[u] + weight < distance[v]):
                return None, None, "Negative cycle detected"
    
    return distance, predecessor, None


# Example usage - adjacency list version
if __name__ == "__main__":
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 2)],
        2: [(3, -3)],
        3: []
    }
    
    distances, prev, error = bellman_ford_adj(graph, 0)
    
    if error:
        print(error)
    else:
        print("Vertex  Distance  Predecessor")
        for v in sorted(distances.keys()):
            print(f"{v:6}  {distances[v]:8.1f}  {prev[v]}")