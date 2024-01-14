import json
import time
import Weather


api_key = "204839194a9bab1305b974d5136e6660"

print("Welcome To WeatherWithYou :)")
print("1.Want to know Weather of a city")
print("2.Want to know Past Weather")

while True:
  try:
    choice = int(input("Enter your choice(1/2): "))
    if choice == 1 or choice == 2:
      break
    else:
      print("Choose 1 or 2")
  except Exception:
    print("Invalid Choice")
    

if choice == 1:
  Weather.weather.weatherforecast()
else:   Weather.weather.history_weatherforecast()
 
