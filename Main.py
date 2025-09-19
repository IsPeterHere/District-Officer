from Post.Adressing import Address_book
from Post.Letter import Letter
from Instance import Instance
from People.Hiring import Person

class Main:
    instance = None
    
    def set_instance(instance):
        Main.instance = instance
        Person.instance = instance

    def __init__(self):
        self.address_book = Address_book(self.instance)
        self.address_book.add(self.instance.general_secretariat.get_address())

    def start(self):
        start_key = self.instance.display("Start","Press Enter")
        
        if "d" in start_key:
            self.instance.display("Debug","Press Enter")
            
        if "o" in start_key:
            self.instance.data.district.name = "test_district"
            self.instance.you.create_address(self.instance.data.district.name)
            users_first_letter = Letter(self.instance,self.instance.you.get_address(),self.instance.general_secretariat.get_address())
            users_first_letter.write(self.instance.general_secretariat.get_writing_template(self.instance.general_secretariat.get_writing_template_index()),make_signature=True,exitable = False)
            users_first_letter.send(days_till_delivery=1)

        else:
        
            self.instance.data.district.name = self.intro()
            self.instance.you.create_address(self.instance.data.district.name)

            self.address_book.open_book(read = False,day = False)

            users_first_letter = Letter(self.instance,self.instance.you.get_address(),self.instance.general_secretariat.get_address())
            users_first_letter.write(self.instance.general_secretariat.get_writing_template(self.instance.general_secretariat.get_writing_template_index()),make_signature=True,exitable = False)
            users_first_letter.send(days_till_delivery=1)

            self.address_book.open_book(write = False,read = False)

        self.main_loop()

    
    def intro(self):
        received_letter = Letter(self.instance,self.instance.general_secretariat.get_address())
    
        received_letter.set_contents_exact(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are now, as of the time of writing, ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   "administer the largely rural district of ________")
    
        while (district_name :=  self.instance.display(received_letter,"Text Entry", prompt = "<Enter District Name>",type = True)) == "":
            pass
    
        received_letter.set_contents_exact(
                   "Good Sir. ","","",
                   "As i am sure you are aware the Western Territories(WT) are now, as of the time of writing, ",
                   "the secretariat's responsibility.",
                   "The Advisory Political Committee has assigned you and a small selection of staff to",
                   f"administer the largely rural district of {district_name}. To carry out these duties you are hereby",
                   "promoted to the grade of District Officer. Congratulations.",
                   "",
                   "Please contact the General Secretariat for further details.")
    
        self.instance.display(received_letter,"Press Enter")
        return district_name

    def main_loop(self):


        while True:
            self.instance.next_day()
            user_input = self.address_book.open_book(typed = True)

            while True:
                match user_input:
                    case None:
                        pass
                    case "d":
                        break
                    case "o":
                        letter = self.instance.you.pop_inbox()
                        letter.transfer_prompts(self.instance.you)
                        while user_input != "x":
                            user_input = self.instance.display(letter,"Read Letter", exit = True, attachments = letter.attachments)
                            if user_input == "a":
                                while True:
                                    user_input = letter.display_attachments()
                                    if user_input == "x":
                                        break
                                    l = list(letter.attachments.keys())
                                    self.instance.display(letter.attachments[l[int(user_input)-1]],"Press Enter"),
                                                          
                                user_input= "a"
                                    
                                
                    case _:
                        try:
                            writing_to = self.address_book.get_Addresses()[user_input]
                        except:
                            self.instance.display.NOTE_invalid_input()
                        else:
                            if writing_to.person.get_writing_template_index() != None:
                                template = writing_to.person.get_writing_template(writing_to.person.get_writing_template_index())
                                letter = Letter(self.instance, self.instance.you.get_address(),writing_to)
                                written = letter.write(template)
                                if written:
                                    letter.send(days_till_delivery=1)

                                

                user_input = self.address_book.open_book()

                
            
        
if __name__ == "__main__":
    Main.set_instance(Instance())
    Main().start()
