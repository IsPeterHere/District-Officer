from People.Personage import Personage
from People.Templates.Template import Template 
from People.Hiring import Person
from Post.Letter import Letter
from Post.Adressing import Address

class Writng:
    def initial_communication(self):
        template = Template("write")
        base = template.make_base()
        option = template.make_text_option_creator()

        base([option("Hi Sir,"), 
            option("Greetings,"),
            option("Hi,")])

        base()
        base()

        hints,skip_hints = base([option("I would like to know more about my assignment.", hints = True)],
                  [option("I am familiar with the particulars of my new assignment ", hints = False)])

        skip_hints = skip_hints([option("...")])

        return template
    
    def choose_secetary(self):
        initial_communication_template = Template("write")
        base = initial_communication_template.make_base()
        option = initial_communication_template.make_text_option_creator()

        base([option("Hi Sir,"), 
            option("Greetings,"),
            option("Hi,")])
    
        base()
        base()
        
        base([option(f"I would like to pick {self.secetary_candidate_1.first_name} {self.secetary_candidate_1.surname} for the position of secratry.", candidate = 0),
              option(f"I would like to pick {self.secetary_candidate_2.first_name} {self.secetary_candidate_2.surname} for the position of secratry.", candidate = 1),
              option(f"I would like to pick {self.secetary_candidate_3.first_name} {self.secetary_candidate_3.surname} for the position of secratry.", candidate = 2)
            ])

        return initial_communication_template

class Responding:
    def initial_response(self):

        def give_extra_hints(received_letter_contents):
            if received_letter_contents["hints"][0]:
                return 0
            return 1

        template = Template("respond")
        base = template .make_base()
        text_option = template .make_text_option_creator()
        function_option = template .make_function_option_creator()
        
        hints, no_hints  = base([text_option("Dear Sir, your assignment is as follows,")],
                                          [text_option("sir...")])(give_extra_hints)

        hints()
        hints()
        hints([text_option("The Western regions are in a dire state, they are lacking in infrastructure, housing, and even basic civil governance. "+
                      "Fortunately limited Control has been established over the regions and us at the GA have been given clearance to start forming a civilian administration. "+
                      f"In your new capacity as District Officer you have been assigned to the district of {self.instance.data.district.name}. " +
                      "Your role is to work on developing the district lifting it out of its current poverty while also building a strong government. " +
                      "The region is unstable and central recourses are limited so one thing is absolutely crucial, control must be maintained.")])

        hints()
        hints()
        hints([text_option("There are 3 candidates for the position of your secretary forwarded with this letter. Please tell us which candidate seems most suitable.")])
        
        def add_secetary_attachments(letter,received_letter_contents):
            self.secetary_candidate_1 = Person()
            self.secetary_candidate_2 = Person("M")
            self.secetary_candidate_3 = Person("F")
            
            letter.attachments["Candidate 1"] = self.secetary_candidate_1.get_CV() 
            letter.attachments["Candidate 2"] = self.secetary_candidate_2.get_CV() 
            letter.attachments["Candidate 3"] = self.secetary_candidate_3.get_CV() 
            
            if received_letter_contents["hints"][0]:
                what_is_secetary = Letter(self.instance,Address(None,"ATTACHED NOTE","",signature=""),signoff="")
                what_is_secetary.set_contents_vague(
                    "The role of (Cheif Administrative) secratry is arguably the most essentail role within a good district",
                    "administaration. They will be in charge of the day to day running of the head office of your district",
                    "administartion. Managemnt of hiring, depertments, and fincnace will all be based in your head office,",
                    "and hence your secretary will be the goto point of contact for these areas.")
                letter.attachments["Role of Secetary"] = what_is_secetary
                
            self.state = "Choose secetary"
            
        hints([function_option(add_secetary_attachments)])
        hints([text_option("PROMPT:choose_secetary")])
        return template

    def choose_secetary_response(self):

            def choice(letter_contents):
                return letter_contents["candidate"][0]

            template = Template("respond")
            base = template .make_base()
            text_option = template .make_text_option_creator()
            function_option = template .make_function_option_creator()
            
            base([text_option("Hi,")])
            base()
            base()
            
            base([text_option(f"You picked {self.secetary_candidate_1.first_name} {self.secetary_candidate_1.surname} for the position of secratry."),
                  text_option(f"You picked {self.secetary_candidate_2.first_name} {self.secetary_candidate_2.surname} for the position of secratry."),
                  text_option(f"You picked {self.secetary_candidate_3.first_name} {self.secetary_candidate_3.surname} for the position of secratry.")
                ])(choice)
            return template

class General_secretariat(Personage,Writng,Responding):

    def __init__(self,instance):
        Personage.__init__(self,instance)
        self.create_address("General Secretariat",
                            "Old Street Buildings A.N.1",
                            "The Executive Branch of the territorial civil service")
        
        self.state = "Start"


    def get_writing_template(self):
        match (self.state):
            case "Start":
                return self.initial_communication()
            case "Choose secetary":
                if self.instance.you.do_if_prompt("choose_secetary"):
                    return self.choose_secetary()
            
        return None;


    def get_response_template(self):
        match (self.state):
            case "Start":
                return self.initial_response()
            case "Choose secetary":
                
                return self.choose_secetary_response()
            case _:
                raise RuntimeError("Unrecognised state: "+str(self.state))