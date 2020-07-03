import requests
import json 
import config
  
api_key = config.weather_api_key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_id = config.weather_city_id
units = "metric"

complete_url = base_url + "appid=" + api_key + "&id=" + city_id + "&units=" + units

def send_rain_alert(description):
    r = requests.post('https://maker.ifttt.com/trigger/rain_alert/with/key/' + config.ifttt_api_key, params={"value1":description,"value2":"none","value3":"none"})
    print('rain alert sent')

def send_low_temperature_alert(temperature):
    r = requests.post('https://maker.ifttt.com/trigger/temperature_alert/with/key/' + config.ifttt_api_key, params={"value1":temperature,"value2":"none","value3":"none"})
    print('temperature alert sent')

response = requests.get(complete_url) 
r_json = response.json() 
  
if r_json["cod"] != "404": 

    main = r_json["main"] 
    weather = r_json["weather"] 

    current_temperature = main["temp"] 
    weather_description = weather[0]["description"] 
    print(current_temperature)
    print(weather_description)

    if current_temperature < 5:
        send_low_temperature_alert(current_temperature)

    if weather_description.lower().find("rain") > -1:
        send_rain_alert(weather_description)