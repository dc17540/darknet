import kmapper
import networkx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
graphList = []
for i in range(1,17):
    graphList.append(i)
G.add_nodes_from(graphList)
edgeList = [(1,2),(2,3),(3,4),(4,1),(3,5),(3,9),(5,6),(6,7),(7,8),(8,5),(9,10),(10,11),(11,12),(12,9),(7,13),(11,13),(13,14),(14,15),(15,16),(16,13)]

edgeListFin =[]

for element in edgeList:
    element = list(element)
    element.append({'weight':1})
    element = tuple(element)
    edgeListFin.append(element)


G.add_edges_from(edgeListFin)
theMetric = dict(nx.all_pairs_dijkstra_path_length(G))

finList = []
finList2 = []
finList3 = []
for key in theMetric.keys():
    finList = []
    for key2 in theMetric[key].keys():
        finList.append(theMetric[key][key2])
    finList2.append(finList)

for element in finList:
    #np.average(np.asarray(element))
    finList3.append(np.average(np.asarray(element)))

print(finList3)
#for key in theMetric.keys():
#    print(theMetric[key])

nx.draw(G)
plt.draw()
plt.show()
for i in range(0,len(finList3)):
    finList3[i] = [finList[i],0]

import kmapper as km

# Some sample data


# Initialize
mapper = km.KeplerMapper(verbose=1)

from sklearn import datasets
#data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.3)
#print(data)
#print(type(data))


# Fit to and transform the data
#projected_data = mapper.fit_transform((np.array(finList3)).reshape(len(finList3),2), projection=[0,1]) # X-Y axis

data,lables = datasets.make_circles(n_samples=500, noise=0.03, factor=0.3)

projected_data = mapper.fit_transform(data,projection=[0,1])
#datasets.make_circles(n_samples=500, noise=0.03, factor=0.3)

# Create dictionary called 'graph' with nodes, edges and meta-information
#graph = mapper.map(projected_data, (np.array(finList3)).reshape(len(finList3),2), cover=km.Cover(n_cubes=10))

graph = mapper.map(projected_data,data, cover=km.Cover(n_cubes=10))

# Visualize it
mapper.visualize(graph, path_html="make_circles_keplermapper_output.html",
                 title="make_circles(n_samples=5000, noise=0.03, factor=0.3)")

