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
        newNode.setCommunity(self)
        self.memberNodes.append(newNode)

    def removeMemberNode(self, removeNode):
        self.memberNodes.remove(removeNode)


    def getCommunitySize(self):
        """
        Returns the number of nodes in the community
        :return: Number of nodes in the community
        """
        return len(self.memberNodes)

    def computeInCommunityWeight(self):
        """
        Computes the weight of all edges between nodes in the community.
        Since edges will be double counted per connection, divide by 2 at end.
        :return: The weight between nodes in the community.
        """

        """TODO TEST THIS"""
        weightSum = 0
        for node in self.getMemberNodes():
            for edge in node.getConnections():
                if edge.getOtherNode(node).getCommunity() == node.getCommunity():
                    weightSum += edge.getWeight()

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
