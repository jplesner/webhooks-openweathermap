# Overview
Create a custom trigger for IFTTT that can be used to trigger what you want!  

In this case, if it is going to rain or if the temperature is below 5 degrees then the webhook will be triggered.

I have this running on a Raspberry Pi Zero as a once a day cron job.  

# Prerequisites
Python3  
### Update in config file
https://openweathermap.org/api key  
IFTTT webhooks service API key  
IFTTT app that uses webhooks with 'temperature_alert' and 'rain_alert' events
