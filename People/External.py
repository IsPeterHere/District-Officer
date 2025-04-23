from People.Templates.Template import Template 
from People.Personage import Personage

class General_secretariat(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")



        self.create_writing_templates()
        self.create_response_template()

    def create_writing_templates(self):
        self.initial_communication_template = Template("write")
        base = self.initial_communication_template.make_base()
        option = self.initial_communication_template.make_option_creator()

        main_root, something_else  = base([option("Hi Sir"), 
                                           option("Greetings,")], 
                                          [option("Hi,")])

        main_root()
        something_else()
        main_root()
        something_else()

        main_root([option("I request more information on my assignment")])
        something_else([option("Tell me more.")])

    def create_response_template(self):
        self.response_template = Template("respond")
        base = self.response_template .make_base()
        option = self.response_template .make_option_creator()

        main_root, something_else  = base([option("Dear Sir,")],
                                          [option("sir,")])(lambda _:0)

        main_root()
        something_else()
        main_root()
        something_else()

        main_root([option("here is more")])
        something_else([option("rude!")])

    def get_writing_template(self):
        return self.initial_communication_template

    def get_response_template(self):
        return self.response_template

class You(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)

    def create_address(self,district_name):
        return Personage.create_address(self,
                                        district_name+" District Administration",
                                        "New Street Buildings Q.K.8",
                                        "You.")

    def proccess_inbox(self):
        self.move_yesterdays_inbox()

