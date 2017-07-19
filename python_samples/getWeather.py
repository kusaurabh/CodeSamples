#!/usr/bin/python

from xml.etree import ElementTree
import httplib2

#Uses GLobal Weather Service @ http://www.webservicex.com

def getWeatherForCity(cityName, country):
    client = httplib2.Http(".cache")
    URI = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=59b8a764b7789f3cf657105a83581ca3'
    response, jsonStr = client.request(URI)
    print(jsonStr)
    print(response)

if __name__ == "__main__":
    getWeatherForCity('Bangalore', 'India')
