import numpy as np


class Graph_Node:
    def __init__(self, indicator_values, name, year):
        self.indicators_values = indicator_values
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name} {np.round(np.array(self.indicators_values), 1)}"

    def __repr__(self):
        return f"{self.name} {np.round(np.array(self.indicators_values), 1)}"
