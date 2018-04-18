#Alle funktioner

#library
import urllib.request
from datetime import date
import json


#vejr-prognose
def weather(key,latitude,longtitude):
	forecast = urllib.request.urlopen("https://api.darksky.net/forecast/"+key+"/"+latitude+","+longtitude).read()
	parsed_forecast = json.loads(forecast)
	forecast_list = []
	weekday = date.today()
	forecast_list.append(date.strftime(weekday, "%A")+": "+parsed_forecast["daily"]["summary"]+'\n---')
	for x in range(0,6):
		forecast_list.append(parsed_forecast["daily"]["data"][x]["summary"])

	return forecast_list

#