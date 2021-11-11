#Import modules needed

import requests 
import json

# Getting new api from https://newsapi.org/
# we will create account and take API key by clicking on get API button.

r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=ce3ad53db2784eff9db2b57ec6e7b7b3')
#r  #page not found = 404 ,for page found= 200
# r.content
#it appers the data as same as in news api
data = json.loads(r.content)
#data

# Reading And showing news
from win32com.client import Dispatch
print("Top 10 Today News")
for i in range(10):
    News = data['articles'][i]['title']
    print("News number",i+1,":",News)
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(News)
