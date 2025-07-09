from InOut.Terminal_py import Terminal
from time import sleep
from InOut.InOutTemplate import ABSTRACT_IN_OUT

class In_Out(ABSTRACT_IN_OUT,Terminal):
    
    def __init__(self):
        Terminal.__init__(self)
        self.input_prompt_box = None
        
    def OUT_start_up(self):
        self.clear()
        
        start_text = self.text_box(6,20,20,100)
        start_text(7,"District Officer")

    def OUT_show_letter(self,letter,type_line1,show_address,show_signature):
        self.clear()
        
        letter_box = self.text_box(3,25,10,120)

        if type_line1:
            letter_box.type(0, " "*60 + letter.sender_address.line1,speed = 0.07)

        full_letter,indices = ([
                  " "*60 + letter.sender_address.line1,
                  " "*64 + letter.sender_address.line2,
                  " "*68 + "{0:%b}. {0:%d}-{0:%y}".format(letter.date)],[0,1,2]) if show_address else ([],[])
        
        full_letter,indices = (full_letter+letter.get_contents(),indices+[6+x for x in range(len(letter.get_contents()))])
       
        full_letter,indices = (full_letter + [
                  " "*60 + letter.signoff + ",",
                  " "*60 + letter.sender_address.get_sign()],indices+[19,21]) if show_signature else (full_letter,indices)

        letter_box.print(indices,*full_letter)

    def OUT_show_address_book(self,address_book,type_date):
        self.clear()
        
        top_text = "Address Book --"+" "*27+"-- Inbox. "+str(len(address_book.you.get_inbox(address_book.the_date())))+" items --"+" "*27
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

    
    def IN_Press_Enter(self):
        start_key = self.get_input("Press Enter To Continue")
        return start_key
    
    def IN_Text_Entry(self,prompt):
        pass
    
    def IN_Letter(self):
        pass
    
    def IN_Address_Book(self):
        pass
    
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