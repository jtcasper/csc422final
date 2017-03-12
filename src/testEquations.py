from equations import *
from graph import *

network1 = {1:[{2:1, 3:1, 4:1}, 1],
           2:[{1:1, 5:1}, 1],
           3:[{1:1, 4:1, 5:1}, 2],
           4:[{1:1, 3:1, 5:1}, 2],
           5:[{2:1, 3:1, 4:1}, 2],
}

network2 = {1:[{2:1, 3:1, 4:1}, 1],
           2:[{1:1, 5:1}, 2],
           3:[{1:1, 4:1, 5:1}, 3],
           4:[{1:1, 3:1, 5:1}, 4],
           5:[{2:1, 3:1, 4:1}, 5],
}

if  __name__ == '__main__':
    print(computeModularityDict(network1))
    graph1 = makeGraphFromDict('network1', network1)
    print('---------------------------------------')
    print(computeModularityGraph(graph1))
    computeDeltaModularity(graph1.getNodes()[0], graph1.getCommunities()[0], graph1.getTotalEdgeWeight())
    # print(graph1.getName())
    # for node in graph1.getNodes():
    #     print("node:{} address:{}".format(node.getID(), node))
    # for edge in graph1.getEdges():
    #     print("node1:{}, address:{}, node2:{}, address:{}".format(edge.getNode1().getID(), edge.getNode1(), edge.getNode2().getID(), edge.getNode2()))
    # for community in graph1.getCommunities():
    #     print("community:{}".format(community.getID()))
    #     for node in community.getMemberNodes():
    #         print("node:{}, community:{}".format(node.getID(), node.getCommunity()))
    #         for edge in node.getConnections():
    #             print("node1:{}, node2:{}".format(edge.getNode1(), edge.getNode2()))