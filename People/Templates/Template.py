
class Template:

    def __init__(self):
        self.base = {}

    def make_reader(self):

        at = self.base["root"]
        index = 0

        def read():
            choices = list(at.keys())
            return choices[index]
        
        def left():
            nonlocal index
            index -= 1
            if index < 0:
                index = len(list(at.keys()))-1

        def right():
            nonlocal index
            index += 1
            if index >= len(list(at.keys())):
                index = 0

        def choose():
            nonlocal at,index 
            at = at[list(at.keys())[index]]
            index = 0

        def end():
            if at == {}:
                return True
            return False

        return {"read":read,"left":left,"right":right,"choose":choose,"end":end}

    def make_base(self):
        self.base["root"] = {}
        return self.node(self.base["root"])

    def node(self,position):
        called = False

        def caller(*lists_of_options):
            nonlocal called

            if called:
                raise RuntimeError("Node already setup")

            if len(lists_of_options) == 0:
                lists_of_options = [["\n"]]

            branches = [{} for _ in range(len(lists_of_options))]
            for branch_index in range(len(branches)):
                for option in  lists_of_options[branch_index]:
                    position[option] = branches[branch_index]

            new_nodes = [self.node(branches[branch_index]) for branch_index in range(len(branches))]

            called = True
            return tuple(new_nodes)

        return caller


"""initial_communication = Template()
base = initial_communication.make_base()
        
main_root, something_else  = base(["Hi Sir", "Greetings,"], ["Honey,"])
main_root(["I request more information on my assignment"])
something_else(["Theres a bee in the kitchen... OwO."])

print(initial_communication.base)"""