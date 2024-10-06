import networkx as nx
import numpy as np
import random
import heapq
import argparse
from collections import deque

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
    reach_u1 = U1.copy()
    reach_u2 = U2.copy()
    q1 = deque(U1)
    q2 = deque(U2)
    in_q1 = set()
    in_q2 = set()
    
    while q1:
        current = q1.popleft()
        if current not in in_q1:
            in_q1.add(current)
            for neighbor in G.neighbors(current):
                if random.random() < G[current][neighbor]['weight1']:
                    q1.append(neighbor)
                reach_u1.add(neighbor)

    while q2:
        current = q2.popleft()
        if current not in in_q2:
            in_q2.add(current)
            for neighbor in G.neighbors(current):
                if random.random() < G[current][neighbor]['weight2']:
                    q2.append(neighbor)
                reach_u2.add(neighbor)

    return reach_u1, reach_u2

def compute_delta_fi(G, U1, U2, v, initial_fi):
    U1.add(v)
    reach_u1, reach_u2 = simulation(G, U1, U2)
    after = G.nodes() - (reach_u1 - reach_u2).union(reach_u2 - reach_u1)
    U1.remove(v)
    return len(after) - initial_fi

def select_v(G, U1, U2):
    remain = G.nodes - (U1.union(U2))
    remain_list = list(remain)
    remain_list.sort(key=lambda x: len(nx.bfs_tree(G, x).nodes()), reverse=True)
    return remain_list

# def select_v(G, U1, U2):
#     remain = G.nodes - (U1.union(U2))
#     remain_list = list(remain)
#     remain_list.sort(key=lambda x: sum(G[x][neighbor].get('weight1', 0) for neighbor in G.neighbors(x)), reverse=True)
#     return remain_list

def greedy_best_first(G, I1, I2, k):
    S1, S2 = set(), set()
    remain_list = select_v(G, I1, I2)
    while len(S1) + len(S2) < k:
        U1 = I1.union(S1)
        U2 = I2.union(S2)
        r1, r2 = simulation(G, U1.copy(), U2.copy())
        initial_length = len(G.nodes() - (r1 - r2).union(r2 - r1))
        max_v1 = -1
        max_delta_1 = 0
        for v in remain_list[:50]:
            compute_delta_1 = compute_delta_fi(G, U1, U2, v, initial_length)
            if compute_delta_1 > max_delta_1:
                max_v1 = v
                max_delta_1 = compute_delta_1

        max_v2 = -1
        max_delta_2 = 0
        for v in remain_list[:50]:
            compute_delta_2 = compute_delta_fi(G, U2, U1, v, initial_length)
            if compute_delta_2 > max_delta_2:
                max_v2 = v
                max_delta_2 = compute_delta_2

        if max_delta_1 > max_delta_2:
            if max_v1 != -1:
                S1.add(max_v1)
                remain_list.remove(max_v1)
        elif max_delta_1 < max_delta_2:
            if max_v2 != -1:
                S2.add(max_v2)
                remain_list.remove(max_v2)
    return S1, S2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--network', type=str, help="path to social network file")
    parser.add_argument('-i', '--initial', type=str, help="path to initial seed set")
    parser.add_argument('-b', '--balanced', type=str, help="path to balanced seed set")
    parser.add_argument('-k', '--budget', type=int, help="budget")
    args = parser.parse_args()

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

if __name__ == "__main__":
    main()