from People.Templates.Template import Template 

class Writng:
    def create_writing_templates(self):
        self.initial_communication_template = Template("write")
        base = self.initial_communication_template.make_base()
        option = self.initial_communication_template.make_option_creator()

        main_root,  = base([option("Hi Sir,"), 
                            option("Greetings,"),
                            option("Hi,")])

        main_root()
        main_root()

        hints,skip_hints = main_root([option("I would like to know more about my assignment.", hints = True)],
                  [option("I am familiar with the particulars of my new assignment ", hints = False)])

        skip_hints = skip_hints([option("...")])