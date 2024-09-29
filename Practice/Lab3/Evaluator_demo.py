# import networkx as nx
# import random

# # A function to simulate information exposure using Monte Carlo (simplified)
# def monte_carlo_simulation(G, I1, I2, S1, S2, iterations=1000):
#     exposure_count = 0
#     for _ in range(iterations):
#         exposed_nodes = set(S1).union(set(S2))
#         for seed in S1:
#             for neighbor in G.neighbors(seed):
#                 if random.random() < G[seed][neighbor]['prob']:
#                     exposed_nodes.add(neighbor)
#         for seed in S2:
#             for neighbor in G.neighbors(seed):
#                 if random.random() < G[seed][neighbor]['prob']:
#                     exposed_nodes.add(neighbor)
#         exposure_count += len(exposed_nodes)
    
#     return exposure_count / iterations

# # Greedy best-first search heuristic algorithm for IEM
# def greedy_best_first_search(G, I1, I2, k):
#     S1, S2 = set(), set()
    
#     while len(S1) + len(S2) < k:
#         # Find v1* and v2* which maximize the exposure when added to S1 and S2 respectively
#         best_v1, best_gain_v1 = None, -1
#         best_v2, best_gain_v2 = None, -1
        
#         for v in G.nodes():
#             if v not in S1 and v not in S2:
#                 # Calculate marginal gain for S1
#                 gain_v1 = monte_carlo_simulation(G, I1, I2, S1.union({v}), S2) - monte_carlo_simulation(G, I1, I2, S1, S2)
#                 if gain_v1 > best_gain_v1:
#                     best_v1, best_gain_v1 = v, gain_v1
                
#                 # Calculate marginal gain for S2
#                 gain_v2 = monte_carlo_simulation(G, I1, I2, S1, S2.union({v})) - monte_carlo_simulation(G, I1, I2, S1, S2)
#                 if gain_v2 > best_gain_v2:
#                     best_v2, best_gain_v2 = v, gain_v2
        
#         # Choose the node that provides the best gain between S1 and S2
#         if best_gain_v1 > best_gain_v2:
#             S1.add(best_v1)
#         else:
#             S2.add(best_v2)
    
#     return S1, S2

# # Example of how to use the algorithm
# if __name__ == "__main__":
#     # Creating a sample network graph
#     G = nx.Graph()
    
#     # Add edges with diffusion probabilities
#     edges = [(1, 2, 0.5), (2, 3, 0.5), (1, 3, 0.5)]
#     for u, v, p in edges:
#         G.add_edge(u, v, prob=p)
    
#     # Initial seed sets I1 and I2
#     I1 = {1}
#     I2 = {3}
    
#     # Budget
#     k = 2
    
#     # Run the greedy best-first search algorithm
#     S1, S2 = greedy_best_first_search(G, I1, I2, k)
    
#     print(f"Optimal Seed Set S1: {S1}")
#     print(f"Optimal Seed Set S2: {S2}")

import random
import numpy as np

for _ in range(10):
    print(np.random.rand() * 5)

a = set([1, 2, 3, 4])
b = set([2, 3, 4, 5])
print(a - b)
print((a-b).union(b-a))
print(a.symmetric_difference(b))