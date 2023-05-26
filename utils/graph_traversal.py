from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node
import numpy as np
import random

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


def compute_moving_cost(demo_site: DS_Environment, previous_node: Graph_Node, intervention_name: str, new_node: Graph_Node):
    total_moving_cost = 0
    previous_indicator_values = np.array(previous_node.indicators_values)
    current_indicator_values = np.array(new_node.indicators_values)

    diff_indicator_values = previous_indicator_values - current_indicator_values

    unit_difference_cost = 1 # needs tuning

    total_moving_cost += np.sum(diff_indicator_values * unit_difference_cost)

    indicators_thresholds = np.array(demo_site.indicators_thresholds)

    total_moving_cost += np.sum(abs((current_indicator_values[current_indicator_values < indicators_thresholds] - indicators_thresholds[current_indicator_values < indicators_thresholds])) * unit_difference_cost * 3)

    interventions_costs = np.array(demo_site.interventions_costs)[int(intervention_name), :].astype(float)

    total_moving_cost += np.sum(interventions_costs)

    total_moving_cost = np.round(total_moving_cost, decimals=2)

    return total_moving_cost


def compute_new_node(demo_site: DS_Environment, previous_node: Graph_Node = None, intervention_name: str = ""):
    if previous_node is None:
        initial_indicator_values = [random.randrange(70, 90) for _ in range(demo_site.number_indicators)]
        return Graph_Node(initial_indicator_values, "2020", 2020)
    else:

        indicator_values = compute_indicator_values(demo_site, previous_node, intervention_name)
        new_node = Graph_Node(indicator_values, f"{previous_node.year + demo_site.unit_time_step}_{intervention_name}",
                           previous_node.year + demo_site.unit_time_step)

        moving_cost = compute_moving_cost(demo_site, previous_node, intervention_name, new_node)

        return new_node, moving_cost
