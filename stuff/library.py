#Alle funktioner

#library
import urllib.request
import json


#vejr-prognose
def weather(key,latitude,longtitude):
	forecast = urllib.request.urlopen("https://api.darksky.net/forecast/"+key+"/"+latitude+","+longtitude+"?exclude=[currently,minutely,alerts,flags]&lang=da").read()
	
	parsed_forecast = json.loads(forecast)

	print(parsed_forecast["hourly"])
	print("https://api.darksky.net/forecast/"+key+"/"+latitude+","+longtitude+"?exclude=[currently,minutely,alerts,flags]&lang=da")



weather("97bca87e978b87f27efdcf3fa67dae96","57.048","9.935")

