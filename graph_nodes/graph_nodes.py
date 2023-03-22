import random


class Graph_Nodes:
    def __init__(self, number_indicators, csv_name=None):
        self.number_indicators = number_indicators

        if csv_name is None:
            self.indicators_values = [random.randrange(70, 90) for _ in range(self.number_indicators)]  # at year 2020
