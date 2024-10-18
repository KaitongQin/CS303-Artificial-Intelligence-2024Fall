import networkx as nx
import numpy as np
import random
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


def simulation(G, I1, I2, S1, S2):
    n = G.number_of_nodes()
    U1 = I1.union(S1)
    U2 = I2.union(S2)
    r1, r2 = U1.copy(), U2.copy()
    q1, q2 = deque(U1), deque(U2)
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
    return n - len(r1 ^ r2)


def fitness(G, I1, I2, x, k):
    S1, S2 = set(), set()
    V = G.number_of_nodes()
    for i in range(V):
        if (x[i]):
            S1.add(i)
    for i in range(V, V * 2):
        if (x[i]):
            S2.add(i - V)
    
    if len(S1) + len(S2) <= k:
        return simulation(G, I1, I2, S1, S2)
    else:
        return -(len(S1) + len(S2))
    

def initialize_population(pop_size, num_genes):
    generations = []
    for _ in range(pop_size):
        generations.append(np.random.choice([0, 1], size=num_genes).tolist())
    return generations


def roulette_wheel_selection(population, fitness_value):
    min_fitness_value = min(fitness_value)
    if min_fitness_value < 0:
        shift_fitness = [(value - min_fitness_value) for value in fitness_value]
    else:
        shift_fitness = fitness_value
    total = sum(shift_fitness)
    pick = np.random.uniform(0, total)
    current = 0
    for i, individual in enumerate(population):
        current += fitness_value[i]
        if current >= pick:
            return individual
    return population[-1]


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(individual, mutation_rate=0.01):
    random_array = np.random.random(len(individual) + 5)
    for i in range(len(individual)):
        if random_array[i] < mutation_rate:
            individual[i] = 1 - individual[i]


def genetic_algorithm(G, I1, I2, pop_size, num_genes, k, generations, mutation_rate=0.01):
    population = initialize_population(pop_size, num_genes)
    for _ in range(generations):
        fitness_value = []
        for individual in population:
            fitness_value.append(fitness(G, I1, I2, individual, k))
        
        next_population = []
        while len(next_population) < pop_size:
            parent1 = roulette_wheel_selection(population, fitness_value)
            parent2 = roulette_wheel_selection(population, fitness_value)

            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_population.append([child1, child2])

        population = next_population[:pop_size]
        
    best = max(population, key=lambda x: fitness(G, I1, I2, x, k))
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--network', type=str, help="path to social network file")
    parser.add_argument('-i', '--initial', type=str, help="path to initial seed set")
    parser.add_argument('-b', '--balanced', type=str, help="path to balanced seed set")
    parser.add_argument('-k', '--budget', type=int, help="budget")
    args = parser.parse_args()
    s = time.time()
    G = nx.DiGraph()
    n = G.number_of_nodes()
    G = read_graph(G, args.network)
    I1, I2 = read_seeds(args.initial)
    budget = args.budget

    best = genetic_algorithm(G, I1, I2, pop_size=50, num_genes=2*n, k=budget, generations=100)
    S1, S2 = set(), set()
    for i in range(n):
        if best[i]:
            S1.add(i)
    for i in range(n, n*2):
        if best[i]:
            S2.add(i - n)

    with open(args.balanced, 'w') as f:
        f.write(f"{len(S1)} {len(S2)}\n")
        for element in S1:
            f.write(f"{element}\n")
        for element in S2:
            f.write(f"{element}\n")
    e = time.time()
    print(e - s)


if __name__ == "__main__":
    main()

