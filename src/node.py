class Node:

    def __init__(self, ID, connections=None):
        """
        :param ID: This node's ID
        :param connections: A list of edges that connect this node to its neighbors
        :param community: The community that this node is a part of
        """

        self.ID = ID
        self.community = 0
        if connections is None:
            self.connections = []

    def getID(self):
         return self.ID

    def getConnections(self):
        return self.connections

    def addConnection(self, newConnection):
        """
        Adds an arc to the list of connections
        :param newConnection: Arc to be added
        """
        if newConnection not in self.connections:
           self.connections.append(newConnection)

    def getCommunity(self):
        return self.community

    def setCommunity(self, newCommunity):
        self.community = newCommunity

    def getDegree(self):
        """
        Computes the degree of the node
        :return: Degree of the node
        """
        return len(self.connections)

    def getNeighborCommunities(self):
        list = []

        for edge in self.getConnections():
            otherNode = edge.getOtherNode(self)
            list.append(otherNode.getCommunity())

        return list

    def getSumEdgeWeights(self):
        """
        Computes the weight of all edges this node is a part of
        :return: The weight of all edges this node is a part of
        """
        sum = 0

        for edge in self.connections:
            sum += edge.getWeight()

        return sum

    # def __str__(self):
    #     return str(self.getID())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getID() == other.getID()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.getID() < other.getID()
