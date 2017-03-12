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
        print(kNode)
        for neighbor, weight in neighbors.items():
            neighborNodes = network[neighbor][0]
            kNeighbor = sum(neighborNodes.values())
            # print(str(kNeighbor) + ' ' + str(neighbor))
            # print(weight)
            # print(kNode)
            # print(kNeighbor)
            print(m)
            # print((weight - (kNode * kNeighbor) / (2*m)) * (1 if values[1] == network[neighbor][1] else 0))
            sumResult += (weight - (kNode * kNeighbor) / (2*m)) * (1 if values[1] == network[neighbor][1] else 0)

    modularity = sumResult/(2*m)

    return modularity

def computeModularityGraph(graph):
    """ Computes the modularity of a network
    :param graph: a graph representation of a network, weighted or unweighted
    :returns: the modularity of the network as double
    """
    m = 0

    for edge in graph.getEdges():
        m += edge.getWeight()

    # Graph representations do not have repreated edges, so divide by 1
    m /= 1


    sumResult = 0
    for node in graph.getNodes():
        kNode = node.getSumEdgeWeights()
        print(kNode)
        for edge in node.getConnections():
            node2 = None
            for edgeNode in edge.getNodes():
                #gets the node that is NOT the current node
                if node != edgeNode:
                    node2 = edgeNode
            kNeighbor = node2.getSumEdgeWeights()
            # print(str(kNeighbor) + ' ' + str(node2.getID()))
            # print(edge.getWeight())
            # print(kNode)
            # print(kNeighbor)
            print(m)
            interimResult = (edge.getWeight() - (kNode * kNeighbor) / (2*m))
            delta = 0
            for c in graph.getCommunities():
                if node in c.getMemberNodes() and node2 in c.getMemberNodes():
                    delta = 1
            interimResult *= delta
            # print(interimResult)
            sumResult += interimResult

    modularity = sumResult/(2*m)

    return modularity
