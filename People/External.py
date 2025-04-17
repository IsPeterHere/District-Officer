from People.Templates.Template import Template 
from People.Personage import Personage

class General_secretariat(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")



        self.create_templates()

    def create_templates(self):
        self.initial_communication = Template()
        base = self.initial_communication.make_base()
        option = self.initial_communication.make_option_creator()

        main_root, something_else  = base([option("Hi Sir", formal = 1), 
                                           option("Greetings,")], 
                                          [option("Honey,")])

        main_root()
        something_else()

        main_root([option("I request more information on my assignment")])
        something_else([option("Theres a bee in the kitchen... OwO.")])

    def reply(self):
        pass 

    def get_template(self):
        return self.initial_communication

class You(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)

    def create_address(self,district_name):
        return Personage.create_address(self,
                                        district_name+" District Administration",
                                        "New Street Buildings Q.K.8",
                                        "You.")

    def proccess_inbox(self):
        #This is Overriding to disable inherited method.
        pass 

    def add_to_inbox(self,delivery_date,letter):
        self.__inbox.get(delivery_date,list()).append(letter)
