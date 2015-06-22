import csv
from igraph import *

# Create empty graph
igraph_cite = Graph()
print("Importing citation network graph ...")

# Set of vertex names
vertices = set()

# Open file to citation network
f = open('Week1/cit-HepPh.txt', 'rt')

# Skip comments
f.readline()
f.readline()
f.readline()
f.readline()

# Loop thru file of edges
try:
    for row in f.readlines():
        # Keep running track of all nodes and add one by one
        if row[0] not in vertices:
            vertices.add(row[0])
            igraph_cite.add_vertices(row[0])
        if row[1] not in vertices:
            vertices.add(row[1])
            igraph_cite.add_vertices(row[1])

        # Attempt to add edge to graph
        try:
            igraph_cite.add_edges( (row[0], row[1]) )
        except Exception as e:
            print e
finally:
    f.close()


print("Graph imported!")
print()
print("Edge Betweenness Centrality:")

ebs = g.edge_betweenness()
max_eb = max(ebs)
central_edges = [g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb] # [(7, 8)]
print("The edge between %s and %s is the most central edge" %
    (igraph_cite.vs[central_edges[0][0]]["name"],
    igraph_cite.vs[central_edges[0][1]]["name"]))

print("Print out the PageRanks for vertices")
igraph_cite.pagerank()

layout = igraph_cite.layout("kamada_kawai")
#plot(igraph_cite, layout = layout)
igraph_cite.vs["label"] = igraph_cite.vs["name"]
#color_dict = {"m": "blue", "f": "pink"}
#igraph_cite.vs["color"] = [color_dict[gender] for gender in igraph_cite.vs["gender"]]
plot(igraph_cite, layout = layout, bbox = (300, 300), margin = 20)