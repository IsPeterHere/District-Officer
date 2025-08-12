# -*- coding: utf-8 -*-
import random

class Name_Generator:
    
    def get_town_name():
        names = []
        with open("Resources/GermanTownNames.txt",encoding='utf-8' ) as f:
            for line in f.readlines():
                names.append(line)
               
        choice = random.choice(names)
        return choice
    
    def get_first_name(year,gender):
        assert(year>1879 and year < 2025), "Year Must be between 1879 and 2025 for name selection"
        assert(gender == "M" or gender == "F"), "gender required for name selction"
        
        names = []
        with open(f"Resources/firstNames/yob{year}.txt",encoding='utf-8' ) as f:
            for line in f.readlines():
                line = line.split(",")
                if line[1] == gender:
                    names.append(line[0])
                
        rnd = min(random.randint(0,len(names)),random.randint(0,len(names)),random.randint(0,len(names)))
        choice = names[rnd]
        return choice
        
    def get_last_name():
        names = []
        with open("Resources/last-names.txt",encoding='utf-8' ) as f:
            for line in f.read().split("\n"):
                names.append(line)
                
        rnd = min(random.randint(0,len(names)),random.randint(0,len(names)),random.randint(0,len(names)))
        choice = names[rnd]
        return choice