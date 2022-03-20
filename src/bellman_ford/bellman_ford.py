import numpy as np 

def bf_negative_cycle(graph):
    """
    Description
    -------
    Get the shortest path using the Bellman-Ford algorithm.

    Parameters
    -------
    G : Networkx DiGraph
        The input graph.

    Returns
    -------
    list
        A list with the shortest path.

    References
    -------
    https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
    https://nbviewer.org/github/rcroessmann/sharing_public/blob/master/arbitrage_identification.ipynb
    """

    n_nodes = len(graph.nodes())
    n = n_nodes + 1
    # Remove nan edges
    edges = [edge for edge in graph.edges().data() if ~np.isnan(edge[2]['weight'])]

    # Add a starting node and add edges with zero weight to all other nodes
    edges = edges + [(n_nodes, i, {'weight': 0}) for i in range(n_nodes)]

    # Initialize node distances and predecessors
    distance= np.ones(n) * np.inf
    distance[n_nodes] = 0  # Starting node has zero distance
    p = np.ones(n) * -1

    # Relax n times
    for i in range(n):  
        x = -1
        for edge in edges:
            if distance[int(edge[0])] + edge[2]['weight'] < distance[int(edge[1])]:
                distance[int(edge[1])] = distance[int(edge[0])] + edge[2]['weight']
                p[int(edge[1])] = int(edge[0])
                x = int(edge[1])
        if x == -1:  # If no relaxation possible, no negative cycle
            return None
        
    # Identify negative cycle
    for i in range(n):
        x = p[int(x)]
    cycle = []
    v = x
    while True:
        cycle.append(int(v))
        if v == x and len(cycle) > 1:
            break
        v = p[int(v)]
    return list(reversed(cycle))
