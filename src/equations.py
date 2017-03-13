def computeModularityDict(network):
    """ Computes the modularity of a network
    :param network: a dict representation of a network, weighted or unweighted
    :returns: the modularity of the network as double
    """
    m = 0

    for node, neighbors in network.items():
        for neighbor, weight in neighbors[0].items():
            m += weight

    m /= 2

    #SUMi,j[Aij - kikj/2m]
    #i = node, j = neighbor

    sumResult = 0
    for node, values in network.items():
        neighbors = values[0]
        kNode = sum(neighbors.values())
        for neighbor, weight in neighbors.items():
            neighborNodes = network[neighbor][0]
            kNeighbor = sum(neighborNodes.values())
            sumResult += (weight - (kNode * kNeighbor) / (2*m)) * (1 if values[1] == network[neighbor][1] else 0)

    modularity = sumResult/(2*m)

    return modularity

def computeModularityGraph(graph):
    """ Computes the modularity of a network
    :param graph: a graph representation of a network, weighted or unweighted
    :returns: the modularity of the network as double
    """
    m = graph.getTotalEdgeWeight()

    # Graph representations do not have repreated edges, so divide by 1
    # The traditional way of doing this node-wise rather than edgewise would double count each edge
    # m /= 1


    sumResult = 0
    for node in graph.getNodes():
        kNode = node.getSumEdgeWeights()
        for edge in node.getConnections():
            node2 = edge.getOtherNode(node)
            kNeighbor = node2.getSumEdgeWeights()
            interimResult = (edge.getWeight() - (kNode * kNeighbor) / (2*m))
            delta = 0
            if node.getCommunity() == node2.getCommunity():
                delta = 1
            interimResult *= delta
            sumResult += interimResult

    modularity = sumResult/(2*m)

    return modularity

def computeDeltaModularity(node, community, m):
    """ Attempts to move a node in to a given community, and calculates the change in modularity due to this move
    :param node: node i to be moved
    :param community: community for the node to be moved in to
    :param m: sum of all weights in the graph
    :return: double change in modularity value
    """

    sumIn = community.computeInCommunityWeight()
    sumTot = 0
    for commNode in community.getMemberNodes():
        sumTot += commNode.getSumEdgeWeights()
    kNode = node.getSumEdgeWeights()
    kNodeComm = 0
    for edge in node.getConnections():
        otherNode = edge.getOtherNode(node)
        if otherNode in community.getMemberNodes():
            kNodeComm += edge.getWeight()

    deltaModularity = ((sumIn + kNodeComm)/(2 * m) - ((sumTot + kNode)/(2 * m))**2) - (sumIn / (2 * m) - (sumTot / (2 * m))**2 - (kNode / (2 * m))**2 )
    return deltaModularity
