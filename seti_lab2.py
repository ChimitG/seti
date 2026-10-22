import networkx as nx
G = nx.cycle_graph(30)
G.add_edge(0, 15)
G.add_edge(29, 15)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])
