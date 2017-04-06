from node import Node
from edge import Edge
from community import Community

class Graph:
    """
    A collection of nodes and arcs between nodes that represent a graph
    """

    def __init__(self, name, nodes=None, edges=None, communities=None):
        """
        Constructs a graph, can be an empty graph
        :param name: Name of the graph
        :param nodes: List of nodes that make up a graph
        :param edges: List of edges that connect nodes
        :param communities: List of communities that are part of the graph
        """
        self.name = name
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes
        if edges is None:
            self.edges = set()
        else:
            self.edges = edges
        if communities is None:
            self.communities = []
        else:
            self.communities = communities

    def getName(self):
        return self.name

    def getNodes(self):
        return self.nodes

    def setNodes(self, nodes):
        self.nodes = nodes

    def addNode(self, newNode):
        self.nodes.append(newNode)

    def getEdges(self):
        return self.edges

    def setEdges(self, edges):
        self.edges = edges

    def getTotalEdgeWeight(self):
        """
        Sums the weights of all edges in the graph
        :return: m: the total edge weight
        """
        m = 0
        for edge in self.getEdges():
            m += edge.getWeight()
        return m

    def addEdge(self, newEdge):
        self.edges.append(newEdge)

    def getCommunities(self):
        return self.communities

    def addCommunity(self, newCommunity):
        self.communities.append(newCommunity)

    def setCommunities(self, communities):
        self.communities = communities

    def getSize(self):
        return

def makeGraphFromDict(name, dict):

    nodes = {}
    communities = []
    edges = set()

    i = 0
    for nodeID, nodeValues in dict.items():
        node = Node(i)
        c = Community(nodeValues[1])
        c.addMemberNode(node)
        nodes[nodeID] = node
        communities.append(c)
        i += 1
    for nodeID, nodeValues in dict.items():
        node = nodes[nodeID]
        for neighborID, arcWeight in nodeValues[0].items():
            node2 = nodes[neighborID]
            e = Edge(node, node2, arcWeight)
            e2 = Edge(node2, node, arcWeight)
            if e not in edges and e2 not in edges:
                edges.add(e)
                node.addConnection(e)
                node2.addConnection(e)

    graph = Graph(name, nodes=nodes, edges=edges, communities=communities)

    return graph
