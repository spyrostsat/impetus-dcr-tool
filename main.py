from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node
import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np


def compute_indicator_values(demo_site: DS_Environment, previous_node: Graph_Node, intervention_name: str):
    previous_indicator_values = np.array(previous_node.indicators_values)
    previous_year = previous_node.year
    time_step = demo_site.unit_time_step
    sc_variables_timeseries = np.array(demo_site.sc_variables_timeseries)
    start_index = (previous_year - demo_site.start_date) // time_step
    sc_variables_timeseries = sc_variables_timeseries[:, start_index:start_index+2]
    indicators_interventions_rel = np.array(demo_site.indicators_interventions_rel)
    interventions_costs = np.array(demo_site.interventions_costs)


def compute_new_node(demo_site: DS_Environment, previous_node: Graph_Node = None, intervention_name: str = ""):
    if previous_node is None:
        new_node = Graph_Node([random.randrange(70, 90) for _ in range(demo_site.number_indicators)], "2020", 2020)
        # compute_indicator_values(demo_site, previous_node, intervention_name)
        return new_node
    else:
        indicator_values = compute_indicator_values(demo_site, previous_node, intervention_name)
        new_node = Graph_Node(indicator_values, f"{previous_node.year + demo_site.unit_time_step}_{intervention_name}", previous_node.year + demo_site.unit_time_step)
        return new_node


attica_ds = DS_Environment()

graph = nx.DiGraph()

first_node = compute_new_node(attica_ds)

graph.add_node(first_node)  # at year 2020))


# Plot Graph
nx.draw(graph, with_labels=True)
plt.show()
