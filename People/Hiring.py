# -*- coding: utf-8 -*-
from Resources.Name_Generator import Name_Generator
import random
from Post.Letter import Letter
from Post.Adressing import Address
from People.Templates.Template import Template 

class Person:
    instance = None
    
    def get_CV_template():
        
        template = Template("respond")
        base = template.make_base()
        text_option = template.make_text_option_creator()
        function_option = template .make_function_option_creator()
        
        base([text_option("TEST CV -- ")])
        def name(letter,person):
            return person["first_name"]+" "+person["surname"]
            
        base([function_option(name)])
        
        return template
        
    
    def __init__(self,gender = None):
        self.gender = random.choice(["M","F"]) if gender == None else gender
        self.first_name = Name_Generator.get_first_name(1920, self.gender)
        self.surname = Name_Generator.get_last_name().lower()
        self.surname = self.surname[0].upper() + self.surname[1:]
    
    def get_written_template_contents(self):
        #Allows for a person to be used as a template response letter parameter
        return {"gender":self.gender,"first_name":self.first_name,"surname":self.surname}
        
        
    def get_CV(self):
        letter = Letter(self.instance,Address(None,"CANDIDATE",self.first_name+" "+self.surname,signature=""),signoff=".Departmental Use Only.")
        template = Person.get_CV_template()
        template.write_response(letter,self)
        return letter