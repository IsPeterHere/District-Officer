
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


class Address_book:

    def __init__(self,instance):
        self.instance = instance
        self.the_date = self.instance.data.the_date
        self.you = self.instance.you
        self.__addresses = dict()

        self.__code = 1

    def get_Addresses(self):
        return self.__addresses.copy()

    def get_Address(self,No):
        return self.__addresses[No]

    def open_book(self,
                  write = True,
                  read = True,
                  day = True,
                  typed = False):
        
        
        if not self.instance.you.get_inbox(self.instance.data.the_date()):
            read = False

        entered = self.instance.display(self,"Address Book",write = write,day=day,read=read,type = typed).replace("0","").lower()
        while not (((entered in self.__addresses.keys()) and write) or not (entered == "o" and read) or not (entered == "d" and day)):
            self.instance.display.NOTE_invalid_input()
            entered = self.instance.display(self,"Address Book",write = write,day=day,read=read,type = typed).replace("0","").replace("0","").lower()

        return entered

    def add(self,address):
        address.code = str(self.__code).rjust(4,"0")
        self.__addresses[str(self.__code)] = address
        self.__code += 1
