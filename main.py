import random
import networkx as nx
import matplotlib.pyplot as plt
import warnings
from utils.shortest_path_dijkstra import perform_dijkstra
from utils.fill_graph import fill_graph
from utils.pathways_generator import generate_pathways
from utils.graph_nodes_edges_print import print_graph_nodes_edges
from utils.plot_graph import plot_graph
random.seed(10)

from ds_environment.ds_environment import DS_Environment

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    attica_ds = DS_Environment(csv_name="./data_inputs/data_template_2.csv")

    all_interventions = attica_ds.interventions
    # all_interventions_numbers = [i for i in range(len(all_interventions))]

    # pathways = generate_pathways(all_interventions_numbers, attica_ds.total_time_steps) # these are all the possible pathways

    graph = nx.DiGraph()
    graph = fill_graph(attica_ds, graph)

    # print_graph_nodes_edges(attica_ds, graph)

    shortest_path = perform_dijkstra(graph=graph, source=list(graph.nodes())[0], target=list(graph.nodes())[-1])

    plot_graph(graph) # plot the graph

if __name__ == "__main__":
    main()
