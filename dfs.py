def get_dfs(adj_list):
    '''
    return DFS for given adjacency list
    '''
    parent = {}

    def walk_node(u):
        '''
        Recursivly visit each node
        '''
        # iterate through the adjacency list of the node
        for v in adj_list[u]:
            # Check if node is not visited
            if v not in parent:
                parent[v] = u
                walk_node(v)

    # Iterate through each node in the list
    for node in adj_list:
        # Check if node is not visited
        if node not in parent:
            parent[node] = None
            walk_node(node)

    return parent

adj_list = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': ['f'],
        'd': [],
        'e': [],
        's': [],
        'f': []
        }

print get_dfs(adj_list)
