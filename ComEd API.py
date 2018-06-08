# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:23:33 2018

@author: Ryan
"""

import requests
import time

hourly_api = "https://hourlypricing.comed.com/api?type=currenthouraverage"
five_min_api = "https://hourlypricing.comed.com/api?type=5minutefeed"

hourly_api_response = requests.get(hourly_api)
five_min_api_response = requests.get(five_min_api)

five_min_price = five_min_api_response.json()[0]['price'] #The current five minute price
five_min_time = five_min_api_response.json()[0]['millisUTC'] #The current five minute time
five_min_time = int(five_min_time)/1000 #To get the Millis time to a workable format
my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(five_min_time)) #To further get the millis time readable
#print("The current five minute price is: " + five_min_price + " cents per kw/h.")

#one_hour_price = hourly_api_response.json()[0]['price'] #The current, or realtime price
#one_hour_time = hourly_api_response.json()[0]['millisUTC']
#print("The current one hour price is: " + one_hour_price + " cents per kw/h.")

counter = 0
my_price = 0

def get_time():
    cur_time = (time.strftime('%I:%M'))
    #cur_time = int(cur_time)
    return cur_time

#Gets the minute right now.
def get_minutes():
    minutes = (time.strftime('%M'))
    minutes = int(minutes)
    return minutes
    #print(minutes)

#Determines how many increments of 5 have passed this hour.
def how_many_fives():
    y = 0
    for x in range(1,get_minutes()):
        if x%5 == 0:
            y = y + 1
    return y
    #print(y)

for x in range(0,how_many_fives()):
    agg_price = five_min_api_response.json()[x]['price']
    agg_price = float(agg_price)
    my_price = my_price + agg_price
    #print(agg_price)
x = x + 1

my_price = my_price/x
my_price = round(my_price,1)
time_now = get_time()

print("The current hour average price at " +  str(time_now) + " is: " + str(my_price))




''''
NOTES AND OTHER UNUSED STUFF

#def main():
#    time_translator(five_min_time)    
#    print(my_time)

#print(api_1.text) #To print all the data in the API
#print(api_1.headers) #To access and view a server’s response headers

#print(hourly_api_response.text)

#Determines whether the current minute is divisible by 5. Helpful because ComEd updates every 5 mins.
#def divide_by_five():
#    if get_minutes()%5 == 0:
#        fives = True
        #x = x + 1
        #return x
#    else:
#        fives = False
#    return fives



'''
