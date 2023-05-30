import networkx as nx

from utils.graph_traversal import compute_new_node
from utils.pathways_generator import generate_pathways
from utils.shortest_path_dijkstra import perform_dijkstra
from utils.graph_nodes_edges_print import print_graph_nodes_edges
from networkx import DiGraph
from ds_environment.ds_environment import DS_Environment
from  graph_nodes.graph_nodes import Graph_Node
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
import copy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def fill_graph(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    final_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(final_node)

    for pathway in pathways:
        for i in range(len(pathway)):
            if i == 0:
                first_node_2020 = list(graph.nodes())[0]
                new_node, moving_cost = compute_new_node(demo_site, first_node_2020, str(pathway[i]))
                graph.add_node(new_node)
                graph.add_edge(first_node_2020, new_node, weight=moving_cost)
            else:
                last_node = list(graph.nodes())[-1]
                new_node, moving_cost = compute_new_node(demo_site, last_node, str(pathway[i]))
                graph.add_edge(last_node, new_node, weight=moving_cost)
                if i == len(pathway) - 1:
                    graph.add_edge(new_node, final_node, weight=0)
    return graph

def fill_graph_new(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    end_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(end_node)

    pathways_copy = copy.deepcopy(pathways)

    common_elements = False
    current_pathway = None

    while True:
        if not common_elements:
            current_nth_child = 0
            current_pathway = pathways.pop(0)
            current_pathways_index = 0
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
        if current_length_pathways == 0:
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


# JUST FOR DEBUGGING
attica_ds = DS_Environment(csv_name="../data_inputs/data_template_2.csv")

all_interventions = attica_ds.interventions
all_interventions_numbers = [i for i in range(len(all_interventions))]
import networkx as nx

from utils.graph_traversal import compute_new_node
from utils.pathways_generator import generate_pathways
from utils.shortest_path_dijkstra import perform_dijkstra
from utils.graph_nodes_edges_print import print_graph_nodes_edges
from networkx import DiGraph
from ds_environment.ds_environment import DS_Environment
from  graph_nodes.graph_nodes import Graph_Node
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
import copy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def fill_graph(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    final_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(final_node)

    for pathway in pathways:
        for i in range(len(pathway)):
            if i == 0:
                first_node_2020 = list(graph.nodes())[0]
                new_node, moving_cost = compute_new_node(demo_site, first_node_2020, str(pathway[i]))
                graph.add_node(new_node)
                graph.add_edge(first_node_2020, new_node, weight=moving_cost)
            else:
                last_node = list(graph.nodes())[-1]
                new_node, moving_cost = compute_new_node(demo_site, last_node, str(pathway[i]))
                graph.add_edge(last_node, new_node, weight=moving_cost)
                if i == len(pathway) - 1:
                    graph.add_edge(new_node, final_node, weight=0)
    return graph

def fill_graph_new(pathways: list, demo_site: DS_Environment):
    graph = nx.DiGraph()

    first_node_2020 = compute_new_node(demo_site)
    graph.add_node(first_node_2020)

    end_node = Graph_Node([-1 for _ in range(demo_site.number_indicators)], "End_Node", demo_site.stop_date + 1)
    graph.add_node(end_node)

    pathways_copy = copy.deepcopy(pathways)

    common_elements = False
    current_pathway = None

    while True:
        if not common_elements:
            current_nth_child = 0
            current_pathway = pathways.pop(0)
            current_pathways_index = 0
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
        if current_length_pathways == 0:
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


# JUST FOR DEBUGGING
attica_ds = DS_Environment(csv_name="../data_inputs/data_template_2.csv")

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
