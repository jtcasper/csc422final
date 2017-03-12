class Community:
    """
    A representation of a community, which is a collection of nodes
    """

    def __init__(self, communityID, memberNodes=None):
        """
        Constructor for a community
        :param communityID: ID of community
        :param memberNodes: List of nodes in this community
        """

        self.ID = communityID
        if memberNodes is None:
            self.memberNodes = []

    def getID(self):
        return self.ID

    def getMemberNodes(self):
        return self.memberNodes

    def addMemberNode(self, newNode):
        # newNode.setCommunity(self.getID())
        self.memberNodes.append(newNode)

    def getCommunitySize(self):
        """
        Returns the number of nodes in the community
        :return: Number of nodes in the community
        """
        return len(self.memberNodes)

    def computeInCommunityWeight(self):
        """
        Computes the weight of all arcs between nodes in the community.
        Since there are 2 arcs per connection, divide by 2 at end.
        :return: The weight between nodes in the community.
        """

        """TODO TEST THIS"""
        weightSum = 0
        for node in self.getMemberNodes():
            for arc in node.getConnections():
                if arc.getNeighbor().getCommunity == node.getCommunity():
                    weightSum += arc.getWeight()

        return weightSum/2

    def __str__(self):
        return str(self.getID())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.getID() == other.getID()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
