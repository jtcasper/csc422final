class Edge:
    """
    An arc between nodes. The origin node will keep a track of neighbor arcs, so bidirectional arcs will have
    an arc from node1 to node2 kept in node1, and a vice versa.
    """

    def __init__(self, node1, node2, weight=1):
        """
        :param neighbor: Node that is a neighbor
        :param weight: Weight of the arc
        """

        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getNodes(self):
        return (self.getNode1(), self.getNode2())

    def getWeight(self):
        return self.weight

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__ or (self.getNode2() == other.getNode1() and self.getNode1() == other.getNode2() and self.getWeight() == other.getWeight())
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)