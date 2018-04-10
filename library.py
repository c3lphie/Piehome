#Alle funktioner

#library
import urllib.request
import json


#vejr-prognose
def weather():
	forecast = urllib.request.urlopen("https://api.darksky.net/forecast/97bca87e978b87f27efdcf3fa67dae96/57.0467,9.9359?exclude=[currently,minutely,alerts,flags]&lang=da&units=si").read()
	
	parsed_forecast = json.loads(forecast)

	print(parsed_forecast["hourly"])



weather()