from graph import Graph
from node import Node
from edge import Edge
from community import Community
from equations import *

#first phase
def phaseOne(graph):

    nodes = graph.getNodes()
    m = graph.getTotalEdgeWeight()
    curr_mod = computeModularityGraph(graph)
    new_mod = curr_mod
    modularityIncrease = True

    while modularityIncrease:
        for nodeID, node in nodes.items():
            ncomms = node.getNeighborCommunities()
            bestModIncrease = float('-inf')
            currCommunity = node.getCommunity()
            bestCommunity = currCommunity
            for ncomm in ncomms:
                print("Moving {} into {}".format(nodeID, ncomm.getID()))
                currCommunity.removeMemberNode(node)
                ncomm.addMemberNode(node)
                currModIncrease = computeDeltaModularity(node, ncomm, m)
                ncomm.removeMemberNode(node)
                currCommunity.addMemberNode(node)
                print(currModIncrease)
                if (currModIncrease > bestModIncrease and currModIncrease > 0):
                    bestCommunity = ncomm
                    bestModIncrease = currModIncrease
            if(bestCommunity != currCommunity):
                print('Moving node {} to community {}'.format(node.getID(), bestCommunity.getID()))
                currCommunity.removeMemberNode(node)
                bestCommunity.addMemberNode(node)
        new_mod = computeModularityGraph(graph)
        if(new_mod > curr_mod):
            print("Modularity Increased by: {}".format(new_mod - curr_mod))
            curr_mod = new_mod
        else:
            modularityIncrease = False

    communities = graph.getCommunities()

    nonEmptyCommList = [comm for comm in communities if comm.getMemberNodes()]
    graph.setCommunities(nonEmptyCommList)


    return graph

#second phase
def phaseTwo(graph):
    """
    Consolidates communities toa  single supernode, and adds edges to that node based on sum of weights between nodes from those communities.
    Nodes will have self-edges with a weight equal to the number of edges between nodes in the community as described in the paper.
    :param graph: A graph object
    :return: A version of input graph corresponding to phase two of the blondel algorithm.
    """

    newNodes = {}
    newEdges = set()
    newCommunities = []
    # Create all supernodes, one per community
    for community in graph.getCommunities():
        id = community.getID()
        node = Node(id)
        id = community.getID()
        c = Community(id)
        c.addMemberNode(node)
        newNodes[id] = node
        newCommunities.append(c)

    # Create all edges between supernodes
    # Outer for loop will correspond to a supernode
    for community in graph.getCommunities():

        # This dictionary will store communityID as the key (these are same as supernode nodeID)
        # and a numerical value representing the weight between two supernodes
        newEdgeDict = {}
        # This for loop corresponds to the edges between each supernode
        for node in community.getMemberNodes():
            neighborList = node.getNeighborCommunities()
            # This loop calculates the weight of each new edge
            for edge in node.getConnections():
                otherNode = edge.getOtherNode(node)
                nCommID = otherNode.getCommunity().getID()
                if node == otherNode:
                    newEdgeDict[nCommID] = newEdgeDict.get(nCommID, 0) + edge.getWeight()
                elif nCommID == node.getCommunity().getID():
                    newEdgeDict[nCommID] = newEdgeDict.get(nCommID, 0) + edge.getWeight()/2
                else:
                    newEdgeDict[nCommID] = newEdgeDict.get(nCommID, 0) + edge.getWeight()
        for key, weight in newEdgeDict.items():
            n1 = newNodes[community.getID()]
            n2 = newNodes[key]
            e1 = Edge(n1, n2, weight)
            e2 = Edge(n2, n1, weight)
            if e1 not in newEdges and e2 not in newEdges:
                n1.addConnection(e1)
                n2.addConnection(e1)
                newEdges.add(e1)

    for nodeID, node in newNodes.items():
        node.computeSumEdgeWeights()

    for community in newCommunities:
        community.computeInCommunityWeight()

    p2graph = Graph(graph.getName(), nodes=newNodes, edges=newEdges, communities=newCommunities)

    return p2graph

