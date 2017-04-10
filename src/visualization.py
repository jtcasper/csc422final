import networkx as nx
import matplotlib.pyplot as plt

def createVis(graph):
    G = nx.Graph()
    nodes = graph.getNodes()
    ids = [] # nodes
    es = [] # edges
    for n in nodes:
        ids.append(nodes[n].getID())
    G.add_nodes_from(ids)
    edges = graph.getEdges()
    print(type(edges))
    for e in edges:
        es.append(e.getNodeIds())
    G.add_edges_from(es)

    nx.draw(G)
    plt.show()
