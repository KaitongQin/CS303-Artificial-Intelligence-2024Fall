import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('C', 'D', weight=1)
G.add_edge('B', 'D', weight=5)

path = nx.dijkstra_path(G, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(G, source='A', target='D', weight='weight')
print("从 A 到 D 的最短路径是:", path)
print("路径长度为:", path_length)