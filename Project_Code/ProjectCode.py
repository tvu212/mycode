#!/usr/bin/env python3




##imported libraries##
import requests
import pandas as pd
import json


##declared variables##
city = "seattle"
api_key = "ab4f8a1a1bce3082d408c58e4a6586ca"






## returns the data from api json file.
def get_data(response):

    temp = response['main']['temp']
    condition = response['weather'][0]["main"]

    print("test works" , temp , condition)


## Sends a get request to the api and returns a json
def get_json(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"  ##PARAMS == CITY, API_KEY, UNITS


    response = requests.get(url).json()    ## returns a dict
    weatherdata = json.dumps(response, indent=4) ## returns data in readable format str


    return response
  

    




def main():
    response = get_json(city, api_key)
    get_data(response)
    


if __name__ == '__main__':
    main()







##response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=seattle&appid=ab4f8a1a1bce3082d408c58e4a6586ca")
##print(response.status_code)
##print(response.json())
##weather = response.json()
##print(weather)
