import numpy as np
from copy import deepcopy


class Graph_Node:
    def __init__(self, indicator_values , name, year, interventions):
        self.indicators_values = indicator_values
        self.name = name
        self.year = year
        self.interventions = deepcopy(interventions)  # deep copy to avoid shared reference among nodes

    def __str__(self):
        return f"{self.name} {np.round(np.array(self.indicators_values), 1)}"

    def __repr__(self):
        return f"{self.name} {np.round(np.array(self.indicators_values), 1)}"
