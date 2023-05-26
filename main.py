import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import warnings
from networkx.drawing.nx_pydot import graphviz_layout
from utils import generate_pathways, compute_new_node, compute_indicator_values, compute_moving_cost, print_graph_nodes_edges, perform_dijkstra

random.seed(10)

from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node

warnings.filterwarnings("ignore", category=DeprecationWarning)

attica_ds = DS_Environment()

graph = nx.DiGraph()

all_interventions = attica_ds.interventions
all_interventions_numbers = [i for i in range(len(all_interventions))]

pathways = generate_pathways(all_interventions_numbers, attica_ds.total_time_steps)

first_node_2020 = compute_new_node(attica_ds)
graph.add_node(first_node_2020)

final_node = Graph_Node([-1 for _ in range(attica_ds.number_indicators)], "End_Node", attica_ds.stop_date + 1)
graph.add_node(final_node)

for pathway in pathways:
    for i in range(len(pathway)):
        if i == 0:
            first_node_2020 = list(graph.nodes())[0]
            new_node, moving_cost = compute_new_node(attica_ds, first_node_2020, str(pathway[i]))
            graph.add_node(new_node)
            graph.add_edge(first_node_2020, new_node, weight=moving_cost)
        else:
            last_node = list(graph.nodes())[-1]
            new_node, moving_cost = compute_new_node(attica_ds, last_node, str(pathway[i]))
            graph.add_edge(last_node, new_node, weight=moving_cost)
            if i == len(pathway) - 1:
                graph.add_edge(new_node, final_node, weight=0)


print_graph_nodes_edges(attica_ds, graph)

perform_dijkstra(graph, first_node_2020, final_node)

T = nx.bfs_tree(graph, first_node_2020)

graph.add_node(first_node_2020)  # at year 2020))
# pos = nx.spring_layout(T)  # Positions of the nodes
pos = graphviz_layout(T, prog="dot")

nx.draw(T, pos, with_labels=True, font_size=6)

# # Plot Graph
# nx.draw(graph, with_labels=True)

# # Display the plot
plt.show()
