class Local:

    def __init__(self,infastructure):

        self.infastructure = infastructure


        self.birth_rate = 0
        self.immigration_rate = 0

        self.living_cost = 5
        #spending power as multiple of living_cost
        self.discretionary_spending = 1.2
        #spending power as multiple of discretionary_spending
        self.elite_spending = 5