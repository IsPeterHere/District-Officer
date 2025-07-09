from People.General_secretariat import General_secretariat
from People.You import You

from District.District import District
from InOut.Display import Display
from InOut.TerminalInOut import In_Out
from datetime import date, timedelta

class Date:

    def __init__(self,year,month,day):
        self.__date = date(year,month,day)

    def next_day(self):
        self.__date = self.__date + timedelta(days = 1)

    def __call__(self):
        return self.__date

class People:

    def __init__(self):
        self.__people = []

    def add(self,person):
        self.__people.append(person)

    def get_all(self):
        return self.__people

    def read_and_reply(self):
        for person in self.__people:
            person.proccess_inbox()

class Data:

    def __init__(self):
        self.people = People()
        self.the_date = None
        self.district = None

        self.player_signature = ""


class Instance:

    year = 1924
    month = 1
    day = 1
    size = 10

    def __init__(self):
        self.display = Display(In_Out())
        self.data = Data()

        self.data.the_date = Date(self.year, self.month, self.day)
        self.data.district = District(self.size)
        self.general_secretariat = General_secretariat(self)
        self.you = You(self)

    def next_day(self):
            self.data.the_date.next_day()
            self.data.district.next_day()
            self.data.people.read_and_reply()

