#!/usr/bin/env python3


##imported libraries##
import requests
import csv
import json
import datetime


##declared variables##
city = "seattle"
api_key = "ab4f8a1a1bce3082d408c58e4a6586ca"
csvheader = ['TEMP','CONDITION','SUNSET TIME']




## returns the data from api json file.
def get_data(response):

    ##pulls any data from response.json that is specified
    temp = response['main']['temp']
    condition = response['weather'][0]["main"]



    ##time test calculations for later
    sunset = int(response["sys"]["sunset"])
    sunset_time  =  datetime.datetime.fromtimestamp(sunset)
    now = datetime.datetime.now()
    difference = sunset_time - now

    return [temp,condition,sunset_time]



    ##print("test works" , temp , condition ,test)
    print(difference.total_seconds() /60**2 )


## Sends a get request to the api and returns a json
def get_json(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"  ##PARAMS == CITY, API_KEY, UNITS
    response = requests.get(url).json()    ## returns a dict
    weatherdata = json.dumps(response, indent=4) ## returns data in readable format str
    return response
  

    
def main():
    response = get_json(city, api_key)
    data = get_data(response)
    with open('test.csv', 'a', encoding='UTF8', newline='') as f:

        writer = csv.writer(f)
        ##writer.writerow(csvheader)
        writer.writerow(data)
        f.close()
    


if __name__ == '__main__':
    main()







