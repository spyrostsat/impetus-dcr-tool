import random


class DS_Environment:
    def __init__(self, ds_name="attica", number_climate_risks=1, climate_risks=None, time_step=5, number_indicators=6,
                 indicators=None, number_sc_variables=6, sc_variables=None, indicators_thresholds=None, start_date=2020, csv_name=None):

        if climate_risks is None:
            self.climate_risks = ["water scarcity"]
        else:
            self.climate_risks = climate_risks
        if indicators is None:
            self.indicators = ["water availability per capita", "water use per capita", "water storage capacity",
                               "water quality", "groundwater levels", "water reuse rate"]
        else:
            self.indicators = indicators
        if sc_variables is None:
            self.sc_variables = ["population growth", "urbanization rates", "income", "ghg emissions", "temperature", "rainfall"]
        else:
            self.sc_variables = sc_variables

        self.ds_name = ds_name
        self.time_step = time_step
        self.climate_risks = climate_risks
        self.number_climate_risks = number_climate_risks
        self.indicators = indicators
        self.number_indicators = number_indicators
        self.number_sc_variables = number_sc_variables
        self.start_date = start_date
        self.stop_date = 2050

        if indicators_thresholds is None:
            self.indicators_thresholds = [random.randrange(40, 60) for _ in range(self.number_indicators)]

        self.years = [year for year in range(self.start_date, self.stop_date+1, self.time_step)]
        if 2050 not in self.years:
            self.years.append(self.stop_date)

        self.indicators_risks_rel = []

        if csv_name is None:
            for i in range(number_climate_risks):
                self.indicators_risks_rel.append([])
                for j in range(number_indicators):
                    self.indicators_risks_rel[i].append(1)
