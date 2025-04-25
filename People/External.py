from People.Templates.Template import Template 
from People.Personage import Personage
from datetime import timedelta

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

        def formality(letter_contents):
            if "formal" in letter_contents:
                return 0
            return 1

        self.response_template = Template("respond")
        base = self.response_template .make_base()
        option = self.response_template .make_option_creator()

        main_root, something_else  = base([option("Dear Sir,")],
                                          [option("sir,")])(formality)

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
    def move_yesterdays_inbox(self):
        self.set_inbox(self.instance.data.the_date(),self.get_inbox(self.instance.data.the_date())+self.get_inbox(self.instance.data.the_date() - timedelta(days = 1)))
        self.clear_inbox(self.instance.data.the_date() - timedelta(days = 1))

    def pop_inbox(self):
        inbox = self.get_inbox(self.instance.data.the_date())
        if len(inbox) == 0:
            return None

        letter = inbox.pop()
        self.set_inbox(self.instance.data.the_date(),inbox)
        return letter


    def proccess_inbox(self):
        self.move_yesterdays_inbox()
        
