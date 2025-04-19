from datetime import timedelta

class Letter:

    number_of_lines = 10
    non_selected_colour = ["\033[38;5;243m","\033[0m"]

    def __init__(self,instance,address,delivery_address = None, signoff = "Yours sincerely"):
        self.instance = instance
        self.delivery_address = delivery_address

        self.display = self.instance.display
        self.sender_address = address
        self.date = self.instance.data.the_date()
        self.signoff = signoff

        self.contents = []
        self.template_info_contents = []

        self.sent = False
    
    def set_contents(self,*lines_of_text):
        assert len(lines_of_text) <= Letter.number_of_lines, f"letter must be {self.number_of_lines} lines or less" 
        self.contents = list(lines_of_text)


    def write(self, type_line1 = False,make_signature = False):
        self.display(self,input = False,type = True,signature = False)

        template_reader = self.delivery_address.person.get_template().make_reader()
        self.contents = [""]

        def display():
            _next = template_reader["read"]()
            self.contents[-1] = self.non_selected_colour[0]+_next+self.non_selected_colour[1]
            if len(template_reader["choices"]()) > 1:
                return self.display(self,prompt = "<Enter 'x' To Exit> <Enter 'n' / 'm' To Scroll Choices>")
            return self.display(self,prompt = "<Enter 'x' To Exit> <Press Enter To Select>")
            
        while (_input :=  display())!= "x":
            if _input == "m":
                template_reader["right"]()
            elif _input == "n":
                template_reader["left"]()
            elif _input == "":
                self.contents[-1] = self.contents[-1].replace(self.non_selected_colour[0], '').replace(self.non_selected_colour[1], '')
                template_reader["choose"]()

                while not template_reader["end"]() and (chosen := template_reader["read"]()) == "\n":
                    template_reader["choose"]()
                    self.contents.append("")
        
            if template_reader["end"]():
                break

        self.template_info_contents = template_reader["contents"]()

        if make_signature:
            self.sender_address.set_sign("_______________")
            while (signature := self.display(self,"<Enter Signature (PERMANENT)>")) =="":
                   pass
            self.sender_address.set_sign(signature)
            self.instance.data.player_signature = signature

        self.display(self)

    def send(self,days_till_delivery):
        assert self.sent == False, "Letter has already been sent"

        self.delivery_address.person.add_to_inbox(self.date + timedelta(days = days_till_delivery),self)
        self.sent = True
