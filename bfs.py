def get_bfs(adj_list, start_node):
    '''
    return BFS for given adjacency list and starting node
    '''
    result = {}
    # set the start node parent to None
    # and level to 0
    result[start_node] = {
        'parent': None,
        'level': 0
    }
    current = [start_node]
    i = 1
    while current:
        next = []
        # iterate through the current node
        for u in current:
            # iterate through the adjacency list of the current node
            # provided the currrent node is not visited
            for v in [x for x in adj_list[u] if x not in result]:
                # set the v node parent to u
                # and level to i
                result[v] = {
                    'parent': v,
                    'level': i
                }
                next.append(v)
        current = next;
        # increment the level
        i += 1
    return result


adj_list = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}

get_bfs(adj_list, 'a')
