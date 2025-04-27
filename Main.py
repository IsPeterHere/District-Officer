from time import time
from Post.Adressing import Address_book
from Post.Letter import Letter
from Instance import Instance



class Sequences:

    def show_debug(self):
        
        debug = self.instance.display.text_box(6,20,20,100)
        debug.type(0,"DEBUG -- "+str(time()),speed = 0.04)
        debug(1,str(self.instance.display.size)+"   -2 lines")
        self.instance.display.debug = True

        self.wait_for_confirmation()

    def start_up(self):

        start_text = self.instance.display.text_box(6,20,20,100)
        start_text(7,"Press Enter to Start")
        start_key = self.instance.display.get_input()
        self.instance.display.clear()

        return start_key

    def wait_for_confirmation(self):
        self.instance.display.get_input("<Press Enter to Confirm Read>")
        self.instance.display.clear()

    def intro(self):
        received_letter = Letter(self.instance,self.instance.general_secretariat.get_address())

        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing, now ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   "administer the largely rural district of ________")

        while (district_name :=  self.instance.display(received_letter,"<Enter District Name>",type = True)) == "":
            pass

        received_letter.set_contents(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are, as of the time of writing, now ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   f"administer the largely rural district of {district_name}. To carry out these duties you are hereby",
                   "promoted to the grade of District Officer. Congratulations.",
                   "",
                   "Please contact the General Secretariat for further details.")

        self.instance.display(received_letter,"<Press Enter to Confirm Read>")
        return district_name


class Main(Sequences):

    def __init__(self):

        self.instance = Instance()
        
        self.address_book = Address_book(self.instance)
        self.address_book.add(self.instance.general_secretariat.get_address())

    def start(self):
        start_key = self.start_up()

        if "s" in start_key:
            self.instance.display.typing = False

        if "d" in start_key:
            self.show_debug()

        if "o" in start_key:
            self.instance.data.district.name = "test_district"
            self.instance.you.create_address(self.instance.data.district.name)
            users_first_letter = Letter(self.instance,self.instance.you.get_address(),self.instance.general_secretariat.get_address())
            users_first_letter.write(make_signature=True,exitable = False)
            users_first_letter.send(days_till_delivery=1)

        else:
        
            self.instance.data.district.name = self.intro()
            self.instance.you.create_address(self.instance.data.district.name)

            self.address_book.open_book(prompt="<Enter No. to Write Letter (i.e 1 or 0001)>")

            users_first_letter = Letter(self.instance,self.instance.you.get_address(),self.instance.general_secretariat.get_address())
            users_first_letter.write(make_signature=True,exitable = False)
            users_first_letter.send(days_till_delivery=1)

            self.address_book.open_book(accept_codes=False,other_accepted_inputs = ["d"],prompt="<It May Take a Day or More For a Reply to Arrive In Your Inbox>   <Enter 'd' to Finsh The Day> \n")

        self.main_loop()


    def main_loop(self):

        def display_book(typed = False):
            open_letter_prompt = "<Enter \'o\' to read next letter in inbox>" if self.instance.you.get_inbox(self.instance.data.the_date()) else "<Inbox Empty>"
            return self.address_book.open_book(type_date=typed,other_accepted_inputs = ["d","o"],prompt = f"<Enter a code to Write Letter>              {open_letter_prompt} \n<Enter 'd' to finsh the day>")

        while True:
            self.instance.next_day()
            user_inut =display_book(typed = True)

            while True:
                match user_inut:
                    case "d":
                        break
                    case "o":
                        letter = self.instance.you.pop_inbox()
                        if letter != None:
                            self.instance.display(letter)

                    case _:
                        writing_to = self.address_book.get_Addresses()[user_inut]
                        letter = Letter(self.instance, self.instance.you.get_address(),writing_to)
                        written = letter.write()
                        if written:
                            letter.send(days_till_delivery=1)

                user_inut = display_book()

                
            
        
if __name__ == "__main__":
    Main().start()
