import networkx as nx
from graph_nodes.graph_nodes import Graph_Node
from utils.graph_traversal import compute_new_node, compute_indicator_values, compute_moving_cost
from ds_environment.ds_environment import DS_Environment


def fill_graph(demo_site: DS_Environment, graph: nx.DiGraph):
    depth = demo_site.total_time_steps

    all_interventions = demo_site.interventions
    all_interventions_numbers = [i for i in range(len(all_interventions))]

    root = Graph_Node(demo_site.initial_indicators_values, str(demo_site.start_date), demo_site.start_date, all_interventions_numbers)

    current_level = [root]

    for i in range(depth):
        next_level = []
        for parent in current_level:
            for intervention in parent.interventions:
                child_name = str(parent.year + demo_site.unit_time_step) + '-' + str(intervention)
                child, moving_cost = compute_new_node(demo_site, parent, str(intervention), child_name)
                if intervention != 0:  # only remove the intervention that has been made if it's not '0'
                    child.interventions.remove(intervention)
                graph.add_edge(parent, child, weight=moving_cost)
                next_level.append(child)
        current_level = next_level

    end_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1, [])
    for node in current_level:
        graph.add_edge(node, end_node, weight=0)

    return graph
