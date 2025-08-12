from typing import DefaultDict


class Template:

    max_width = 99

    def __init__(self,type):
        match(type):
            case "respond":
                self.type = type
            case "write":
                self.type = type
            case _:
                raise RuntimeError("Template must have valid type")

        self.base = {}

    def make_reader(self):

        at = self.base
        index = 0
        contents = DefaultDict(list)

        def response_function(letter_contents):
            nonlocal index
            index = at["response_func"](letter_contents)

        def choices():
            return list(at["options"].keys())

        def read():
            return choices()[index]

        def left():
            nonlocal index
            index -= 1
            if index < 0:
                index = len(choices())-1

        def right():
            nonlocal index
            index += 1
            if index >= len(choices()):
                index = 0

        def choose():
            nonlocal at,index,contents
            info = at["options"][choices()[index]]["info"]
            for key in list(info.keys()):
                contents[key].append(info[key])

            at = at["options"][choices()[index]]["branch"]
            index = 0

        def end():
            if at["options"] == {}:
                return True
            return False

        def get_contents():
            return contents

        return {"choices":choices,"read":read,"left":left,"right":right,"choose":choose,"end":end,"contents":get_contents,"response_function":response_function}

    def write_response(self,reply_letter,received_letter):
        if self.type != "respond":
            raise RuntimeError("template cant respond as it is not of a response type")

        contents = [""]

        reader = self.make_reader()
        ch = 0
        while not reader["end"]():


            if len(reader["choices"]()) == 1:
                chosen = reader["read"]()
                reader["choose"]()
            else:
                reader["response_function"](received_letter.get_written_template_contents())
                chosen = reader["read"]()
                reader["choose"]()
            
            if callable(chosen):
                chosen = chosen(reply_letter,received_letter.get_written_template_contents())
            
            if chosen != None:
                if chosen == "":
                    contents.append("")
                    ch = 0
                else:
                    while ch + len(chosen) > self.max_width:
    
                        pivot = self.max_width - ch
                        while pivot >= 1 and chosen[pivot] != " ":
                            pivot -= 1
    
                        if pivot == 0:
                            raise RuntimeError(f"Word exceeded maximum with of {self.max_width}")
    
                        contents[-1] += chosen[:pivot+1]
                        contents.append("")
                        chosen = chosen[pivot+1:]
                        ch = 0
    
                    ch += len(chosen)
                    contents[-1] += chosen 

        reply_letter.set_contents(*contents)



    def make_base(self):
        self.base = {"options":{},"response_func":None}
        return self.node(self.base)

    def make_text_option_creator(self):
        def option(text, **kwargs):
            return kwargs | {"__text":text} 
        return option
    
    def make_function_option_creator(self):
        def option(text, **kwargs):
            return kwargs | {"__text":text} 
        return option

    def node(self,position):
        split = False
        pos = position

        def response_func_setter(new_nodes):
            nonlocal pos
            def response_func_set(response_function):
                nonlocal pos
                if not callable(response_function):
                    raise RuntimeError("Response function not provided")
                if pos["response_func"] != None:
                    raise RuntimeError("Response function already set")

                pos["response_func"] = response_function
                
                if callable(new_nodes):
                    pos = new_nodes
                    
                return new_nodes

            return response_func_set
            


        def caller(*lists_of_options):
            nonlocal split,pos

            if split:
                raise RuntimeError("Node already split")

            if len(lists_of_options) == 0:
                lists_of_options = [[{"__text":""}]]



            if len(lists_of_options) == 1:
                branch = {"options":{},"response_func":None}
                option = lists_of_options[0][0]
                for option in  lists_of_options[0]:
                    pos["options"][option["__text"]] = {"branch":branch, "info":option}
                
                if self.type == "respond" and len(lists_of_options[0]) > 1:
                    return response_func_setter(self.node(branch))
                
                pos = branch
                
            else:
                branches = [{"options":{},"response_func":None} for _ in range(len(lists_of_options))]
                for branch_index in range(len(branches)):
                    for option in  lists_of_options[branch_index]:
                        pos["options"][option["__text"]] = {"branch":branches[branch_index], "info":option}

                new_nodes = tuple([self.node(branches[branch_index]) for branch_index in range(len(branches))])

                split = True
                match (self.type):
                    case "respond":
                        return response_func_setter(new_nodes)
                    case "write":
                        return new_nodes

        return caller

"""
initial_communication = Template("write")
base = initial_communication.make_base()
option = initial_communication.make_option_creator()

main_root, something_else  = base([option("Dear Sir,"), 
                                    option("Greetings,")], 
                                    [option("Hi")])

main_root()
something_else()
main_root()
something_else()

main_root([option("I request more information on my assignment")])
something_else([option("Tell me more.")])


initial_response = Template("respond")
base = initial_response.make_base()
option = initial_response.make_option_creator()

main_root, something_else  = base([option("Dear Sir,")],
                                  [option("sir,")])(lambda x:0)

main_root()
something_else()
main_root()
something_else()

main_root([option("here is more")])
something_else([option("rude!")])

print(initial_response.write_response(""))"""