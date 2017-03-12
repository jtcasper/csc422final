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
            self.nodes = []
        if edges is None:
            self.edges = []
        if communities is None:
            self.communities = []

    def getName(self):
        return self.name

    def getNodes(self):
        return self.nodes

    def addNode(self, newNode):
        self.nodes.append(newNode)

    def getEdges(self):
        return self.edges

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

    def getSize(self):
        return


def makeGraphFromDict(name, dict):
    """
    Updates this graph to be equal to a dictionary representation of a graph.
    Essentially a secondary constructor using a dict
    :param dict: Dictionary representation of a graph
    :return: Graph object that is equivalent to dict
    """

    graph = Graph(name)
    communities = []
    nodes = []

    for nodeID, nodeValues in dict.items():
        c = Community(nodeValues[1])
        n = Node(nodeID)
        if n not in nodes:
            nodes.append(n)
        for node in nodes:
            if node == n:
                n = node
        for neighborID, arcWeight in nodeValues[0].items():
            n2 = Node(neighborID)
            if n2 not in nodes:
                nodes.append(n2)
            for node in nodes:
                if node == n2:
                    n2 = node
            e = Edge(n, n2, arcWeight)
            if e not in graph.getEdges():
                graph.addEdge(e)
                n.addConnection(e)
                n2.addConnection(e)
        if c not in communities:
            communities.append(c)
        for comm in communities:
            if c == comm:
                c = comm
                c.addMemberNode(n)

    for node in nodes:
        graph.addNode(node)
    for c in communities:
        graph.addCommunity(c)

    return graph
