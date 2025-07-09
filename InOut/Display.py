from Post.Adressing import Address_book
from Post.Letter import Letter

      
class Display:
    
    def __init__(self,in_Out):
        self.in_Out = in_Out

    def __call__(self, object_or_tag, question = None ,**flags):
        match (object_or_tag):
            case "Start":
                self.in_Out.OUT_start_up()

            case Letter():
                self.OUT_show_letter(object_or_tag,flags.get('type',False),flags.get('address',True),flags.get('signature',True))

            case Address_book():
                self.OUT_show_address_book(object_or_tag,flags.get('type',False))
                
            case _:
                raise RuntimeError("Unrocognised Object/Tag For Display")
        
        if question != None:
            match (question):
                
                case ("Press Enter"):
                    user_input = self.in_Out.IN_Press_Enter()
                case ("Text Entry"):
                    user_input = self.in_Out.IN_Text_Entry()
                case ("Letter"):
                    user_input = self.in_Out.IN_Letter()
                case ("Address Book"):
                    user_input = self.in_Out.IN_Address_Book()
                    
            return user_input
        
