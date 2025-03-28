

import Utils.storage as UT

class Local_Control:

    def __init__(self,central,local,trad):
        self.looks_to_central_governance = UT.Value(central)
        self.looks_to_local_governance = UT.Value(local)
        self.looks_to_traditional_governance = UT.Value(trad)

class Local_Population:

    def __init__(self,children,able,care):

        self.children = children
        self.able = able
        self.care = care

        self.population_growth_births = 0
        self.population_growth_immigration = 0

    @property
    def population(self):
        return self.children+self.able+self.care

class Local_Economy:

    def __init__(self,local_population,elite,discretionary,nonDiscretionary,extreme_need,living_cost,elite_spending = 20,discretionary_spending = 1.8):
        self.population = local_population

        self.living_cost = living_cost
        #spending power as multiple of living_cost
        self.elite_spending = elite_spending
        self.discretionary_spending = discretionary_spending

        self.set_spending_levels(elite,discretionary,nonDiscretionary,extreme_need)

    def set_spending_levels(self,elite,discretionary,nonDiscretionary,extreme_need):
        assert elite+discretionary+nonDiscretionary+extreme_need == self.population.population
        self.__elite = elite
        self.__discretionary = discretionary
        self.__nonDiscretionary = nonDiscretionary
        self.__extreme_need = extreme_need
