import networkx as nx
import numpy as np
import argparse
from collections import deque

def read_graph(G, file_path):
    P1, P2 = [], []
    with open(file_path, 'r') as f:
        n, m = map(int, f.readline().strip().split(" "))
        for i in range(m):
            s = f.readline().strip().split(" ")
            u = int(s[0])
            v = int(s[1])
            p1 = float(s[2])
            p2 = float(s[3])
            P1.append(p1)
            P2.append(p2)
            G.add_edge(u, v, weight1=p1, weight2=p2)
    return G, P1, P2

def read_seeds(file_path):
    I1 = []
    I2 = []
    with open(file_path, 'r') as f:
        i1, i2 = map(int, f.readline().strip().split(" "))
        for i in range(i1):
            I1.append(int(f.readline().strip()))
        for i in range(i2):
            I2.append(int(f.readline().strip()))
    I1 = set(I1)
    I2 = set(I2)
    return I1, I2

def simulation(G, U1, U2, P1, P2):
    active_u1 = U1.copy()
    active_u2 = U2.copy()
    q1 = deque(U1)
    q2 = deque(U2)
    
    while q1:
        current = q1.popleft()
        for neighbor in G.neighbors(current):
            if neighbor not in active_u1:
                if np.random.rand() < G[current][neighbor]['weight1']:
                    q1.append(neighbor)
                active_u1.add(neighbor)

    while q2:
        current = q2.popleft()
        for neighbor in G.neighbors(current):
            if neighbor not in active_u2:
                if np.random.rand() < G[current][neighbor]['weight2']:
                    q2.append(neighbor)
                active_u2.add(neighbor)

    return active_u1, active_u2

def monte_carlo_simulation(G, U1, U2, P1, P2, Iteration):
    total_E = 0
    nodes = set(G.nodes())
    n = G.number_of_nodes()
    for _ in range(Iteration):
        u1, u2 = simulation(G, U1, U2, P1, P2)
        symmetric_difference_size = len(u1.symmetric_difference(u2))
        total_E += n - symmetric_difference_size

    return total_E / Iteration


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--network', type=str, help="path to social network file")
    parser.add_argument('-i', '--initial', type=str, help="path to initial seed set")
    parser.add_argument('-b', '--balanced', type=str, help="path to balanced seed set")
    parser.add_argument('-k', '--budget', type=int, help="budget")
    parser.add_argument('-o', '--output', type=str, help="path to output value")
    args = parser.parse_args()

    G = nx.DiGraph()
    G, P1, P2 = read_graph(G, args.network)
    I1, I2 = read_seeds(args.initial)
    S1, S2 = read_seeds(args.balanced)
    U1 = I1.union(S1)
    U2 = I2.union(S2)
    iterations = 1000
    ans = monte_carlo_simulation(G, U1, U2, P1, P2, iterations)
    print(ans)
    # with open(args.output, 'w') as f:
    #     f.write(f"{ans:.2f}\n")

if __name__ == "__main__":
    main()

