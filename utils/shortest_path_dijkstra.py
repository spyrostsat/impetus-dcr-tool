import networkx as nx
from graph_nodes.graph_nodes import Graph_Node


def perform_dijkstra(graph: nx.DiGraph, source: Graph_Node, target: Graph_Node):
    print("\n===========DIJKSTRA ALGORITHM FOR SHORTEST PATH FINDING:===========")
    shortest_path = nx.shortest_path(graph, source, target, weight='weight')
    shortest_path_length = nx.shortest_path_length(graph, source, target, weight='weight')

    print("Shortest Path:", shortest_path)
    print("Shortest Path Length:", shortest_path_length)
