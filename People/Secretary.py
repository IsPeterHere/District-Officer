# -*- coding: utf-8 -*-

from People.Personage import Personage
from People.Templates.Template import Template 

class Writng:
    pass

class Responding:
    pass
    
class Secretary(Personage,Writng,Responding):

    def __init__(self,instance):
        
        Personage.__init__(self,instance)
        self.create_address("TEST NAME",
                            "Internal Communication",
                            "Your Secretary")


    def get_writing_template(self):
        return self.initial_communication()

    def get_response_template(self):
        return self.initial_response()

