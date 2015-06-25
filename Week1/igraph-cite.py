import csv
from igraph import *

# Create empty graph
igraph_cite = Graph()
print("Importing citation network graph ...")

# Set of vertex names
vertices = { }

# Open file to citation network
f = open('Week1/cit-HepPh.txt', 'rt')

# Skip comments
f.readline()
f.readline()
f.readline()
f.readline()

# Loop thru file of edges
counter = 0
edges = []
try:
    for line in f.readlines():
        row = [int(x) for x in line.strip().split('\t')]
        print "bp %d" % counter
        # Keep running track of all nodes and add one by one
        if row[0] not in vertices:
            vertices[row[0]] = 1
            igraph_cite.add_vertices(row[0])
        if row[1] not in vertices:
            vertices[row[1]] = 1
            igraph_cite.add_vertices(row[1])

        # Attempt to add edge to graph
        edges.append((row[0], row[1]))
        counter = counter + 1

        if counter % 100 == 0:
            print "Adding another 100 edges (%d total)" % (counter * 100)
            try:
                igraph_cite.add_edges( edges )
                edges = []
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