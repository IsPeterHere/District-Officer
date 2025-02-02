#import Terminal_py
import Terminal_py

from time import sleep
import random 






# set up terminal window   
T = Terminal_py.Terminal()

#make a text box
#4 mandatory parameters are start line, end line, start column, end column
#opptionaly border charcters can be added to the top, left, right and bottom
my_text = T.text_box(10,20,10,90,left = "|",right = "|")

#change text of text box
my_text.text = "Hello World"





#example of live program
while True:
    sleep(2)
    my_text.text = "a number: "+str(random.randint(0,100))
