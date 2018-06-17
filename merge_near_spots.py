# coding : utf-8

import numpy as np
import matplotlib.pyplot as plt
import math

from union_find import UnionFind
from graph import Graph, Edge

NUM_NODE = 100

def divide_graph(graph, distance):
    """
    divide graph with connected components by links whose distance is less than the second argument.
    """
    group = [-1] * NUM_NODE
    current_group_id = 0
    division = []
    for i in range(NUM_NODE):
        current_group = set()
        if(group[i] != -1):
            continue
        # dfs
        stack = []
        stack.append(i)
        while(stack):
            now = stack.pop()
            group[now] = current_group_id
            current_group.add(now)
            for edge in graph.get_out_links(now):
                if(edge.distance <= distance and group[edge.target] == -1):
                    stack.append(edge.target)
        division.append(current_group)
        current_group_id += 1
    return division

def draw_graph(graph, distance):
    """
    draw input graph, without edges whose length is over distance.
    """
    plt.xlim([0,1])
    plt.ylim([0,1])
    for i in range(NUM_NODE):
        for edge in minimum_spanning_tree.get_out_links(i):
            source = edge.source
            target = edge.target
            if (source > target or edge.distance > distance):
                continue
            plt.plot([x[source], x[target]],
                [y[source], y[target]], marker = 'o')

def draw_merge_result(merge_result, x_coords, y_coords):
    """
    draw grouping result.
    circles' size is proportional to the size of the cluster.
    """
    xs = []
    ys = []
    ss = []
    for nodes in merge_result:
        sum_x = 0
        sum_y = 0
        for node in nodes:
            sum_x += x_coords[node]
            sum_y += y_coords[node]
        xs.append(sum_x/len(nodes))
        ys.append(sum_y/len(nodes))
        ss.append(len(nodes) * 12)
    plt.scatter(xs, ys, s=ss)

def construct_euclidean_minimim_spanning_tree(x_coords, y_coords):
    """
    construct minimum spanning tree(Kruskal's algorithm)
    ref: https://ja.wikipedia.org/wiki/%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB%E6%B3%95
    """
    edges = []
    for i in range(NUM_NODE):
        for j in range(i + 1, NUM_NODE):
            distance_ij = math.hypot(x_coords[i] - x_coords[j], y_coords[i] - y_coords[j])
            edges.append(Edge(i, j, distance_ij))
            edges.append(Edge(j, i, distance_ij))
    edges.sort(key=Edge.get_distance)

    uf = UnionFind(NUM_NODE)
    minimum_spanning_tree = Graph(NUM_NODE)
    for edge in edges:
        if (uf.belongsSameGroup(edge.source, edge.target)):
            continue
        uf.union(edge.source, edge.target)
        minimum_spanning_tree.addEdge(edge.source, edge.target, edge.distance)
        minimum_spanning_tree.addEdge(edge.target, edge.source, edge.distance)
    return minimum_spanning_tree

plt.subplots_adjust(wspace=0.4, hspace=0.6)
x = np.random.rand(NUM_NODE)
y = np.random.rand(NUM_NODE)
minimum_spanning_tree = construct_euclidean_minimim_spanning_tree(x, y)

plt.subplot(3, 2, 1)
plt.title("original node distribution")
plt.plot(x, y, 'o')


plt.subplot(3, 2, 2)
plt.title("minimum spanning tree")
draw_graph(minimum_spanning_tree, 1e+10)

plt.subplot(3, 2, 3)
plt.title("merge result with threshold 0.03")
draw_merge_result(divide_graph(minimum_spanning_tree, 0.03), x, y)

plt.subplot(3, 2, 4)
draw_graph(minimum_spanning_tree, 0.03)

plt.subplot(3, 2, 5)
plt.title("merge result with threshold 0.08")
draw_merge_result(divide_graph(minimum_spanning_tree, 0.08), x, y)

plt.subplot(3, 2, 6)
draw_graph(minimum_spanning_tree, 0.08)

plt.show()