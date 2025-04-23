from InOut.Terminal_py import Terminal
from time import sleep
from Post.Adressing import Address_book
from Post.Letter import Letter

class DisplayObjects:

    def show_letter(self,letter,type_line1,show_address,show_signature):
        letter_box = self.text_box(3,25,10,120)

        if type_line1:
            letter_box.type(0, " "*60 + letter.sender_address.line1,speed = 0.07)

        full_letter,indices = ([
                  " "*60 + letter.sender_address.line1,
                  " "*64 + letter.sender_address.line2,
                  " "*68 + "{0:%b}. {0:%d}-{0:%y}".format(letter.date)],[0,1,2]) if show_address else ([],[])
        
        full_letter,indices = (full_letter+letter.get_contents(),indices+[7+x for x in range(len(letter.get_contents()))])
       
        full_letter,indices = (full_letter + [
                  " "*60 + letter.signoff + ",",
                  " "*60 + letter.sender_address.get_sign()],indices+[19,21]) if show_signature else (full_letter,indices)

        letter_box.print(indices,*full_letter)

    def show_address_book(self,address_book,type_date):

        top_text = "Address Book --"+" "*27+"-- Inbox. "+str(len(address_book.you.get_todays_inbox()))+" items --"+" "*27
        date = "-- {0:%d} {0:%b}. {0:%Y}".format(address_book.the_date())

        if type_date:
            temp_bar = self.text_box(0,3,5,115)
            temp_bar.type(0,len(top_text)*" " + date)

        top_bar = self.text_box(0,3,5,115,bottom = "_")
        top_bar.print([0,1,2],top_text+date,
                "-"*110,
                "No   | "+"Name" + " "*17+"| Description")

        body = self.text_box(3,24,5,115,bottom = "_")

        lines = ["     |"+" "*22+"|" for x in range(21)]

        addresses = list(address_book.get_Addresses().values())
        for line in range(len(addresses)):
            code = addresses[line].code
            name = addresses[line].get_name()
            desc = addresses[line].desc
            lines[line] = f"{code} | {name}"+" "*(21-len(name))+f"| {desc}"

        body.print([x for x in range(1,21)],*lines)

class Display(Terminal,DisplayObjects):

    def __init__(self):
        Terminal.__init__(self)

        self.input_prompt_box = None
        
    def input_prompt(self,prompt):
        if prompt != "":
            prompt = "\033[38;5;243m"+prompt+"\033[0m"
            self.input_prompt_box = self.text_box(26,28,10,120)
            prompt = prompt.split("\n")+[" "]
            self.input_prompt_box.print([0,1],*prompt)
        
    def remove_input_prompt(self):
        if self.input_prompt_box != None:
            self.remove_text_box(self.input_prompt_box)
            self.input_prompt_box = None

    def get_input(self,prompt = ""):
        sleep(0.04)
        self.input_prompt(prompt)
        inp = input()
        self.change_made()
        sleep(0.04)
        self.remove_input_prompt()
        return inp


    def __call__(self,object,prompt = "<Press Enter to Continue>",**flags):
        match(object):

            case Letter():
                self.show_letter(object,flags.get('type',False),flags.get('address',True),flags.get('signature',True))

            case Address_book():
                self.show_address_book(object,flags.get('type',False))
        
        if flags.get("input",True):
            user_input = self.get_input(prompt)
            self.clear()

            return user_input
        self.clear()
