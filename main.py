import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pydot
import warnings
from networkx.drawing.nx_pydot import graphviz_layout

random.seed(10)

from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node


warnings.filterwarnings("ignore", category=DeprecationWarning)

def compute_indicator_values(demo_site: DS_Environment, previous_node: Graph_Node, intervention_name: str):
    previous_indicator_values = np.array(previous_node.indicators_values)
    previous_year = previous_node.year
    time_step = demo_site.unit_time_step
    sc_variables_timeseries = np.array(demo_site.sc_variables_timeseries)
    start_index = (previous_year - demo_site.start_date) // time_step
    sc_variables_timeseries = sc_variables_timeseries[:, start_index:start_index + 2]
    sc_variables_timeseries = sc_variables_timeseries[:, 1] - sc_variables_timeseries[:, 0]
    sc_variables_timeseries *= 100

    indicators_interventions_rel = np.array(demo_site.indicators_interventions_rel)

    indicators_interventions_rel = indicators_interventions_rel[int(intervention_name), :].astype(float)

    indicators_sc_variables_rel = np.array(demo_site.indicators_sc_variables_rel)

    multipliers_indicators_sc_variables_rel = indicators_sc_variables_rel ** sc_variables_timeseries

    multipliers_indicators_sc_variables_rel = np.prod(multipliers_indicators_sc_variables_rel, axis=1)

    new_indicator_values = np.round(previous_indicator_values * multipliers_indicators_sc_variables_rel, decimals=3)

    new_indicator_values += indicators_interventions_rel

    return new_indicator_values


def compute_new_node(demo_site: DS_Environment, previous_node: Graph_Node = None, intervention_name: str = ""):
    if previous_node is None:
        return Graph_Node([random.randrange(70, 90) for _ in range(demo_site.number_indicators)], "2020", 2020)
    else:
        indicator_values = compute_indicator_values(demo_site, previous_node, intervention_name)
        new_n = Graph_Node(indicator_values, f"{previous_node.year + demo_site.unit_time_step}_{intervention_name}",
                           previous_node.year + demo_site.unit_time_step)
        return new_n


first_node = None
attica_ds = DS_Environment()

graph = nx.DiGraph()

for year in attica_ds.years:
    if year == 2020:
        first_node = compute_new_node(attica_ds)
        graph.add_node(first_node)  # at year 2020
    elif year == 2025:
        first_n = list(graph.nodes())[0]
        for j, intervention in enumerate(attica_ds.interventions):
            new_node = compute_new_node(attica_ds, first_n, str(j))
            graph.add_node(new_node)
            graph.add_edge(first_n, new_node)


T = nx.bfs_tree(graph, first_node)

# pos = nx.spring_layout(T)  # Positions of the nodes
pos = graphviz_layout(T, prog="dot")

nx.draw(T, pos, with_labels=True, font_size=6)

# Display the plot
plt.show()
