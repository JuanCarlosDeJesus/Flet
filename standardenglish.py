''' install openai = pip3 install openai '''
import openai

# we will be using dotenv, .env and .gitignore to hide the openai api key
openai.api_key = str(open(f"/Users/macuser/Documents/Flet/token.txt").read())

class StandardEnglish():
    def __init__(self, text_to_convert):
        self.text_to_convert = text_to_convert
    
    def convertStandardEnglish(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt = f"Convert ungrammatical statements into standard English:\n{self.text_to_convert}",
            messages=[],
            temperature=0,
            max_tokens=256
        )
        
        result = {
            'id': response.id,
            'created': response.created,
            'model': response.model,
            'completion_tokens': response.usage.completion_tokens,
            'prompt_tokens': response.usage.prompt_tokens,
            'total_tokens': response.usage.total_tokens,
            'output': response.choices[0].text,
            'status': response.choices[0].finish_reason,
        }
        
        return result["output"]