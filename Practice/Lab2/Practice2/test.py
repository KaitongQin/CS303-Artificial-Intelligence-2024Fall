import networkx as nx 
import matplotlib.pyplot as plt 
from queue import PriorityQueue
import heapq

# networkx version 2.3 (pip install networkx)
# matplotlib version 2.2.3
# !!! When dealing with nodes under the same distance/situation, pop them by alphabet order
# eg.When AStar Search faces with A and B with same distance, pop A first then pop B
# Modify any code you want to modify, try to make your hands dirty.
# Author Jimmy Gao


def vis(colors, position, G):
    fig, ax = plt.subplots()
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
    nx.draw(G, pos=position, with_labels=True, node_color=colors)  # get positions
    nx.draw_networkx_edge_labels(G, position, edge_labels=edge_labels)  # draw edge
    ax.xaxis.set_major_locator(plt.NullLocator())  # delete x axis
    ax.yaxis.set_major_locator(plt.NullLocator())  # delete y axis
    plt.show()


"""
Write your AStar Searh in python and get familar with python dictionary structure

Args:
- Graph: a node dict contains all edges and their weights. keys are nodes' names. values are tuple (End_node,weight).
------ eg: Graph["S"]:[('R', '80'), ('F', '99')]
------ means there is an edge from S to R with weight 80 and an edge from S to F with weight 99
- start: start node in graph
- end: end node in graph
- distances: straight line distance dict from each node to end node
------ eg: distances["S"]: 20.0
------ means the straight line distance from node S to end node is 20.0
Returns:
- do not need to return,but don't forget to yield the list queue
------ eg. queue:['S']
"""
def AStarSearch(Graph,start,end,distances):
    heap = []
    heapq.heappush(heap, (0, start))
    came_from = {}
    dist = {}
    came_from[start] = None
    dist[start] = 0
    yield heap

    while heap:
        current_priority, current = heapq.heappop(heap)
        yield heap
        
        if current == end:
            break

        for next, weight in sorted(Graph.get(current, [])):
            new_cost = dist[current] + weight
            if next not in dist or new_cost < dist[next]:
                dist[next] = new_cost
                priority = dist[next] + distances[next]
                heapq.heappush(heap, (priority, next))
                came_from[next] = current
        yield heap

# test block
test_case = 1
G = nx.DiGraph()  # for visualization
position = {}
result = []

# read file
distances={}
with open(f'./test_cases/{test_case}.txt', 'r') as f:
    line = f.readline()
    all_nodes = line.strip().split(" ")
    line = f.readline()
    dis=line.strip().split(" ")
    for i in range(len(all_nodes)):
        distances[all_nodes[i]]=float(dis[i])
    line=f.readline()
    for i in range(int(line)):
        line = f.readline()
        edge = line.strip().split(" ")
        G.add_edge(edge[0], edge[1], weight=float(edge[2]))
    pos = f.readline().strip().split(" ")
    for i in range(len(all_nodes)):
        position[all_nodes[i]] = (float(pos[i * 2]), float(pos[2 * i + 1]))
Graph = dict([(u, []) for u, v, d in G.edges(data=True)])
for u, v, d in G.edges(data=True):
    Graph[u].append((v, d["weight"]))
for node in G:
    if node not in Graph.keys():
        Graph[node]=[]
# Visualization
gray = (0.5, 0.5, 0.5)
brown = (0.5, 0.25, 0)
white = (1, 1, 1)
colors_list = [(_i, white) for _i in G.nodes]
colors_dict = dict(colors_list)
start=all_nodes[0]
end=all_nodes[-1]
res = AStarSearch(Graph,start,end,distances)
q = next(res)
temp_q=[]
last_q=q.copy()
last_node = None
while True:
    try:
        for node in G.nodes:
            if node in q and colors_dict[node] == white:
                colors_dict[node] = brown
            elif node not in q and colors_dict[node] == brown:
                colors_dict[node] = gray
                result.append(node)
        nodes, colors = zip(*colors_dict.items())
        vis(colors, position, G)
        if white not in colors:
            last_node = q[0]
        q = next(res)
        temp_q=last_q.copy()
        last_q=q.copy()
        if end in temp_q and end not in q:
            last_node=end
            break
    except StopIteration:
        break
for node in G.nodes:
    if node == last_node:
        colors_dict[node] = gray
result.append(last_node)
nodes, colors = zip(*colors_dict.items())
vis(colors, position, G)
print(result)