import random
import csv

random.seed(10)  # to keep same numbers in all custom runs


class DS_Environment:
    def __init__(self, csv_name=None):
        if csv_name is not None:
            try:
                all_data = []
                with open(csv_name, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        if row:
                            all_data.append(row)

                    print(all_data)

                    # GENERAL DEMO SITE PARAMETERS
                    self.ds_name = all_data[0][0]

                    self.climate_risks = all_data[1]

                    self.indicators = all_data[2]

                    self.sc_variables = all_data[3]

                    self.interventions = all_data[4]

                    self.interventions_costs_names = all_data[5]

                    self.unit_time_step = int(all_data[6][0])  # we split the total time duration in self.unit_time_step-year (e.g., 5-year) time steps

                    self.number_climate_risks = len(self.climate_risks)

                    self.number_indicators = len(self.indicators)

                    self.number_sc_variables = len(self.sc_variables)

                    self.number_interventions = len(self.interventions)

                    self.number_interventions_costs = len(self.interventions_costs_names)

                    self.start_date = int(all_data[7][0])

                    self.stop_date = int(all_data[8][0])

                    self.indicators_thresholds = all_data[9]
                    self.indicators_thresholds = [int(d) for d in self.indicators_thresholds]


                    self.years = [year for year in range(self.start_date, self.stop_date + 1, self.unit_time_step)]
                    if self.stop_date not in self.years:
                        self.years.append(self.stop_date)

                    self.total_time_steps = len(self.years) - 1  # total number of self.unit_time_step-year time steps

                    # INDICATORS - SOCIOECONOMIC VARIABLES SECTION

                    row_to_read = 10

                    # if user gives no input, all indicators are associated with all climate risks, which means that we append '1' as "True"
                    self.indicators_risks_rel = []
                    for i in range(self.number_climate_risks):
                        self.indicators_risks_rel.append(all_data[row_to_read])
                        self.indicators_risks_rel[i] = [int(d) for d in self.indicators_risks_rel[i]]
                        row_to_read += 1

                    self.indicators_sc_variables_rel = []
                    for i in range(self.number_indicators):
                        self.indicators_sc_variables_rel.append(all_data[row_to_read])
                        self.indicators_sc_variables_rel[i] = [float(d) for d in self.indicators_sc_variables_rel[i]]
                        row_to_read += 1

                    # SOCIO ECONOMIC VARIABLES TIMESERIES SECTION

                    self.sc_variables_sign = all_data[row_to_read]
                    self.sc_variables_sign = [int(d) for d in self.sc_variables_sign]
                    row_to_read += 1

                    self.sc_variables_timeseries = []

                    for i in range(self.number_sc_variables):
                        self.sc_variables_timeseries.append(all_data[row_to_read])
                        self.sc_variables_timeseries[i] = [float(d) for d in self.sc_variables_timeseries[i]]
                        row_to_read += 1

                    # INTERVENTIONS SECTION

                    self.indicators_interventions_rel = []
                    for i in range(self.number_interventions):
                        self.indicators_interventions_rel.append(all_data[row_to_read])
                        self.indicators_interventions_rel[i] = [int(d) for d in self.indicators_interventions_rel[i]]
                        row_to_read += 1

                    # all intervention costs get values closer to 10 as they get worse. E.g., the biggest Cost is 10 but the biggest feasibility is 1

                    self.interventions_costs = []
                    for i in range(self.number_interventions):
                        self.interventions_costs.append(all_data[row_to_read])
                        self.interventions_costs[i] = [int(d) for d in self.interventions_costs[i]]
                        row_to_read += 1

                    print(self.interventions_costs)
            except FileNotFoundError:
                print("Wrong file path...")

        else: # fixed data instantiation if not csv file is given

            # GENERAL DEMO SITE PARAMETERS
            self.climate_risks = ["water scarcity"]
            self.indicators = ["water availability per capita", "water use per capita", "water storage capacity",
                               "water quality", "groundwater levels", "water reuse rate"]
            self.sc_variables = ["population growth", "urbanization rates", "income", "ghg emissions", "temperature",
                                 "rainfall"]
            self.ds_name = "attica"
            self.unit_time_step = 5  # we split the total time duration in self.unit_time_step-year (e.g., 5-year) time steps
            self.number_climate_risks = len(self.climate_risks)
            self.number_indicators = len(self.indicators)
            self.number_sc_variables = len(self.sc_variables)
            self.start_date = 2020
            self.stop_date = 2040

            self.indicators_thresholds = [random.randrange(40, 60) for _ in range(self.number_indicators)]

            self.years = [year for year in range(self.start_date, self.stop_date + 1, self.unit_time_step)]
            if self.stop_date not in self.years:
                self.years.append(self.stop_date)

            self.total_time_steps = len(self.years) - 1  # total number of self.unit_time_step-year time steps

            # INDICATORS - SOCIO ECONOMIC VARIABLES SECTION

            # if user gives no input, all indicators are associated with all climate risks, which means that we append '1' as "True"
            self.indicators_risks_rel = []
            for i in range(self.number_climate_risks):
                self.indicators_risks_rel.append([])
                for j in range(self.number_indicators):
                    self.indicators_risks_rel[i].append(1)

            self.indicators_sc_variables_rel = []
            for i in range(self.number_indicators):
                self.indicators_sc_variables_rel.append([])
                for j in range(self.number_sc_variables):
                    self.indicators_sc_variables_rel[i].append(random.uniform(0.95, 1))  # this might be able  to take values greater than 1, if one sc variable gets improved (e.g., population gets reduced)


            # SOCIO ECONOMIC VARIABLES TIMESERIES SECTION

            self.sc_variables_sign = [1, 1, -1, 1, 1, -1]

            self.sc_variables_timeseries = []

            for i in range(self.number_sc_variables):
                self.sc_variables_timeseries.append([])
                for j in range(len(self.years)):
                    if j == 0:
                        self.sc_variables_timeseries[i].append(random.uniform(0.6, 0.7))
                    else:
                        self.sc_variables_timeseries[i].append(self.sc_variables_timeseries[i][j-1] + self.sc_variables_sign[i] * random.uniform(0.02, 0.07))

            # INTERVENTIONS SECTION

            self.interventions = ["Do Nothing", "Sewer Mining", "Rainwater Harvesting", "Subsol", "Forests EWSs", "Groundwater Usage"]
            # self.interventions = ["Do Nothing", "Sewer Mining"]
            self.number_interventions = len(self.interventions)

            self.indicators_interventions_rel = []
            for i in range(self.number_interventions):
                self.indicators_interventions_rel.append([])
                for j in range(self.number_indicators):
                    if i == 0:
                        self.indicators_interventions_rel[i].append(0)
                    else:
                        self.indicators_interventions_rel[i].append(random.randrange(1, 11))

            # all intervention costs get values closer to 10 as they get worse. E.g., the biggest Cost is 10 but the biggest feasibility is 1
            self.interventions_costs_names = ["Cost", "Technology readiness level", "Societal readiness level", "Time to implementation [years]",
                                              "Hidden risks - disadvantages of intervention", "Feasibility"]

            self.number_interventions_costs = len(self.interventions_costs_names)

            self.interventions_costs = []
            for i in range(self.number_interventions):
                self.interventions_costs.append([])
                for j in range(self.number_interventions_costs):
                    if i == 0:
                        self.interventions_costs[i].append(0)
                    else:
                        self.interventions_costs[i].append(random.randrange(1, 11))
