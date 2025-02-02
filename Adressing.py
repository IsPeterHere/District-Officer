class Address:

    def __init__(self,line1,line2,desc = "",name = None,signatory = None):
        self.code = None
        self.line1 = line1
        self.line2 = line2
        self.desc = desc
        self.__name = name
        self.__signatory = signatory

    def get_name(self):
        if self.__name == None:
            return self.line1
        return self.__name

    def get_sign(self):
        if self.__signatory == None:
            return "INS. "+self.get_name()
        else:
            return self.__signatory


class Address_book:

    def __init__(self,display,date):
        self.display = display
        self.date = date
        self.__addresses = dict()

        self.__code = 1

    def open_book(self):
        top_bar = self.display.text_box(0,3,5,115,bottom = "_")
        top_bar.print([0,1,2],"Address Book"+" "*80+"-- {0:%d} {0:%b}. {0:%Y}".format(self.date),
                "-"*110,
                "No   | "+"Name" + " "*17+"| Description")#1,"No   |"+" "*9+"Name" + " "*9+"|"+ " "*35+"Description"

        body = self.display.text_box(3,24,5,115,bottom = "_")

        texts = ["     |"+" "*22+"|" for x in range(21)]

        addresses = list(self.__addresses.values())
        for line in range(len(addresses)):
            code = addresses[line].code
            name = addresses[line].get_name()
            desc = addresses[line].desc
            texts[line] = f"{code} | {name}"+" "*(21-len(name))+f"| {desc}"

        body.print([x for x in range(1,21)],*texts)

        code_entered = self.display.get_input("<Enter Code to Write Letter>").replace("0","")
        while not code_entered in self.__addresses.keys():
            code_entered = self.display.get_input("<INVALID INPUT> <Enter Code to Write Letter>").replace("0","")

        self.display.clear()
        return self.__addresses[code_entered]

    def add(self,address):
        address.code = str(self.__code).rjust(4,"0")
        self.__addresses[str(self.__code)] = address
        self.__code += 1
