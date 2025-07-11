import random 
import math


class Tile:

    names = []
    with open("Resources/GermanTownNames.txt",encoding='utf-8' ) as f:
        for line in f.readlines():
            names.append(line)

    def __init__(self,pos,parent_map):
        self.__pos = pos
        self.__map = parent_map

        self.name = self.names.pop(random.randint(0,len(self.names)-1))

        self.make_up = {"forest":{"percent_of_map":0,"utilized":0},
                        "hills":{"percent_of_map":0,"utilized":0},
                        "mountains":{"percent_of_map":0,"utilized":0},
                        "grasslands":{"percent_of_map":0,"utilized":0},
                        "marsh lands":{"percent_of_map":0,"utilized":0},
                        "fertile plains":{"percent_of_map":0,"utilized":0},
                        "fresh water":{"percent_of_map":0,"utilized":0},
                        "brown land":{"percent_of_map":0,"utilized":0},
                        "polluted water":{"percent_of_map":0,"utilized":0}}

        self.create_make_up()

    def create_make_up(self):
        r = random.random()

        dist = {}
        for i,key in enumerate(self.make_up.keys()):
            dist[key] = abs(random.randint(0,100)*math.cos(r*i))

        total = sum(dist.values())

        for key in self.make_up:
            self.make_up[key]["percent_of_map"] = (dist[key]/total)*100

    def __str__(self):
        return "<TILE> " + self.name
