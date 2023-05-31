import networkx as nx
from utils.graph_traversal import compute_new_node
from ds_environment.ds_environment import DS_Environment
from  graph_nodes.graph_nodes import Graph_Node


def fill_graph(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    end_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(end_node)

    # Initializations
    common_elements = False
    current_pathway = None
    current_nth_child = None
    new_pathway_to_pop = None
    current_pathways_index = None

    while True:
        if not common_elements:
            current_nth_child = 0
            current_pathway = pathways.pop(0) # if no common_elements exist from previous nodes that have been added to the graph, then we pop the first available pathway from the list and add the respective node to the graph
            current_pathways_index = 0 # this remembers where we are index-wise in the searching (inside the pathways list) for other common nodes

            for i in range(len(current_pathway)):
                if i == 0:
                    first_node_2020 = list(graph.nodes())[0]
                    new_node, moving_cost = compute_new_node(demo_site, first_node_2020, str(current_pathway[i]))
                    graph.add_node(new_node)
                    graph.add_edge(first_node_2020, new_node, weight=moving_cost)
                else:
                    last_node = list(graph.nodes())[-1]
                    new_node, moving_cost = compute_new_node(demo_site, last_node, str(current_pathway[i]))
                    graph.add_edge(last_node, new_node, weight=moving_cost)
                    if i == len(current_pathway) - 1:
                        graph.add_edge(new_node, end_node, weight=0)

            common_elements = True

        elif common_elements:
            father = list(graph.nodes())[-1 - current_nth_child]
            new_node, moving_cost = compute_new_node(demo_site, father, str(new_pathway_to_pop[-1]))
            graph.add_node(new_node)
            graph.add_edge(father, new_node, weight=moving_cost)
            graph.add_edge(new_node, end_node, weight=0)

        current_length_pathways = len(pathways)
        if current_length_pathways == 0: # when the pathways 2d list is out of elemenets, all pathways have been added as nodes to the graph, so we terminate the loop
            break

        new_pathway_to_pop = None

        for i in range(current_pathways_index, len(pathways)):
            if current_pathway[:-1] == pathways[i][:-1]: # this needs to be in a for loop and not -1 karfwta
                new_pathway_to_pop = pathways.pop(i)
                current_pathways_index = i
                current_nth_child += 1
                break

        if new_pathway_to_pop is None:
            common_elements = False

    return graph
