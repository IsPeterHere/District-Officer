
import ollama

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