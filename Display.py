from Terminal_py import Terminal
from time import sleep

class Display(Terminal):

    def __init__(self,district_map):
        Terminal.__init__(self)
        self.district_map = district_map

        self.input_prompt_box = None
        
    def input_prompt(self,prompt):
        self.input_prompt_box = self.text_box(26,27,10,100)
        self.input_prompt_box(0,prompt)

    def remove_input_prompt(self):
        if self.input_prompt_box != None:
            self.remove_text_box(self.input_prompt_box)
            self.input_prompt_box = None

    def get_input(self,prompt = ""):
        sleep(0.04)
        self.input_prompt(" "*10+prompt)
        inp = input()
        self.change_made()
        sleep(0.04)
        self.remove_input_prompt()
        return inp

