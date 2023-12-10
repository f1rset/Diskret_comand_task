import copy

def strong_coherence_oriented(graph: dict) -> list:
    """Searches for strong coherence in oriendet graph
    It uses Kosarag's algorithm

    Args:
        graph (dict): G - oriented graph

    Returns:
        list: strong coherence
    """
    #_______________________________________
    def dfs(graph_dfs: dict, v: int, visited: dict, stack: list):
        """Searches for dfs in graph

        Args:
            graph (dict): G - oriented graph
            v (int): vertix
            visited (dict): if visited true, else False
            stack (list): list of stack
        """
        visited[v] = True
        for i in graph_dfs[v]:
            if not visited[i]:
                dfs(graph_dfs, i, visited, stack)
        stack.append(v)
    #________________________________________
    def transpose(graph_to_transpose):
        """Function transposes graph

        Args:
            graph (dict): G - oriented graph

        Returns:
            dict: transposed graph
        """
        transposed_graph = {}
        for key in graph_to_transpose.keys():
            transposed_graph[key] = []
        for i in graph_to_transpose:
            for j in graph_to_transpose[i]:
                transposed_graph[j].append(i)
        return transposed_graph
    #_________________________________________
    vertices = list(graph.keys())
    stack: list = []
    visited = {}
    for i in vertices:
        visited[i] = False
    for i in vertices:
        if not visited[i]:
            dfs(graph, i, visited, stack)
    transposed_graph = transpose(graph)
    visited = {}
    for i in vertices:
        visited[i] = False
    result = []
    while stack:
        i = stack.pop()
        if not visited[i]:
            temp: list = []
            dfs(transposed_graph, i, visited, temp)
            result.append(temp)
    return result

def find_components(graph: dict[int, list[int]])->list:
    """
    >>> find_components({1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4], 6: [7], 7: [6]})
    [1, 4, 6]
    >>> find_components({1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4]})
    [1, 4]
    >>> find_components({
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
    ... })
    [0]
    """
    def dfs(graf: dict[int, list[int]], start)->list:
        visited = []
        result = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                result.append(vertex)
                for neighbor in reversed(graf[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    visited = []
    components = []
    for start in graph:
        if start not in visited:
            comp = dfs(graph, start)
            components.append(min(comp))
            for i in comp:
                visited.append(i)
    return components

"""This function finds all the connecting points of an undirected graph"""
def find_con_points(graph):
    """
    finds all the connecting points of an undirected graph
    >>> find_con_points({0: [1], 1: [0, 2, 3, 5], 2: [1, 3, 4, 5],\
 3: [1, 2, 4], 4: [2, 3, 5], 5: [2, 4, 1, 6], 6:[5]})
    [1, 5]
    >>> find_con_points({
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
    ... })
    [4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29, 32, 33, 36, 37, 40, 41, 44, 45, 48,\
 49, 52, 53, 56, 57, 60, 61, 64, 65, 68, 69, 72, 73, 76, 77, 80, 81, 84, 85, 88, 89, 92, 93, 96, 97]
    """
    def dfs_mod(graph: dict[int, list[int]], source: int, destination: int) -> bool:
        result = []
        def ggg(current):
            if current not in result:
                result.append(current)
                for neighbour in graph[current]:
                    ggg(neighbour)
        ggg(source)
        return destination in result
    con_points=[]
    graph_copy=copy.deepcopy(graph)
    for i in copy.deepcopy(graph):
        del graph_copy[i]
        graph_copy={l : [m for m in graph_copy[l] if m!=i] for l in graph_copy}
        if not dfs_mod(graph_copy,list(graph_copy.keys())[0],list(graph_copy.keys())[-1]):
            con_points.append(i)
        graph_copy=copy.deepcopy(graph)
    return con_points
