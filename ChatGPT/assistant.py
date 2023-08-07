''' Flet OpenAI code '''
import openai

openai.api_key = str(open("token.txt").read())

class SmartFenris():
    def __init__(self):
        self.messages = [
            {"role":"system", "content":"You are a helpful assistant."}
        ]
 
    def SmartFenrisResponse(self, user_text):
        self.user_text = user_text
        
        while True:
            
            # storing the user question in the message list
            self.messages.append({"role":"user", "content":self.user_text})
            
            # getting the response foem the OpenAI API
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = self.messages
            )

            # appending the generated response so that the AI remembers the past responses
            self.messages.append({"role":"assistant", "content":str(response['choices'][0]['message']['content'])})
            
            # returning the response
            return response['choices'][0]['message']['content']