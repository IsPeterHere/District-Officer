from datetime import date, timedelta

class Date:

    def __init__(self,year,month,day):
        self.__date = date(year,month,day)

    def next_day(self):
        self.__date = self.__date + timedelta(days = 1)

    def __call__(self):
        return self.__date