from datetime import timedelta

class Letter:

    number_of_lines = 12
    non_selected_colour = ["\033[38;5;243m","\033[0m"]

    def __init__(self,instance,sender_address,delivery_address = None, signoff = "Yours sincerely"):
        self.instance = instance
        self.delivery_address = delivery_address

        self.display = self.instance.display
        self.sender_address = sender_address
        self.date = self.instance.data.the_date()
        self.signoff = signoff

        self.__contents = []
        self.__written_template_contents = None

        self.sent = False
    
    def set_contents(self,*lines_of_text):
        assert len(lines_of_text) <= Letter.number_of_lines, f"letter must be {self.number_of_lines} lines or less" 
        self.__contents = list(lines_of_text)

    def get_contents(self):
        return self.__contents


    def write(self, type_line1 = False,make_signature = False, exitable = True):
        self.display(self,input = False,type = type_line1,signature = False)

        template_reader = self.delivery_address.person.get_writing_template().make_reader()
        self.__contents = [""]
        chosen_contents = [""]

        def display():
            _next = template_reader["read"]()
            self.__contents[-1] += self.non_selected_colour[0]+_next+self.non_selected_colour[1]
            if len(template_reader["choices"]()) > 1:
                return self.display(self,prompt = "<Enter 'x' To Exit> <Enter 'n' / 'm' To Scroll Choices> <Press Enter To Select>",signature = False)
            return self.display(self,prompt = "<Enter 'x' To Exit> <Press Enter To Select>",signature = False)
            
        while not template_reader["end"]():
            _input = display()
            if _input == "x" and exitable:
                return False
            
            if _input == "m":
                template_reader["right"]()
            elif _input == "n":
                template_reader["left"]()
            elif _input == "":
                chosen_contents[-1] += template_reader["read"]()
                template_reader["choose"]()

                while not template_reader["end"]() and template_reader["read"]() == "":
                    template_reader["choose"]()
                    self.__contents.append("")
                    chosen_contents.append("")

            self.__contents = chosen_contents.copy()


        self.__written_template_contents = template_reader["contents"]()

        if make_signature:
            self.sender_address.set_sign("_______________")
            while (signature := self.display(self,"<Enter Signature (PERMANENT)>")) =="":
                   pass
            self.sender_address.set_sign(signature)
            self.instance.data.player_signature = signature

        if exitable:
            _input = self.display(self,prompt =  "<Enter 'x' To Exit> <Press Enter To Send>")
            if _input == "x":
                return False
            return True
        else:
            self.display(self,prompt =  "<Press Enter To Send>")
            return True

    def get_written_template_contents(self):
        if self.__written_template_contents == None:
            raise RuntimeError("Letter has not been written")
        return self.__written_template_contents

    def send(self,days_till_delivery):
        assert self.sent == False, "Letter has already been sent"

        self.delivery_address.person.add_to_inbox(self.date + timedelta(days = days_till_delivery),self)
        self.sent = True
