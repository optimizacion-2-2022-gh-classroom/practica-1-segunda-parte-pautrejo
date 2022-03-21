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
    https://www.simplilearn.com/tutorials/data-structure-tutorial/bellman-ford-algorithm
    """

    n_nodes = len(graph.nodes())
    n = n_nodes + 1
    # Remove nan borders inside graph
    edges = []
    for edge in graph.edges().data():
        if ~np.isnan(edge[2]['weight']):
            edges.append(edge)

    # Add a start node and add zero weighted edges to all other nodes
    for i in range(n_nodes):
        edges.append((n_nodes, i, {'weight': 0}))

    # Initialize distances of nodes and predecessors
    distance= np.ones(n) * np.inf # Starting distances with infinite values
    distance[n_nodes] = 0  # Starting node has zero distance
    predecessors = np.ones(n) * -1  # Starting predecessors with -1 values

    for i in range(n):  
        x = -1
        for edge in edges:
            if distance[int(edge[0])] + edge[2]['weight'] < distance[int(edge[1])]:
                distance[int(edge[1])] = distance[int(edge[0])] + edge[2]['weight']
                predecessors[int(edge[1])] = int(edge[0])
                x = int(edge[1])
        if x == -1:  # If relaxation is not possible, there is no negative cycle
            return None
        
    # Identify negative cycle
    for i in range(n):
        x = predecessors[int(x)]
    cycle = []
    v = x
    while True:
        cycle.append(int(v))
        if v == x and len(cycle) > 1:
            break
        v = predecessors[int(v)]
    
    cycle.reverse() # reverse list
    return cycle