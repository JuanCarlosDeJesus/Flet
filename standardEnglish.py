''' install openai = pip3 install openai '''
import openai 

# we will be using dotenv, .env and .gitignore to hide the openai api key
openai.api_key = str(open("token.txt").read())


