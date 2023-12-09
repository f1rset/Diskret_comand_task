import copy

def search_for_bridges(graph:dict) -> list:
    """
   Find bridges - finds all bridges in an undirected graph (returns a list of edges,
each edge is an ordered pair of points).
    >>> search_for_bridges({1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], \
5: [4, 6], 6: [5, 7], 7: [6]})
    [[3, 4], [4, 5], [5, 6], [6, 7]]
    """
    res = []
    edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            if [neighbor, vertex] not in edges:
                edges.append([vertex, neighbor])
    min_vertex = min(graph)
    max_vertex = max(graph)
    edges_copy = copy.deepcopy(edges)
    for val in edges:
        edges_copy.remove(val)
        if not find_path(len(graph)+1, edges_copy, min_vertex, max_vertex):
            res.append(val)
        edges_copy.append(val)
    return res

def find_path(n: int, edges: list, source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 4], [3, 5], [4, 5]], 1, 5)
    True
    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 2], [3, 5], [4, 5]], 1, 5)
    False
    """
    graph = {i: [] for i in range(n)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited = [False] * n

    def neighbor_search(vertex):
        if vertex == destination:
            return True
        visited[vertex] = True
        return any(neighbor_search(neighbor) for neighbor in graph[vertex] if not visited[neighbor])

    return neighbor_search(source)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
