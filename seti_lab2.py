import networkx as nx
G = nx.cycle_graph(30)

G.add_edge(0, 15)
G.add_edge(21, 19)
G.add_edge(21, 23)
G.add_edge(18, 24)
G.add_edge(22, 20)

centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
  print("c(", n, ")=", centrality[n])
