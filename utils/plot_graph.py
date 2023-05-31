import matplotlib.pyplot as plt
import networkx as nx


# PRINT THE GRAPH SECTION
def plot_graph(graph):
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Generate the layout using the Graphviz layout engine
    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot', args='-Grankdir=LR')

    # Draw the nodes
    nx.draw_networkx_nodes(graph, pos, node_size=200, ax=ax)

    # Draw the edges
    nx.draw_networkx_edges(graph, pos, ax=ax)

    # # Draw node labels
    nx.draw_networkx_labels(graph, pos, font_size=10, ax=ax)

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Adjust plot limits to avoid cropping
    ax.margins(0.1)

    # Display the plot
    plt.tight_layout()
    plt.axis('off')

    # # Display the plot
    plt.show()
