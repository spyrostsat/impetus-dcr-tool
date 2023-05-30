from networkx import DiGraph
from ds_environment.ds_environment import DS_Environment


def print_graph_nodes_edges(demo_site: DS_Environment, graph: DiGraph):
    all_nodes = list(graph.nodes())
    for node in all_nodes:
        print(node.name)

    # for i in range(len(list(graph.nodes())) - 2):
    #     current_node = list(graph.nodes())[i + 2]
    #     print(current_node)
    #     if current_node.year == demo_site.stop_date:
    #         print()

    for u, v, attrs in graph.edges(data=True):
        cost = attrs['weight']
        print(f"Edge: {u} - {v}, Cost: {cost}")
