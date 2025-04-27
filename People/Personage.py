from typing import DefaultDict
from Post.Adressing import Address
from Post.Letter import Letter
import random


class Personage():

    def __init__(self,instance):
        self.instance = instance
        self.__address = None
        self.__inbox = DefaultDict(list)

        self.signoff = "Yours sincerely"

        self.instance.data.people.add(self)

    def get_address(self):
        return self.__address

    def create_address(self,line1,line2,desc = "",name = None,signature = None):
        self.__address = Address(self,line1,line2,desc,name,signature)
        return self.__address

    def add_to_inbox(self,delivery_date,letter):
        assert delivery_date >= self.instance.data.the_date(), "Invalid delivery date"
        self.__inbox[delivery_date].append(letter)

    def get_inbox(self,day):
        return self.__inbox[day]

    def set_inbox(self,day,inbox):
        self.__inbox[day] = inbox

    def clear_inbox(self,day):
        del self.__inbox[day]

    def proccess_inbox(self):
        inbox = self.get_inbox(self.instance.data.the_date())
        self.clear_inbox(self.instance.data.the_date())
        for letter in inbox:
            self.reply(letter)

    def reply(self,letter):
        reply_letter = Letter(self.instance,self.get_address(),letter.sender_address,self.signoff) 
        reply_letter.set_contents(*self.get_response_template().write_response(letter))
        reply_letter.send(self.get_delivery_time())
        


    def get_delivery_time(self):
        return random.randint(0,1)

    def get_writing_template(self):
        raise RuntimeError(f"No Writing template defined for {self.__address.get_name()}")

    def get_response_template(self):
        raise RuntimeError(f"No Response template defined for {self.__address.get_name()}")