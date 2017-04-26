import sys
from graph import makeGraphFromDict
from parsecsv import *
from algorithm import *
from visualization import *

if len(sys.argv) > 2:
    print('Usage: py main.py <filepath> OR <1,2,3> (for a default dataset)')
    sys.exit(1)

network = {}
name = sys.argv[1]

if sys.argv[1] == '1':
    #network = csvToDict('../data/network23')
    network23 = {}

    for i in range(1, 151):
        if(i%5) == 1:
            network23[i] = [{i+1:1, i+2:1, i+3:1, i+4:1, (i+7)%150:1}, i]
        elif(i%5) == 2:
            network23[i] = [{i-1:1, i+1:1, i+2:1, i+3:1}, i]
        elif(i%5) == 3:
            network23[i] = [{i-2:1, i-1:1, i+1:1, i+2:1}, i]
        elif(i%5) == 4:
            network23[i] = [{i-3:1, i-2:1, i-1:1, i+1:1}, i]
        elif(i%5) == 0:
            network23[i] = [{i-4:1, i-3:1, i-2:1, i-1:1}, i]
    network = network23
    name = 'network23'
elif sys.argv[1] == '2':
    network = csvToDict('../data/ucidata-zachary/out.ucidata-zachary')
    name = 'zachary'
elif sys.argv[1] == '3':
    network = csvToDict('../data/hero-network/hero-network.csv')
    name = 'marvel'

networkGraph = makeGraphFromDict(sys.argv[0], network)

currentModularity = computeModularityGraph(networkGraph)
prevModularity = currentModularity

#print(currentModularity)
#print(prevModularity)
#print(networkGraph.getTotalEdgeWeight())
outpath = '../html/' + name + '0'
createVis(networkGraph, outpath)
modularities = [currentModularity]
i = 1
while True:
    networkGraph = phaseOne(networkGraph)
    currentModularity = computeModularityGraph(networkGraph)
    modularities.append(currentModularity)
    # print(currentModularity)
    # print(prevModularity)
    print(networkGraph.getTotalEdgeWeight())
    # print(i)
    if currentModularity <= prevModularity:
        break
    outpath = '../html/' + name + str(i)
    createVis(networkGraph, outpath)
    i += 1
    networkGraph = phaseTwo(networkGraph)
    outpath = '../html/' + name + str(i)
    createVis(networkGraph, outpath)
    i += 1
    prevModularity = currentModularity

print(modularities)
print(max(modularities))
print('done')
