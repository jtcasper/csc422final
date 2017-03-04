def computeModularity(network):
    """ Computes the modularity of a network
    :param network: a dict representation of a graph, weighted or unweighted
    :returns: the modularity of the graph as double
    """
    """
    TODO Figure out how to represent which community node is in (list probably).
    Currently assumes network is a dict with values being a list with 2 elements
    a dict of neighbor nodes and the weight of that edge, and its community
    """
    modularity = 0
    m = 0

    for node, neighbors in network.items():
        for neighbor, weight in neighbors.items():
            m += weight

    m /= 2

    #SUMi,j[Aij - kikj/2m]
    #i = node, j = neighbor

    sumResult = 0
    for node, neighbors in network.items():
        kNode = 0
        for neighbor, weight in neighbors.items():
            kNode += weight
            kNeighbor = 0
            for neighborNeighbor, nnWeight in network[neighbor]:
                kNeighbor += nnWeight

            sumResult += (weight - (kNode * kNeighbor) / (2*m)) *
                         (1 if node[1] == neighbor[1] else 0)



    modularity = sumResult/(2*m)

    return modularity
