class Value:

    MIN = 0
    MAX = 100

    def __init__(self,value):
        assert value > self.MIN and value < self.MAX, "Ensure value is in range"
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = max(min(value,self.MAX),self.MIN)