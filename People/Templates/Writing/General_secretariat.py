from People.Templates.Template import Template 

class Writng:
    def create_writing_templates(self):
        self.initial_communication_template = Template("write")
        base = self.initial_communication_template.make_base()
        option = self.initial_communication_template.make_option_creator()

        main_root, something_else  = base([option("Hi Sir"), 
                                           option("Greetings,")], 
                                          [option("Hi,")])

        main_root()
        something_else()
        main_root()
        something_else()

        main_root([option("I request more information on my assignment",formal = True)])
        something_else([option("Tell me more.")])