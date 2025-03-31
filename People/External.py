from People.Personage import Personage

class General_secretariat(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")

        self.initial_communication = False

    def reply(self):
        if self.initial_communication:
            pass

        else:
            success = self.reply_initial_communication()
            if success:
                self.initial_communication = True

    def reply_initial_communication(self):
        pass

class You(Personage):

    def __init__(self,instance):
        Personage.__init__(self,instance)

    def create_address(self,district_name):
        return Personage.create_address(self,
                                        district_name+" District Administration",
                                        "New Street Buildings Q.K.8",
                                        "You.")

    def proccess_inbox(self):
        pass

    def add_to_inbox(self,delivery_date,letter):
        self.__inbox.get(delivery_date,list()).append(letter)
