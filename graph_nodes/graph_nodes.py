import random
random.seed(10)


class Graph_Node:
    def __init__(self, indicator_values, name, year):
        self.indicators_values = indicator_values
        self.name = name
        self.year = year

    def __str__(self):
        return f"Graph_Node(indicator_values={self.indicators_values}, name={self.name}"
