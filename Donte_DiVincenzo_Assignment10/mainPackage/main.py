#main.py

# Name: Donte DiVincenzo
# email: jain2ss@mail.uc.edi , shiverld@mail.uc.edu, rootepr@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: In this project, we  researched an API, built a URL with a data request and submitted it to the server. Then received the results from the server. Then we 
#put the results into a python dictionary and extracted data from the dictionary and printed it to the console 
# Citations: https://api.nasa.gov/planetary/apod?api_key=REJuLqvuWm1chdtWJdWO69oZKGgkebY6GsrCsBSr
# Anything else that's relevant:


import json
import requests
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=REJuLqvuWm1chdtWJdWO69oZKGgkebY6GsrCsBSr')
json_string = response.content
parsed_json = json.loads(json_string) # Now we have a python dictionary


x = parsed_json['explanation']

print("Interesting Information: ",x)