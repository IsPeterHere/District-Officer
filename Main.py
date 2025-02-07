from time import time
from District import District
from Display import Display
from Date import Date
from Adressing import Address,Address_book
from Letter import Letter
from Personage import Personage
from root import Root

class Sequences:

    def show_debug(self):
        
        debug = self.display.text_box(6,20,20,100)
        debug.type(0,"DEBUG -- "+str(time()),speed = 0.04)
        debug(1,str(self.display.size)+"   -2 lines")
        self.display.debug = True

        self.wait_for_confirmation()

    def start_up(self):

        start_text = self.display.text_box(6,20,20,100)
        start_text(7,"Press Enter to Start")
        start_key = self.display.get_input()
        self.display.clear()

        return start_key

    def wait_for_confirmation(self):
        self.display.get_input("<Press Enter to Confirm Read>")
        self.display.clear()

    def intro(self):
        received_letter = Letter(Address(None,"Central Administration",
                                         "Capital Buildings A.A.1",
                                         "The highest body in the civil service"),
                                 self.data.the_date(),self.display)

        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing now ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   "administer the largely rural district of ________")

        district_name = self.display(received_letter,"<Enter District Name>",type = True)

        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing now ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   f"administer the largely rural district of {district_name}. Congratulations.",
                   "",
                   "Please contact the General Secretariat for further details.")

        self.display(received_letter,"<Press Enter to Confirm Read>")
        return district_name

class General_secretariat(Personage):

    def __init__(self):
        Personage.__init__(self)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")

    def reply(self):
        pass

class You(Personage):

    def __init__(self):
        Personage.__init__(self)

    def create_address(self,district_name):
        return Personage.create_address(self,
                                        district_name+" District Administration",
                                        "New Street Buildings Q.K.8",
                                        "You.")

    def proccess_inbox(self):
        pass

class Main(Sequences,Root):

    def __init__(self):

        self.data.the_date = Date(1924, 1, 1)
        self.data.district = District(size = 10)

        self.display = Display()
        self.general_secretariat = General_secretariat()
        self.you = You()
        self.address_book = Address_book(self.display,self.you)
        self.address_book.add(self.general_secretariat.get_address())

    def start(self):
        start_key = self.start_up()

        if "s" in start_key:
            self.display.typing = False

        if "d" in start_key:
            self.show_debug()

        if "o" in start_key:

            self.you.create_address("test_district")
            users_first_letter = Letter(self.you.get_address(),self.display,self.general_secretariat.get_address())
            users_first_letter.set_contents("Hi, can i have more details on my assignment.")
            users_first_letter.send(days_till_delivery=1)

        else:
        
            self.data.district.name = self.intro()
            self.you.create_address(self.data.district.name)

            self.address_book.open_book(prompt="<Enter No. to Write Letter (i.e 78 or 0078)>")

            users_first_letter = Letter(self.you.get_address(),self.display,self.general_secretariat.get_address())
            users_first_letter.write(make_signature=True)
            users_first_letter.send(days_till_delivery=1)

            self.address_book.open_book(accept_codes=False,other_accepted_inputs = ["day"],prompt="<It may take a day or more for a reply to arrive>   <Enter 'day' to finsh the day>")

        self.main_loop()


    def main_loop(self):
        while True:
            self.data.the_date.next_day()
            self.data.people.read_and_reply()
            self.address_book.open_book(type_date=True)
            
        
if __name__ == "__main__":
    Main().start()