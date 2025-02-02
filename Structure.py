import random 

class Place:

    def __init__(self,tile,name):
        self.tile = tile
        self.tile.claim(self)

        self.name = name

    def __str__(self):
        return "Location: "+self.name

    def __del__(self):
        self.tile.release()

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
