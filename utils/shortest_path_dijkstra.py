import networkx as nx
from graph_nodes.graph_nodes import Graph_Node


def perform_dijkstra(graph: nx.DiGraph, source: Graph_Node, target: Graph_Node):
    shortest_path = nx.shortest_path(graph, source, target, weight='weight')
    shortest_path_length = nx.shortest_path_length(graph, source, target, weight='weight')
    print("\nShortest path (Dijkstra):\t", end="")
    for i in range(len(shortest_path) - 1):
        print(shortest_path[i].name, end=" ---> ")
    print(shortest_path[-1].name)
    return shortest_path
