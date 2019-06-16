import kmapper
import networkx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def intersect(lst1, lst2):
    for  i in range(0,len(lst1)):
        lst1[i] = tuple(lst1[i])

    for i in range(0,len(lst2)):
        lst2[i] = tuple(lst2[i])
    
    lst1 = set(lst1)
    lst2 = set(lst2)
    
    lst3 = lst1 & lst2
    return lst3

def newGraph(aCover):
    nodeDict = {}
    finEdgeList = []
    counter = 1
    for element in aCover:
        if(len(element) > 2):
            nodeDict[counter] = element[2:]
            counter += 1
    for key in nodeDict.keys():
        for key2 in nodeDict.keys():
            if(nodeDict[key2] != nodeDict[key] and key != key2):
                if(len(intersect(nodeDict[key],nodeDict[key2])) != 0):
                    finEdgeList.append((key,key2))
    G=nx.Graph()
    G.add_nodes_from(nodeDict.keys())




    for element in finEdgeList:
        element = list(element)
        element.append({'weight':1})
        element = tuple(element)
        edgeListFin.append(element)


    G.add_edges_from(finEdgeList)
    return G




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



finList3 = np.asarray(finList3)

finList3 = (1/np.max(finList3))*finList3

#finList3 = finList3[:, np.array((0,1))]



nodeList = list(G.nodes)
#print(nodeList)
counter = 0
finDict = {}
for element in finList3:
   
    if(element not in finDict.keys()):
        finDict[element] = [nodeList[counter]]
    else:
        finDict[element].append(nodeList[counter])
    counter += 1


theCover = []
theN = 4
theE = .25
for i in range(0,theN):
    val1 =  (i)/(theN)
    val2 = (i+1)/(theN)
    theCover.append([val1,val2])
    

for i in range(0,len(theCover)):
    for j in range(0,len(theCover[i])):
        if(theCover[i][j] != 0 and theCover[i][j] != 1):
            if(j == 0):
                theCover[i][j] = theCover[i][j] - theE
            else:
                theCover[i][j] = theCover[i][j] + theE

#calcuate subgraphs in cover

for i in range(0,len(theCover)):
    for key in finDict.keys():
        if(key >= theCover[i][0] and key <= theCover[i][1]):
            theCover[i].append(finDict[key])

#print("Final Cover")
print(theCover)
newGraph = newGraph(theCover)
plt.figure(1)
nx.draw(newGraph)
plt.figure(2)
nx.draw_networkx(G)
plt.show()
