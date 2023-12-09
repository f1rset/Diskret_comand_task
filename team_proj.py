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
