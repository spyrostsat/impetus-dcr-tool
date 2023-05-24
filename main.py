import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import warnings
import itertools

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
        return Graph_Node(initial_indicator_values, "2020", 2020)
    else:
        indicator_values = compute_indicator_values(demo_site, previous_node, intervention_name)
        new_n = Graph_Node(indicator_values, f"{previous_node.year + demo_site.unit_time_step}_{intervention_name}",
                           previous_node.year + demo_site.unit_time_step)
        return new_n


def generate_pathways(interventions, n_steps):
    results = []
    for r in range(len(interventions)):  # for each length of interventions
        for perm in itertools.permutations(interventions[1:], r): # Exclude '0', generate permutations
            for indices in itertools.combinations(range(n_steps), len(perm)): # Indices to insert interventions
                result = [0] * n_steps # Initial pathway with all '0's
                for index, intervention in zip(indices, perm): # Insert interventions
                    result[index] = intervention
                results.append(result)
    return results

attica_ds = DS_Environment()
initial_indicator_values = [random.randrange(70, 90) for _ in range(attica_ds.number_indicators)]

graph = nx.DiGraph()

all_interventions = attica_ds.interventions
all_interventions_numbers = [i for i in range(len(all_interventions))]

pathways = generate_pathways(all_interventions_numbers, attica_ds.total_time_steps)

first_node_2020 = compute_new_node(attica_ds)
graph.add_node(first_node_2020)

for pathway in pathways:
    for i in range(len(pathway)):
        if i == 0:
            new_node = compute_new_node(attica_ds, list(graph.nodes())[0], str(pathway[i]))
            graph.add_node(new_node)
        else:
            last_node = list(graph.nodes())[-1]
            new_node = compute_new_node(attica_ds, last_node, str(pathway[i]))
            graph.add_edge(last_node, new_node)

print(list(graph.nodes())[0], "\n")

for i in range(len(list(graph.nodes())) - 1):
    current_node = list(graph.nodes())[i + 1]
    print(current_node)
    if current_node.year == attica_ds.stop_date:
        print("\n")


print(pathways)


# nx.draw(graph, with_labels=True)
#
# # Display the graph
# plt.show()
