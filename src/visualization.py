import networkx as nx
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import*
from plotly.offline import plot
import math

def createVis(graph, name):
    G = nx.Graph()
    nodes = graph.getNodes()
    ids = [] # nodes
    es = [] # edges
    for n in nodes:
        ids.append(nodes[n].getID())
    G.add_nodes_from(ids)
    edges = graph.getEdges()
    for e in edges:
        es.append(e.getNodeIDs())
    G.add_edges_from(es)

    # create positions for nodoes
    communities = []
    communityIDs = []
    for c in graph.getCommunities(): # get unique communities
        if c.getID() not in communityIDs:
            communities.append(c)
            communityIDs.append(c.getID())
    numCommunities = len(communities)
    plotCenters = []
    r = 1 # radius of circle
    for i in range(numCommunities):
        x = r * math.cos(2 * math.pi * i / numCommunities)
        y = r * math.sin(2 * math.pi * i / numCommunities)
        plotCenters.append((x, y))

    # for c in graph.getCommunities():
    #     print('Community ID: ' + str(c.getID()))
    #     print('Member node IDs: ')
    #     for n in c.getMemberNodes():
    #         print(n.getID())
    #     print('---')

    for i in range(numCommunities):
        center = plotCenters[i]
        c = communities[i]
        r = 0.1 # radius of community
        nodes = c.getMemberNodes()
        numNodes = c.getCommunitySize()
        for j in range(numNodes):
            point = []
            if nodes[j].getID() == c.getID():
                point.append(center[0])
                point.append(center[1])
            else:
                x = center[0] + r * math.cos(2 * math.pi * j / numNodes-1)
                y = center[1] + r * math.sin(2 * math.pi * j / numNodes-1)
                point.append(x)
                point.append(y)
            G.node[nodes[j].getID()]['pos'] = point
            G.node[nodes[j].getID()]['com'] = c.getID()

    createPlotly(G, name)

def createPlotly(G, name):
    edge_trace = Scatter(
        x = [],
        y = [],
        line = Line(width=0.5, color='#888'),
        hoverinfo = 'none',
        mode = 'lines')

    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x = [],
        y = [],
        text = [],
        mode = 'markers',
        hoverinfo = 'text',
        marker = Marker(
            showscale = True,
            colorscale='YIGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Community Number',
                xanchor='left',
                titleside='right'
            ),
            line = dict(width=2)))

    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    # color nodes based on community id
    for node in G.nodes():
        node_trace['marker']['color'].append(G.node[node]['com'])
        node_info = 'Community ID: ' + str(G.node[node]['com']) + ' Node ID: ' + str(node) + ' Coords: ' + str(G.node[node]['pos'])
        #print(node_info)
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
             layout=Layout(
                title='Graph of Clusters',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    plot(fig, filename=name)
