import networkx as nx

from utils import compute_new_node
from networkx import DiGraph
from ds_environment.ds_environment import DS_Environment
from  graph_nodes.graph_nodes import Graph_Node


def fill_graph(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    final_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(final_node)

    for pathway in pathways:
        for i in range(len(pathway)):
            if i == 0:
                first_node_2020 = list(graph.nodes())[0]
                new_node, moving_cost = compute_new_node(demo_site, first_node_2020, str(pathway[i]))
                graph.add_node(new_node)
                graph.add_edge(first_node_2020, new_node, weight=moving_cost)
            else:
                last_node = list(graph.nodes())[-1]
                new_node, moving_cost = compute_new_node(demo_site, last_node, str(pathway[i]))
                graph.add_edge(last_node, new_node, weight=moving_cost)
                if i == len(pathway) - 1:
                    graph.add_edge(new_node, final_node, weight=0)

    return graph
