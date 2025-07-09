from abc import ABC, abstractmethod

class ABSTRACT_IN_OUT(ABC):
    
    @abstractmethod
    def OUT_start_up(self):
        pass
    
    @abstractmethod
    def OUT_show_letter(self,letter,type_line1,show_address,show_signature):
        pass
    
    @abstractmethod
    def OUT_show_address_book(self,address_book,type_date):
        pass

    @abstractmethod
    def IN_Press_Enter(self):
        pass
    
    @abstractmethod
    def IN_Text_Entry(self,prompt):
        pass
    
    @abstractmethod
    def IN_Letter(self):
        pass
    
    @abstractmethod
    def IN_Address_Book(self):
        pass