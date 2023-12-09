import copy

def search_for_bridges(graph:dict) -> list:
    """
   Find bridges - finds all bridges in an undirected graph (returns a list of edges,
each edge is an ordered pair of points).
    >>> search_for_bridges({1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], \
5: [4, 6], 6: [5, 7], 7: [6]})
    [[3, 4], [4, 5], [5, 6], [6, 7]]
    >>> graph = {
    ...     0: [1, 2, 3],
    ...     1: [0, 2, 3, 4],
    ...     2: [0, 1, 3, 4],
    ...     3: [0, 1, 2, 4],
    ...     4: [1, 2, 3, 5],
    ...     5: [4, 6, 7],
    ...     6: [5, 7, 8],
    ...     7: [5, 6, 8],
    ...     8: [6, 7, 9],
    ...     9: [8, 10, 11],
    ...     10: [9, 11, 12],
    ...     11: [9, 10, 12],
    ...     12: [10, 11, 13],
    ...     13: [12, 14, 15],
    ...     14: [13, 15, 16],
    ...     15: [13, 14, 16],
    ...     16: [14, 15, 17],
    ...     17: [16, 18, 19],
    ...     18: [17, 19, 20],
    ...     19: [17, 18, 20],
    ...     20: [18, 19, 21],
    ...     21: [20, 22, 23],
    ...     22: [21, 23, 24],
    ...     23: [21, 22, 24],
    ...     24: [22, 23, 25],
    ...     25: [24, 26, 27],
    ...     26: [25, 27, 28],
    ...     27: [25, 26, 28],
    ...     28: [26, 27, 29],
    ...     29: [28, 30, 31],
    ...     30: [29, 31, 32],
    ...     31: [29, 30, 32],
    ...     32: [30, 31, 33],
    ...     33: [32, 34, 35],
    ...     34: [33, 35, 36],
    ...     35: [33, 34, 36],
    ...     36: [34, 35, 37],
    ...     37: [36, 38, 39],
    ...     38: [37, 39, 40],
    ...     39: [37, 38, 40],
    ...     40: [38, 39, 41],
    ...     41: [40, 42, 43],
    ...     42: [41, 43, 44],
    ...     43: [41, 42, 44],
    ...     44: [42, 43, 45],
    ...     45: [44, 46, 47],
    ...     46: [45, 47, 48],
    ...     47: [45, 46, 48],
    ...     48: [46, 47, 49],
    ...     49: [48, 50, 51],
    ...     50: [49, 51, 52],
    ...     51: [49, 50, 52],
    ...     52: [50, 51, 53],
    ...     53: [52, 54, 55],
    ...     54: [53, 55, 56],
    ...     55: [53, 54, 56],
    ...     56: [54, 55, 57],
    ...     57: [56, 58, 59],
    ...     58: [57, 59, 60],
    ...     59: [57, 58, 60],
    ...     60: [58, 59, 61],
    ...     61: [60, 62, 63],
    ...     62: [61, 63, 64],
    ...     63: [61, 62, 64],
    ...     64: [62, 63, 65],
    ...     65: [64, 66, 67],
    ...     66: [65, 67, 68],
    ...     67: [65, 66, 68],
    ...     68: [66, 67, 69],
    ...     69: [68, 70, 71],
    ...     70: [69, 71, 72],
    ...     71: [69, 70, 72],
    ...     72: [70, 71, 73],
    ...     73: [72, 74, 75],
    ...     74: [73, 75, 76],
    ...     75: [73, 74, 76],
    ...     76: [74, 75, 77],
    ...     77: [76, 78, 79],
    ...     78: [77, 79, 80],
    ...     79: [77, 78, 80],
    ...     80: [78, 79, 81],
    ...     81: [80, 82, 83],
    ...     82: [81, 83, 84],
    ...     83: [81, 82, 84],
    ...     84: [82, 83, 85],
    ...     85: [84, 86, 87],
    ...     86: [85, 87, 88],
    ...     87: [85, 86, 88],
    ...     88: [86, 87, 89],
    ...     89: [88, 90, 91],
    ...     90: [89, 91, 92],
    ...     91: [89, 90, 92],
    ...     92: [90, 91, 93],
    ...     93: [92, 94, 95],
    ...     94: [93, 95, 96],
    ...     95: [93, 94, 96],
    ...     96: [94, 95, 97],
    ...     97: [96, 98, 99],
    ...     98: [97, 99, 100],
    ...     99: [97, 98, 100],
    ...     100: [99, 98, 97]
    ... }
    >>> search_for_bridges(graph)
    [[4, 5], [8, 9], [12, 13], [16, 17], [20, 21], [24, 25], [28, 29], [32, 33], \
[36, 37], [40, 41], [44, 45], [48, 49], [52, 53], [56, 57], [60, 61], [64, 65], \
[68, 69], [72, 73], [76, 77], [80, 81], [84, 85], [88, 89], [92, 93], [96, 97]]
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
        # if (val[0]==min_vertex and len(graph[min_vertex]) > 1
        #     ) or (val[1]==max_vertex and len(graph[max_vertex]) > 1):
        #     continue
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
