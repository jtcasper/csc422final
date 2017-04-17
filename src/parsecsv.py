import csv
import pprint

def csvToDict(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        if filename == '../data/ucidata-zachary/out.ucidata-zachary':
            next(reader)
        nodes = []
        network = {}
        count = 0
        for row in reader:
            # one set of edges (2 -> 3)
            if filename == '../data/ucidata-zachary/out.ucidata-zachary':
                row = row[0].split(' ')
                fromNode = int(row[0])
                toNode = int(row[1])
            else:
                # only run for count rows
                count += 1
                if count == 50000:
                    break
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
            # edges the other way (3 -> 2)
            if filename == '../data/ucidata-zachary/out.ucidata-zachary':
                fromNode = int(row[1])
                toNode = int(row[0])
            else:
                fromNode = row[1]
                toNode = row[0]
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
        #if filename != '../data/ucidata-zachary/out.ucidata-zachary':
        #    print(network['AVALANCHE/DOMINIC PE'])
        return network

#if __name__ == '__main__':
    #csvToDict('../data/ucidata-zachary/out.ucidata-zachary')
    #csvToDict('../data/hero-network/hero-network.csv')
