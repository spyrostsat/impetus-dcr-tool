from ds_environment.ds_environment import DS_Environment
from graph_nodes.graph_nodes import Graph_Node

attica_ds = DS_Environment()
sample_node = Graph_Node(5)

print(attica_ds.ssp_scenario, '\n')

print(attica_ds.sc_variables_ssp_rel, '\n')

print(attica_ds.sc_variables_timeseries)
