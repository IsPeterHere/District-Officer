from People.Personage import Personage
from datetime import timedelta
from People.Templates.Writing.General_secretariat import Writng
from People.Templates.Responses.General_secretariat import Responding

class General_secretariat(Personage,Writng,Responding):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")



        self.create_writing_templates()
        self.create_response_template()

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
        
