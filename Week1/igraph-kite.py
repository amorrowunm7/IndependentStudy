import csv
from igraph import *

# Create empty graph
igraph_kite = Graph()
print("Importing graph ...")

# List of vertex names
vertices = [ ]       

# Read in vertices
f = open('Week1/kite_vertices.csv', 'rt')
f.readline()
try:
    reader = csv.reader(f)
    for row in reader:
        vertices.append(row[0])
finally:
    f.close()

# Add vertices to the graph
igraph_kite.add_vertices(len(vertices))
igraph_kite.vs["name"] = vertices


# Read in edges for kite network
edges = [ ]
f = open('Week1/kite_edges.csv', 'rt')
f.readline()
try:
    reader = csv.reader(f)
    for row in reader:
        edges.append((row[0], row[1]))
finally:
    f.close()

# Setup edges
igraph_kite.add_edges( edges )

print("Graph imported!")
print()
print("Edge Betweenness Centrality:")

ebs = g.edge_betweenness()
max_eb = max(ebs)
central_edges = [g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb] # [(7, 8)]
print("The edge between %s and %s is the most central edge" %
    (igraph_kite.vs[central_edges[0][0]]["name"],
    igraph_kite.vs[central_edges[0][1]]["name"]))

print("Print out the PageRanks for vertices")
igraph_kite.pagerank()

layout = igraph_kite.layout("kamada_kawai")
#plot(igraph_kite, layout = layout)
igraph_kite.vs["label"] = igraph_kite.vs["name"]
#color_dict = {"m": "blue", "f": "pink"}
#igraph_kite.vs["color"] = [color_dict[gender] for gender in igraph_kite.vs["gender"]]
plot(igraph_kite, layout = layout, bbox = (300, 300), margin = 20)