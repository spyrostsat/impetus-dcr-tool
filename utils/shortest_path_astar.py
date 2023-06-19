import networkx as nx
from graph_nodes.graph_nodes import Graph_Node
from ds_environment.ds_environment import DS_Environment
import numpy as np


def make_heuristic_function(demo_site: DS_Environment):
    def heuristic_cost(source: Graph_Node, target: Graph_Node):
        cost = 0
        unit_cost = 1  # needs tuning
        indicators_thresholds = np.array(demo_site.indicators_thresholds)
        indicators_values = np.array(source.indicators_values)

        sum_positive = np.sum(indicators_values[indicators_values > indicators_thresholds] - indicators_thresholds[indicators_values > indicators_thresholds])
        sum_negative = np.abs(np.sum(indicators_values[indicators_values < indicators_thresholds] - indicators_thresholds[indicators_values < indicators_thresholds]))

        multiply_value = ((demo_site.stop_date - source.year) / demo_site.unit_time_step) * unit_cost

        if sum_positive > 0:
            cost += (1 / sum_positive) * multiply_value

        cost += sum_negative * multiply_value

        return cost


    return heuristic_cost


def perform_astar(graph: nx.DiGraph, source: Graph_Node, target: Graph_Node, demo_site: DS_Environment):
    heuristic = make_heuristic_function(demo_site)
    shortest_path = nx.astar_path(graph, source, target, heuristic=heuristic, weight='weight')
    shortest_path_length = nx.shortest_path_length(graph, source, target, weight='weight')
    print("\nShortest path (A*):\t\t\t", end="")
    for i in range(len(shortest_path) - 1):
        print(shortest_path[i].name, end=" ---> ")
    print(shortest_path[-1].name)
    return shortest_path
