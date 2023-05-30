import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import warnings
from networkx.drawing.nx_pydot import graphviz_layout
from utils import generate_pathways, compute_new_node, compute_indicator_values, compute_moving_cost, print_graph_nodes_edges, perform_dijkstra, fill_graph

random.seed(10)

from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    attica_ds = DS_Environment(csv_name="./data_inputs/data_template.csv")

    all_interventions = attica_ds.interventions
    all_interventions_numbers = [i for i in range(len(all_interventions))]

    pathways = generate_pathways(all_interventions_numbers, attica_ds.total_time_steps)

    graph = fill_graph(pathways, attica_ds)

    print_graph_nodes_edges(attica_ds, graph)

    shortest_path_dijkstra = perform_dijkstra(graph, list(graph.nodes())[0], list(graph.nodes())[1])

    # PRINT THE GRAPH SECTION

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Generate the layout using the Graphviz layout engine
    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot', args='-Grankdir=LR')

    # Draw the nodes
    nx.draw_networkx_nodes(graph, pos, node_size=200, ax=ax)

    # Draw the edges
    nx.draw_networkx_edges(graph, pos, ax=ax)

    # Draw node labels
    nx.draw_networkx_labels(graph, pos, font_size=10, ax=ax)

    # Adjust plot limits to avoid cropping
    ax.margins(0.1)

    # Display the plot
    plt.tight_layout()
    plt.axis('off')

    # # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
