import networkx as nx
G = nx.cycle_graph(30)

G.add_edge(0, 14)
G.add_edge(0, 29)
G.add_edge(22, 19)
G.add_edge(22, 25)
G.add_edge(22, 18)
G.add_edge(15, 13)
G.add_edge(29, 28)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
  print("c(", n, ")=", centrality[n])
