from typing import DefaultDict


class Template:

    def __init__(self):
        self.base = {}

    def make_reader(self):

        at = self.base
        index = 0
        contents = DefaultDict(list)

        def choices():
            return list(at.keys())

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
            info = at[choices()[index]]["info"]
            for key in list(info.keys()):
                contents[key].append(info[key])

            at = at[choices()[index]]["branch"]
            index = 0

        def end():
            if at == {}:
                return True
            return False

        def get_contents():
            return contents

        return {"choices":choices,"read":read,"left":left,"right":right,"choose":choose,"end":end,"contents":get_contents}

    def make_base(self):
        self.base = {}
        return self.node(self.base)

    def make_option_creator(self):
        def option(text, **kwargs):
            return kwargs | {"text":text} 
        return option


    def node(self,position):
        split = False
        pos = position

        def caller(*lists_of_options):
            nonlocal split,pos

            if split:
                raise RuntimeError("Node already split")

            if len(lists_of_options) == 0:
                lists_of_options = [[{"text":"\n"}]]

            if len(lists_of_options) == 1 and len(lists_of_options[0]) == 1 :
                branch = {}
                option = lists_of_options[0][0]
                pos[option["text"]] = {"branch":branch, "info":option}
                pos = branch
            else:
                branches = [{} for _ in range(len(lists_of_options))]
                for branch_index in range(len(branches)):
                    for option in  lists_of_options[branch_index]:
                        pos[option["text"]] = {"branch":branches[branch_index], "info":option}

                new_nodes = [self.node(branches[branch_index]) for branch_index in range(len(branches))]

                split = True
                return tuple(new_nodes)

        return caller

"""
initial_communication = Template()
base = initial_communication.make_base()
option = initial_communication.make_option_creator()

main_root, something_else  = base([option("Hi Sir", formal = 1), 
                                   option("Greetings,")], 
                                  [option("Honey,")])

main_root()
something_else()

main_root([option("I request more information on my assignment")])
something_else([option("Theres a bee in the kitchen... OwO.")])

print(initial_communication.base)"""