
from datetime import timedelta
from root import Root

class Letter(Root):

    number_of_lines = 10

    def __init__(self,address,display, delivery_address = None, signoff = "Yours sincerely"):
        self.display = display
        self.delivery_address = delivery_address

        self.sender_address = address
        self.date = self.data.the_date()
        self.signoff = signoff

        self.contents = []

        self.sent = False
    
    def set_contents(self,*lines_of_text):
        assert len(lines_of_text) <= Letter.number_of_lines, f"letter must be {self.number_of_lines} lines or less" 
        self.contents = list(lines_of_text)


    def write(self, type_line1 = False,make_signature = False):
        self.display(self,input = False,type = True,signature = False)

        self.contents = ["->"]+["."]*(Letter.number_of_lines-1)+[""]
        line = 0
        while line < Letter.number_of_lines and (user_input := self.display(self,"<Enter 'Done' to finish writing>",signature = False)).lower() != "done":
            self.contents[line] = user_input
            line += 1
            self.contents[line] = "->"
        
        self.contents = [line if line != "." and line != "->" else "" for line in self.contents]

        if make_signature:
            self.sender_address.set_sign("_______________")
            signature = self.display(self,"<Enter Signature (PERMANENT)>")
            self.sender_address.set_sign(signature)
            self.data.player_signature = signature

        self.display(self)

    def send(self,days_till_delivery):
        assert self.sent == False, "Letter has already been sent"

        self.delivery_address.person.add_to_inbox(self.date + timedelta(days = days_till_delivery),self)
        self.sent = True
