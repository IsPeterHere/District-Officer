import random 

class Map:

    def __init__(self,size):
        self.__size = size
        self.__grid = [[Tile((x,y),self) for y in range(size)] for x in range(size)]
        self.__free_tiles = [self.__grid[x][y] for x in range(size) for y in range(size)]
        random.shuffle(self.__free_tiles)

    def get_free_tile(self):
        return self.__free_tiles[0]

    def claim_tile(self,tile):
        self.__free_tiles.remove(tile)

    def release_tile(self,tile):
        self.__free_tiles.append(tile)
        random.shuffle(self.__free_tiles)

class Tile:

    def __init__(self,pos,parent_map):
        self.__pos = pos
        self.__map = parent_map
        self.__owner = None

    def claim(self,owner):
        assert self.__owner == None ,"Tile cannot be claimed if it already has an owner"

        self.__owner = owner
        self.__map.claim_tile(self)

    
    def release(self):
        self.__owner = None
        self.__map.release_tile(self)


class Local_Employment:

    def __init__(self,local_Economy,local_population):
        self.economy = local_Economy
        self.population = local_population


    
class Local_Construction:

    def __init__(self,local_Economy,local_Employment):
        pass

class Local_Industry_Supply:

    def __init__(self,local_Economy,local_Employment):
        pass

class Local_Industry_Production:

    def __init__(self,local_Economy,local_Employment):
        pass

class Local_Industry_Sale_and_Export:

    def __init__(self,local_Economy,local_Employment):
        pass

class Place:

    names = []
    with open("GermanTownNames.txt") as f:
        for line in f.readlines:
            names.append(line)

    def __init__(self,tile,name = None):
        self.tile = tile
        self.tile.claim(self)

        if name == None:
            self.name = self.names.pop(random.randint(0,len(self.names)))
        else:
            self.name = name



    def __str__(self):
        return "Place: "+self.name

    def __del__(self):
        self.tile.release()


class District_center(Place):

    def __init__(self,tile):
        Place.__init__(self,tile,"District center")

class Town(Place):

    def __init__(self,tile,type_name = "Town"):
        Place.__init__(self,tile)

class Village(Place):

    def __init__(self,tile,type_name = "Village"):
        Place.__init__(self,tile)

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
            self.urban_areas.append(Town(self.map.get_free_tile(),"Long-Established Town"))

        self.rural_areas = []
        for _ in range(rural_areas):
            self.rural_areas.append(Village(self.map.get_free_tile(),"Rural Village"))

