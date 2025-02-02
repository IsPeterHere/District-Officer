from Structure import Place,Map

class District_center(Place):

    def __init__(self,tile):
        Place.__init__(self,tile,"District center")

class Urban_area(Place):

    def __init__(self,tile,name):
        Place.__init__(self,tile,"(Urban area) "+name)

class Rural_area(Place):

    def __init__(self,tile,name):
        Place.__init__(self,tile,"(Rural area) "+name)

class Natural_lake(Place):

    def __init__(self,tile,name):
        Place.__init__(self,tile,"Natural lake")


class District:

    def __init__(self,size=10):
        self.map = Map(size)
        self.name = "<District_name>"

        self.__generate(2,6)

    def __generate(self,urban_areas,rural_areas):
        self.district_center = District_center(self.map.get_free_tile())

        self.urban_areas = []
        for _ in range(urban_areas):
            self.urban_areas.append(Urban_area(self.map.get_free_tile(),"Old town"))

        self.rural_areas = []
        for _ in range(rural_areas):
            self.rural_areas.append(Rural_area(self.map.get_free_tile(),"Old Villages"))

