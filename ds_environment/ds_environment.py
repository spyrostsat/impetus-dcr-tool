import random

random.seed(10) # to keep same numbers in all custom runs


class DS_Environment:
    def __init__(self, csv_name=None):
        if csv_name is None:
            self.climate_risks = ["water scarcity"]
            self.indicators = ["water availability per capita", "water use per capita", "water storage capacity",
                                "water quality", "groundwater levels", "water reuse rate"]
            self.sc_variables = ["population growth", "urbanization rates", "income", "ghg emissions", "temperature", "rainfall"]
            self.ds_name = "attica"
            self.unit_time_step = 5 # we split the total time duration in self.unit_time_step-year time steps
            self.number_climate_risks = 1
            self.number_indicators = 6
            self.number_sc_variables = 6
            self.start_date = 2020
            self.stop_date = 2050
            self.number_of_ssps = 5
            self.indicators_thresholds = [random.randrange(40, 60) for _ in range(self.number_indicators)]

            self.years = [year for year in range(self.start_date, self.stop_date+1, self.unit_time_step)]
            if 2050 not in self.years:
                self.years.append(self.stop_date)

            self.total_time_steps = len(self.years) - 1 # total number of self.unit_time_step-year time steps

            self.ssp_scenario = [random.randrange(1, self.number_of_ssps+1) for _ in range(self.total_time_steps)]
            
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
                    self.indicators_sc_variables_rel[i].append(random.uniform(0.95, 1))
            
            
            self.sc_variables_sing = [1, 1, -1, 1, 1, -1] # if the sc_variable gets higher or lower as SSPs get worse (i.e., from SSP1 to SSP5)
            # we have value '1' for increase and '-1' for decrease
            
            self.sc_variables_ssp_rel = []
            for i in range(self.number_sc_variables):
                self.sc_variables_ssp_rel.append([])
                for j in range(self.number_of_ssps):
                    if j == 0:
                        self.sc_variables_ssp_rel[i].append(random.uniform(1.01, 1.05))
                    else:
                        if self.sc_variables_sing[i] == 1:
                            self.sc_variables_ssp_rel[i].append(self.sc_variables_ssp_rel[i][j-1] + random.uniform(0, 0.05))
                        else:
                            self.sc_variables_ssp_rel[i].append(self.sc_variables_ssp_rel[i][j-1] - random.uniform(0, 0.05))

            self.sc_variables_timeseries_init = [random.uniform(0.6, 0.85) for _ in range(self.number_sc_variables)]
            self.sc_variables_timeseries = []
            
            for i in range(self.number_sc_variables):
                self.sc_variables_timeseries.append([])
                for j in range(self.total_time_steps + 1):
                    if j == 0:
                        self.sc_variables_timeseries[i].append(self.sc_variables_timeseries_init[i])
                    else:
                        self.sc_variables_timeseries[i].append(self.sc_variables_timeseries[i][j-1] * self.sc_variables_ssp_rel[i][self.ssp_scenario[j-1]-1])
            
            