#!/usr/bin/env python3


##imported libraries##
import requests
import csv
import json
import datetime
import os
import smtplib





##declared variables##
city = "seattle"
api_key = "ab4f8a1a1bce3082d408c58e4a6586ca"
csvheader = ['TEMP','CONDITION','CURRENT TIME']
os.chdir('/home/student/mycode/Project_Code/')




##DATASET INDEX VARIABLES##

TEMPERATURE = 0
CONDITION = 1
SUNSET_TIME = 3




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

    return [temp,condition,now]



    ##print("test works" , temp , condition ,test)
    print(difference.total_seconds() /60**2 )


## Sends a get request to the api and returns a json
def get_json(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"  ##PARAMS == CITY, API_KEY, UNITS
    response = requests.get(url).json()    ## returns a dict
    weatherdata = json.dumps(response, indent=4) ## returns data in readable format str
    return response



def temp_check(data, output_file):
    if data[TEMPERATURE] < 32.00:
        output_file.write(f"It is a freezing {data[0]} degrees out there!\n")
    if data[TEMPERATURE] > 100.00:
        output_file.write(f"Holy shit its {data[0]} degrees outside!! Remember to hydrate!\n")
    else:
        output_file.write(f"Not too hot not too cold right now\n")



def rain_check(data, output_file):
    if data[CONDITION] == 'Rain':
        output_file.write("Its raining bring a coat!\n")
    else:
        output_file.write("Looks pretty clear out there!\n")
    
def main():


    response = get_json(city, api_key)
    data = get_data(response)


    with open('test.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        ##writer.writerow(csvheader)
        writer.writerow(data)
        


    with open ('output_file.txt', 'w', encoding='UTF8', newline='') as output_file:
        temp_check(data,output_file)
        rain_check(data,output_file)

    


if __name__ == '__main__':
    main()







