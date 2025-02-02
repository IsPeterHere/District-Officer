from importlib.resources import contents
from time import time
from District import District
from Display import Display
from datetime import date
from Adressing import Address,Address_book

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
        received_letter = Letter(self.general_secretariat,self.date,self.display)

        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing now ",
                   "the secretariats responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   "administer the largely rural district of ________")
        district_name = received_letter.show_letter("<Enter District Name>",type_line1 = True)
        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing now ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   f"administer the largely rural district of {district_name}.",
                   "",
                   "Contact the WT Division for further details.")
        district_name = received_letter.show_letter()
        return district_name

class Letter:

    def __init__(self,address,date,display, signoff = "Yours sincerely"):
        self.display = display

        self.address = address
        self.date = date
        self.signoff = signoff
    
    def set_contents(self,*lines_of_text):
        self.contents = list(lines_of_text)

    def show_letter(self,prompt = "<Press Enter to Confirm Read>",type_line1 = False):
        letter_box = self.display.text_box(3,25,10,120)

        if type_line1:
            letter_box.type(0," "*60 + self.address.line1,speed = 0.07)

        letter = [" "*60 + self.address.line1,
                  " "*64 + self.address.line2,
                  " "*68 + "{0:%b}. {0:%d}-{0:%y}".format(self.date)]+self.contents+[
                  " "*60+self.signoff+",",
                  " "*60+self.address.get_sign()]

        letter_box.print([0,1,2]+[7+x for x in range(len(self.contents))]+[19,21],*letter)

        user_input = self.display.get_input(prompt)
        self.display.clear()

        return user_input


class Main(Sequences):

    def __init__(self):
        self.date = date(1904, 1, 1)
        self.district = District(10)
        self.display = Display(self.district.map)

        self.general_secretariat = Address("General Secretariat",
                                           "Old Street Buildings A.N.1",
                                           "The Executive Branch of the territorial civil service")

        self.address_book = Address_book(self.display,self.date)
        self.address_book.add(self.general_secretariat)

        start_key = self.start_up()
        if "d" in start_key:
            self.show_debug()

        if "o" in start_key:
            self.address_book.open_book()
        
        self.district.name = self.intro()
        self.address_book.open_book()
        

Main()