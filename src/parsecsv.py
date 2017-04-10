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
            fromNode = row[0]
            toNode = row[1]
            if fromNode not in nodes:
                nodes.append(fromNode)
                network[fromNode] = []
                innerDict = {}
                innerDict[toNode] = 1
                network[fromNode].append(innerDict)
                network[fromNode].append(fromNode)
            else:
                network[fromNode][0][toNode] = 1
        #pp = pprint.PrettyPrinter(indent=1)
        #pp.pprint(network)

if __name__ == '__main__':
    csvToDict('../data/ucidata-zachary/out.ucidata-zachary')
