
import asyncio
from ollama import AsyncClient
class M:
    def __init__(self):
        self.response = None
    async def chat(self):
      message = {'role': 'user', 'content': 'Why is the sky blue?'}
      self.response = await AsyncClient().chat(model='deepseek-r1:1.5b', messages=[message])

m = M()
m.chat()

asyncio.run(m.chat())
while m.response == None:
    print("yay")
print(m.response)

"""
response = ollama.chat(
    model='deepseek-r1:1.5b',
    messages=[
        {'role': 'system', 'content': "The user has written a letter to a person but before they send it there is something that must be determined. "},
        {'role': 'system', 'content': "Answer the user with a yes or a no depending on weather the contents of letter appear to be asking for details or requesting help. "},
        {'role': 'system', 'content': "Answer the user only with a 'yes' or a 'no'. "},
        {'role': 'user', 'content': 'letter:  hello, i am requesting further details. i also dont understand the game menu, tell me you love me.'}
    ]
)

# Print the response
print(response['message']['content'])

print(ollama.generate(model='deepseek-r1:1.5b', prompt='Why is the sky blue?',system="The user has written a letter to a person but before they send it there is something that must be determined.\nAnswer the user with a yes or a no depending on weather the contents of letter appear to be asking for details or requesting help.\nAnswer the user only with a 'yes' or a 'no'.",)["response"])"""