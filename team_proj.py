def read_directed_graph(file_path: str) -> dict:
    """
    (str) -> dict
    This function reads a directed graph from a file and returns it as a dictionary.
    """
    graph = {}
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip().split(',')
            if int(line[0]) in graph:
                graph[int(line[0])].append(int(line[-1]))
            if int(line[0]) not in graph:
                graph[int(line[0])]= [int(line[-1])]
            if int(line[-1]) not in graph:
                graph[int(line[-1])]= []
    sorted_keys = sorted(graph.keys())
    sorted_graph = {key: graph[key] for key in sorted_keys}
    return sorted_graph

def read_undirected_graph(file_path: str) -> dict:
    """
    (str) -> dict
    This function reads an undirected graph from a file and returns it as a dictionary.
    """
    graph = {}
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip().split(',')
            if int(line[0]) in graph:
                graph[int(line[0])].append(int(line[-1]))
            if int(line[-1]) in graph:
                graph[int(line[-1])].append(int(line[0]))
            if int(line[0]) not in graph:
                graph[int(line[0])] = [int(line[-1])]
            if int(line[-1]) not in graph:
                graph[int(line[-1])] = [int(line[0])]
    sorted_keys = sorted(graph.keys())
    sorted_graph = {key: graph[key] for key in sorted_keys}
    return sorted_graph

def write_file_directed(graph: dict, file_name: str):
    """
    (dict, str)
    This function reads a directed graph from a dictionary and writes it to a file.
    """
    write_list = []
    for key, value in graph.items():
        for elem in value:
            write_list.append([key, elem])
    with open(file_name, 'w', encoding='UTF-8') as file:
        for pair in write_list:
            if pair == write_list[-1]:
                file.write(f'{pair[0]},{pair[-1]}')
            else:
                file.write(f'{pair[0]},{pair[-1]}\n')

def write_file_undirected(graph: dict, file_name: str):
    """
    (dict, str)
    This function reads an undirected graph from a dictionary and writes it to a file.
    """
    write_list = []
    for key, value in graph.items():
        for elem in value:
            if [elem, key] in write_list:
                continue
            write_list.append([key, elem])
    with open(file_name, 'w', encoding='UTF-8') as file:
        for pair in write_list:
            if pair == write_list[-1]:
                file.write(f'{pair[0]},{pair[-1]}')
            else:
                file.write(f'{pair[0]},{pair[-1]}\n')
