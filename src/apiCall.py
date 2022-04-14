import requests
import json

#Build the url with the correct parameters
baseUrl = 'http://www.boredapi.com/api/activity/'

#Get responses without using parameters
response = requests.get(baseUrl)

#Handle the response
content = response.content
info = json.loads(content)

#Check the type of the data
print(type(info))
#Check that data is returned
print(info)

#Get different attributes of the data
activity = info['activity']
type = info['type']
participantCount = info['participants']

#Print different attributes of the data
print('Activity 1:',activity)
print('Type 1:',type)
print('Participant Count 1:',participantCount)

#########################################################

#Dictionary with key/value pairs of parameter(s)
parameters = {
    'participants': 5
} 

#Get responses based on parameter(s)
response2 = requests.get(baseUrl, params=parameters)

#Handle the response
content2 = response2.content
info2 = json.loads(content2)

#Get different attributes of the data
activity2 = info2['activity']
type2 = info2['type']
participantCount2 = info2['participants']

#Print different attributes of the data
print('Activity 2:', activity2)
print('Type 2:', type2)
print('Participant Count 2:', participantCount2)

#Run py apiCall.py in the terminal (Windows)