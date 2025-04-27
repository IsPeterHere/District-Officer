from People.Templates.Template import Template 

class Responding:
    def create_response_template(self):

        def formality(letter_contents):
            if "formal" in letter_contents:
                return 0
            return 1

        self.response_template = Template("respond")
        base = self.response_template .make_base()
        option = self.response_template .make_option_creator()

        main_root, something_else  = base([option("Dear Sir,")],
                                          [option("sir,")])(formality)

        main_root()
        something_else()
        main_root()
        something_else()

        main_root([option("here is more")])
        something_else([option("rude!")])