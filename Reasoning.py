import ollama
import asyncio
from ollama import AsyncClient

class Reasoning:

    model = 'deepseek-r1:1.5b'

    async def reason(self,questions = []):
        tasks = []
        async with asyncio.TaskGroup() as tg:
            for question in questions:
                match question["type"]:
                    case "binary":
                        tasks.append(tg.create_task(
                            self.binary_reason(question["question"],
                                               question.get("about",""))))

                    case "choice":
                        tasks.append(tg.create_task(
                            self.choice_reason(question["options"],
                                               question.get("about",""))))
                      
                    case _:
                        print("error unrecognized type: "+question["type"])

        for task in tasks:
            print(task.result())

    async def binary_reason(self,question,about):
        response = await AsyncClient().chat(
            model= self.model,
            messages=[
                {'role': 'system', 'content':f"Answer the user with a yes or a no depending on the question '{question}'\n"+"Answer the user only with a 'yes' or a 'no'. \n"},
                {'role': 'user', 'content': about}
            ])
        answer = response['message']['content']
        print(answer)
        answer = answer.split("</think>")[1].lower()
        if "yes" in answer:
            return True
        elif "no" in answer:
            return False
        else:
            print("error no binary response from model")

    async def choice_reason(self,options,about):
        response = await AsyncClient().chat(
            model= self.model,
            messages=[
                {'role': 'system', 'content':f"Answer the user with an A,B,C,... depending on which option best fits the letters contents '{options}'\n"+"Answer the user only with the corresponding characters (i.e 'A' and/or 'AB' and/or...). \n"},
                {'role': 'user', 'content':about}
            ])
        answer = response['message']['content']
        print(answer)
        answer = answer.split("</think>")[1].lower()
        if "A" in answer:
            return True
        elif "B" in answer:
            return False
        else:
            print("error no binary response from model")


if __name__ == "__main__":

    t =Reasoning()

    # asyncio.run( t.reason([{"type":"binary",
    #                         "question": " Are the contents of the letter polite? ",
    #                         "about":    "The letter's contents are as follows: hi sir, please help me?"},
    #                         ]))

    asyncio.run( t.reason([{"type":"choice",
                            "options": "A. The letter is asking for help doing something or with something\n B.The letter is asking for money/funding for something \n C.The letter is asking for sexual favors",
                            "about":    "The letter's contents are as follows: hi sir, please help me? also give me a blow job"},
                            ]))