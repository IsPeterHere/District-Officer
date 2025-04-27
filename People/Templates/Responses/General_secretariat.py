from People.Templates.Template import Template 

class Responding:
    def create_response_template(self):

        def formality(letter_contents):
            if letter_contents["hints"][0]:
                return 0
            return 1

        self.response_template = Template("respond")
        base = self.response_template .make_base()
        option = self.response_template .make_option_creator()

        hints, no_hints  = base([option("Dear Sir,")],
                                          [option("sir,")])(formality)

        hints()
        hints()