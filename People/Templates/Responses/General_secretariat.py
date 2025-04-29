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

        hints, no_hints  = base([option("Dear Sir, your assignment is as follows,")],
                                          [option("sir...")])(formality)

        hints()
        hints()
        hints([option("The Western regions are in a dire state, they are lacking in infrastructure, housing, and even basic civil governance. "+
                      "Fortunately limited Control has been established over the regions and us at the GA have been given clearance to start forming a civilian administration. "+
                      f"In your new capacity as District Officer you have been assigned to the district of {self.instance.data.district.name}. " +
                      "Your role is to work on developing the district to lift it out of its current poverty while also building a strong government. " +
                      "The region is unstable and central recourses are limited so one thing is absolutely crucial, control must be maintained.")])

        hints()
        hints()
        hints([option("There are 3 candidates for the position of your secretary attached to this letter. Please tell us which candidate seems most suitable.")])
