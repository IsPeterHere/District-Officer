from root import Root


class Address:

    def __init__(self,person,line1,line2,desc = "",name = None,signature = None):
        self.person = person

        self.code = None
        self.line1 = line1
        self.line2 = line2
        self.desc = desc
        self.__name = name
        self.__signature = signature

    def get_name(self):
        if self.__name == None:
            return self.line1
        return self.__name

    def get_sign(self):
        if self.__signature == None:
            return "INS. "+self.get_name()
        else:
            return self.__signature

    def set_sign(self,signature):
        self.__signature = signature


class Address_book(Root):

    def __init__(self,display,you):
        self.display = display
        self.the_date = self.data.the_date
        self.you = you
        self.__addresses = dict()

        self.__code = 1

    def get_Addresses(self):
        return self.__addresses.copy()

    def get_Address(self,No):
        return self.__addresses[No]

    def open_book(self,
                  type_date = False,
                  accept_codes = True,
                  other_accepted_inputs = [],
                  prompt = "<Enter a code to Write Letter>              <Enter 'open' to read next letter in inbox> \n<Enter 'day' to finsh the day>"):

        entered = self.display(self,prompt,type = type_date).replace("0","").lower()
        while not (((entered in self.__addresses.keys()) and accept_codes) or (entered in other_accepted_inputs)):
            entered = self.display(self,prompt+"         <INVALID INPUT>").replace("0","").lower()

        self.display.clear()
        return entered

    def add(self,address):
        address.code = str(self.__code).rjust(4,"0")
        self.__addresses[str(self.__code)] = address
        self.__code += 1
