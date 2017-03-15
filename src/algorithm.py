import graph
from equations import *

#first phase
def phaseOne(graph):

    nodes = graph.getNodes()
    m = graph.getTotalEdgeWeight()
    curr_mod = computeModularityGraph(graph)
    new_mod = curr_mod
    modularityIncrease = True

    while modularityIncrease:
        for node in nodes:
            ncomms = node.getNeighborCommunities()
            bestModIncrease = float('-inf')
            currCommunity = node.getCommunity()
            bestCommunity = currCommunity
            for ncomm in ncomms:
                currModIncrease = computeDeltaModularity(node, ncomm, m)
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

    return graph
