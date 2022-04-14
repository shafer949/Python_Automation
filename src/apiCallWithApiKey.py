import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

#Install pip install python-dotenv

#Build the url with the correct parameters
baseUrl = 'https://api.giphy.com/v1/gifs/random'
api_key = os.getenv("API_KEY")
parameters = {
    'api_key': api_key,
    'rating': 'g'
} 

#Get all response
response = requests.get(baseUrl, params=parameters)

#Handle the response
content = response.content
info = json.loads(content)
print(type(info))
print(info)

#cd into the src directory then
#Run py apiKey.py in the terminal (Windows)