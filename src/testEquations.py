from equations import *
from graph import *
from algorithm import *
from visualization import *
from parsecsv import *

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

#from paper, network of 5-cliques connected to one another
network23 = {}

for i in range(1, 151):
    if(i%5) == 1:
        network23[i] = [{i+1:1, i+2:1, i+3:1, i+4:1, (i+7)%150:1}, i]
    elif(i%5) == 2:
        network23[i] = [{i-1:1, i+1:1, i+2:1, i+3:1}, i]
    elif(i%5) == 3:
        network23[i] = [{i-2:1, i-1:1, i+1:1, i+2:1}, i]
    elif(i%5) == 4:
        network23[i] = [{i-3:1, i-2:1, i-1:1, i+1:1}, i]
    elif(i%5) == 0:
        network23[i] = [{i-4:1, i-3:1, i-2:1, i-1:1}, i]

if  __name__ == '__main__':

    # graph23 = makeGraphFromDict('network23', network23)
    # p1graph23 = phaseOne(graph23)
    # createVis(p1graph23, 'network23')

    # zachDict = csvToDict('../data/ucidata-zachary/out.ucidata-zachary')
    # zachGraph = makeGraphFromDict('zachary', zachDict)
    # p1ZachGraph = phaseOne(zachGraph)
    # createVis(p1ZachGraph, 'zachary')

    marvelDict = csvToDict('../data/hero-network/hero-network.csv')
    marvelGraph = makeGraphFromDict('marvel', marvelDict)
    p1MarvelGraph = phaseOne(marvelGraph)
    createVis(p1MarvelGraph, 'marvel')

    # graph2 = makeGraphFromDict('network2', network2)
    # p1graph2 = phaseOne(graph2)
    # createVis(p1graph2, 'network2')

    # graph1 = makeGraphFromDict('network1', network1)
    # p1graph1 = phaseOne(graph1)
    # createVis(p1graph1, 'network1')

    # print(computeModularityDict(network1))
    # graph1 = makeGraphFromDict('network1', network1)
    # graph23 = makeGraphFromDict('network23', network23)
    # print('---------------------------------------')
    # print(computeModularityGraph(graph1))
    # #print(computeDeltaModularity(graph1.getNodes()[0], graph1.getCommunities()[0], graph1.getTotalEdgeWeight()))
    # print('---------------------------------------')
    # print(computeModularityGraph(graph23))
    # p1graph23 = phaseOne(graph23)
    # graph23 = makeGraphFromDict('network23', network23)
    # #graph23.getNodes().sort()
    # nodes = p1graph23.getNodes()
    # for comm in p1graph23.getCommunities():
    #     if(len(comm.getMemberNodes()) > 0 and len(comm.getMemberNodes()) != 5):
    #         print(comm.getID())
    # for i in range(0, 150):
    #     print("{} {} {}".format(i + 1, nodes[i] == nodesSorted[i], nodes[i].getCommunity() == nodesSorted[i].getCommunity()))
    #     if(len(nodes[i].getCommunity().getMemberNodes()) != 5):
    #         for node in nodes[i].getCommunity().getMemberNodes():
    #             print(node.getID())
        # print(" {} {}".format(nodes[i].getCommunity(), nodesSorted[i].getCommunity()))
        # for node1, node2 in zip(nodes[i].getCommunity().getMemberNodes(), nodesSorted[i].getCommunity().getMemberNodes()):
        #     print("     {} {}".format(node1.getID(), node2.getID()))
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
