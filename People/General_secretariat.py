from People.Personage import Personage
from People.Templates.Template import Template 

class Writng:
    def initial_communication(self):
        initial_communication_template = Template("write")
        base = initial_communication_template.make_base()
        option = initial_communication_template.make_option_creator()

        main_root,  = base([option("Hi Sir,"), 
                            option("Greetings,"),
                            option("Hi,")])

        main_root()
        main_root()

        hints,skip_hints = main_root([option("I would like to know more about my assignment.", hints = True)],
                  [option("I am familiar with the particulars of my new assignment ", hints = False)])

        skip_hints = skip_hints([option("...")])

        return initial_communication_template

class Responding:
    def initial_response(self):

        def formality(letter_contents):
            if letter_contents["hints"][0]:
                return 0
            return 1

        response_template = Template("respond")
        base = response_template .make_base()
        option = response_template .make_option_creator()

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
        hints([option("There are 3 candidates for the position of your secretary forwarded with this letter. Please tell us which candidate seems most suitable.")])

        return response_template



class General_secretariat(Personage,Writng,Responding):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")


    def get_writing_template(self):
        return self.initial_communication()

    def get_response_template(self):
        return self.initial_response()