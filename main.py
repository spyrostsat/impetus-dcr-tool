import random
import networkx as nx
import warnings
from utils.plot_graph import plot_graph
from utils.shortest_path_dijkstra import perform_dijkstra
from utils.shortest_path_astar import perform_astar
from utils.fill_graph import fill_graph
random.seed(10)
from time import time
from ds_environment.ds_environment import DS_Environment

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main():
    time_start = time()
    attica_ds = DS_Environment(csv_name="./data_inputs/data_template_3.csv")

    graph = nx.DiGraph()
    graph = fill_graph(attica_ds, graph)
    time_end = time()
    print(f"Graph Filling Duration = {time_end - time_start:.6f}")

    time_start = time()
    shortest_path = perform_astar(graph=graph, source=list(graph.nodes())[0], target=list(graph.nodes())[-1], demo_site=attica_ds)
    time_end = time()
    print(f"A* Duration = {time_end - time_start:.6f}")

    time_start = time()
    shortest_path = perform_dijkstra(graph=graph, source=list(graph.nodes())[0], target=list(graph.nodes())[-1])
    time_end = time()
    print(f"Dijkstra Duration = {time_end - time_start:.6f}")

    plot_graph(graph) # plot the graph

if __name__ == "__main__":
    main()
