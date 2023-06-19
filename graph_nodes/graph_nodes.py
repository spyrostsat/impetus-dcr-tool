import numpy as np
from copy import deepcopy


class Graph_Node:
    def __init__(self, indicator_values , name, year, interventions):
        self.indicators_values = indicator_values
        self.name = name
        self.year = year
        self.interventions = deepcopy(interventions)  # deep copy to avoid shared reference among nodes

    def __str__(self):
        if self.name != "End_Node":
            return f"{self.name} | {np.round(np.average(np.array(self.indicators_values)), 2)}"
        else:
            return " "

    def __repr__(self):
        return f"{self.name} {np.round(np.array(self.indicators_values), 1)}"
