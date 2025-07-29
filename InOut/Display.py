from Post.Adressing import Address_book
from Post.Letter import Letter

      
class Display:
    
    def __init__(self,in_Out):
        self.in_Out = in_Out

    def NOTE_invalid_input(self):
        self.in_Out.NOTE_invalid_input()
        
    def __call__(self, object_or_tag, question_tag ,**flags):
        match (object_or_tag):
            case ("Debug"):
                self.in_Out.OUT_show_debug()
            case "Start":
                self.in_Out.OUT_start_up()
            case "Attachments":
                    self.in_Out.OUT_Attachments_list(flags["attachments"])
            case Letter():
                self.in_Out.OUT_show_letter(object_or_tag,flags.get('type',False),flags.get('address',True),flags.get('signature',True))
            case Address_book():
                self.in_Out.OUT_show_address_book(object_or_tag,flags.get('type',False))
            case _:
                raise RuntimeError("Unrocognised Object/Tag For Display")
        
        match (question_tag):
            case ("Press Enter"):
                user_input = self.in_Out.IN_Press_Enter()
            case ("Text Entry"):
                user_input = self.in_Out.IN_Text_Entry(flags.get('prompt',"<Type Input>"))
            case ("Write Letter"):
                user_input = self.in_Out.IN_Write_Letter(flags["send"],flags["exit"],flags["scroll"],flags["select"])
            case ("Read Letter"):
                user_input = self.in_Out.IN_Read_Letter(flags["exit"],flags["attachments"])
            case ("Attachments"):
                user_input = self.in_Out.IN_Attachments_list()
            case ("Address Book"):
                user_input = self.in_Out.IN_Address_Book(flags["read"],flags["write"],flags["day"])
            case None:
                user_input = None
            case _:
                raise RuntimeError("Unrocognised Question Tag")
                
        return user_input
    
