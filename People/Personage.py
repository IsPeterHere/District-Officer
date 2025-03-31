from Post.Adressing import Address

class Personage():

    def __init__(self,instance):
        self.instance = instance
        self.__address = None
        self.__inbox = dict()

        self.instance.data.people.add(self)

    def get_address(self):
        return self.__address

    def create_address(self,line1,line2,desc = "",name = None,signature = None):
        self.__address = Address(self,line1,line2,desc,name,signature)
        return self.__address

    def add_to_inbox(self,delivery_date,letter):
        assert delivery_date > self.instance.data.the_date(), "A letter must be added to a future inbox"
        self.__inbox.get(delivery_date,list()).append(letter)

    def get_todays_inbox(self):
        return self.__inbox.get(self.instance.data.the_date(),list())

    def clear_todays_inbox(self):
        self.__inbox[self.instance.data.the_date()] = list()

    def proccess_inbox(self):
        inbox = self.get_todays_inbox()
        self.clear_todays_inbox()

        for letter in inbox:
            self.reply(letter)
