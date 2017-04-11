import csv
import pprint

def csvToDict(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        nodes = []
        network = {}
        for row in reader:
            row = row[0].split(' ')
            # one set of edges (2 -> 3)
            fromNode = int(row[0])
            toNode = int(row[1])
            if fromNode not in nodes:
                nodes.append(fromNode)
                network[fromNode] = []
                innerDict = {}
                innerDict[toNode] = 1
                network[fromNode].append(innerDict)
                network[fromNode].append(fromNode)
            else:
                network[fromNode][0][toNode] = 1
            # edges the other way (3 -> 2)
            fromNode = int(row[1])
            toNode = int(row[0])
            if fromNode not in nodes:
                nodes.append(fromNode)
                network[fromNode] = []
                innerDict = {}
                innerDict[toNode] = 1
                network[fromNode].append(innerDict)
                network[fromNode].append(fromNode)
            else:
                network[fromNode][0][toNode] = 1

        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(network)
        return network

#if __name__ == '__main__':
    #csvToDict('../data/ucidata-zachary/out.ucidata-zachary')
