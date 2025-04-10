import Utils.storage as UT


class Population_Unit:

    def __init__(self):
        self.Quality_of_life = 0

        self.children = 0
        self.able = 0
        self.care = 0

        self.looks_to_central_governance = UT.Value(0)
        self.looks_to_local_governance = UT.Value(0)
        self.looks_to_traditional_governance = UT.Value(0)
        self.culture_of_law = UT.Value(0)
        self.Access_to_gov = UT.Value(0)

        self.__last_spending_category = None
        self.__spending_category = None

    @property
    def size(self):
        return self.children+self.able+self.care

    def set_spending(self,spending):
        if spending in ["ND","D","E","N"]:
            self.__last_spending_category = self.__spending_category
            self.__spending_category = spending
        else:
            raise RuntimeError("Unrecognized spending category")