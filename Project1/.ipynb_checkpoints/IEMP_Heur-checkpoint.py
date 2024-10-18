import networkx as nx
import numpy as np
import argparse
from collections import deque
import time

def read_graph(G, file_path):
    with open(file_path, 'r') as f:
        n, m = map(int, f.readline().strip().split(" "))
        for i in range(m):
            s = f.readline().strip().split(" ")
            u = int(s[0])
            v = int(s[1])
            p1 = float(s[2])
            p2 = float(s[3])
            G.add_edge(u, v, weight1=p1, weight2=p2)
    return G


def read_seeds(file_path):
    I1, I2 = [], []
    with open(file_path, 'r') as f:
        i1, i2 = map(int, f.readline().strip().split(" "))
        for i in range(i1):
            I1.append(int(f.readline().strip()))
        for i in range(i2):
            I2.append(int(f.readline().strip()))
    I1 = set(I1)
    I2 = set(I2)
    return I1, I2


def simulation(G, U1, U2):
    r1 = U1.copy()
    r2 = U2.copy()
    q1 = deque(U1)
    q2 = deque(U2)
    a1, a2 = set(), set() 

    while q1:
        current = q1.popleft()
        a1.add(current)
        for neighbor in G.neighbors(current):
            if np.random.rand() < G[current][neighbor]['weight1'] and (neighbor not in a1):
                q1.append(neighbor)
            r1.add(neighbor)

    while q2:
        current = q2.popleft()
        a2.add(current)
        for neighbor in G.neighbors(current):
            if np.random.rand() < G[current][neighbor]['weight2'] and (neighbor not in a2):
                q2.append(neighbor)
            r2.add(neighbor)
    return r1, r2


def bfs(G, v, weight):
    q = deque()
    r = set()
    a = set()
    q.append(v)
    r.add(v)
    a.add(v)
    while q:
        current = q.popleft()
        for neighbor in G.neighbors(current):
            if np.random.rand() < G[current][neighbor][weight] and (neighbor not in a):
                q.append(neighbor)
                a.add(neighbor)
            r.add(neighbor)
    return r


def node_list(G):
    n = G.number_of_nodes()
    node_list = list(G.nodes)
    node_list.sort(key=lambda x: G.out_degree(x), reverse=True)
    if n > 10000:
        return node_list[:300], 10
    elif n > 5000:
        return node_list, 3
    else:
        return node_list[:100], 5


def greedy_best_first(G, I1, I2, budget):
    S1, S2 = set(), set()
    n = G.number_of_nodes()
    nodes, check_num = node_list(G)
    while len(S1) + len(S2) < budget:
        h1 = np.zeros(n)
        h2 = np.zeros(n)
        U1, U2 = I1.union(S1), I2.union(S2)

        for _ in range(check_num):
            r1, r2 = simulation(G, U1, U2)
            start = n - len(r1 ^ r2)

            for v in nodes:
                r1_v = bfs(G, v, 'weight1')
                r1_v = r1_v.union(r1)
                end = n - len(r1_v ^ r2)
                h1[v] += (end - start)

                r2_v = bfs(G, v, 'weight2')
                r2_v = r2_v.union(r2)
                end = n - len(r2_v ^ r1)
                h2[v] += (end - start)
        
        v1 = np.argmax(h1)
        v2 = np.argmax(h2)
        if h1[v1] > h2[v2]:
            S1.add(v1)
        else:
            S2.add(v2)
    return S1, S2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--network', type=str, help="path to social network file")
    parser.add_argument('-i', '--initial', type=str, help="path to initial seed set")
    parser.add_argument('-b', '--balanced', type=str, help="path to balanced seed set")
    parser.add_argument('-k', '--budget', type=int, help="budget")
    args = parser.parse_args()

    start = time.time()
    G = nx.DiGraph()
    G = read_graph(G, args.network)
    I1, I2 = read_seeds(args.initial)
    budget = args.budget
    S1, S2 = greedy_best_first(G, I1, I2, budget)

    with open(args.balanced, 'w') as f:
        f.write(f"{len(S1)} {len(S2)}\n")
        for element in S1:
            f.write(f"{element}\n")
        for element in S2:
            f.write(f"{element}\n")
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()

