import graphlab as gl

# Load Data
kite_vertices = gl.SFrame.read_csv('Week1/kite_vertices.csv')
kite_edges = gl.SFrame.read_csv('Week1/kite_edges.csv')

# Create graph
g_kite = gl.SGraph()
g_kite = g_kite.add_vertices(vertices=kite_vertices, vid_field='name')
g_kite = g_kite.add_edges(edges=kite_edges, src_field='src', dst_field='dst')
g_kite.get_edges().to_dataframe()

g_kite.get_vertices()

gl.canvas.set_target('browser')
g_kite.show(vlabel="id")

pr = gl.pagerank.create(g_kite)
pr.get('pagerank').topk(column_name='pagerank')