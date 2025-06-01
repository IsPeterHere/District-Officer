import random 
from District.Tile import Tile

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




class District:

    def __init__(self,size=10):
        self.map = Map(size)
        self.name = "<District_name>"

        self.__generate(2,6)

    def __generate(self,urban_areas,rural_areas):
        pass

    def next_day(self):
        pass