
class Infastructure_object:

    def __init__(self,name):
        self.name = name

    def build(self,infastructre):
        pass

    def destroy(self,infastructre):
        del self

    def __str__(self):
        return "<INFASTRUCTURE OBJECT>" + self.name



class Infastructure:

    def __init__(self,tile):
        self.tile = tile
        
        
        self.create_staring_infastructure()

    def create_staring_infastructure(self):
