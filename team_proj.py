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
