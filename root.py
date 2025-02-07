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


class Root:
    data = Data()