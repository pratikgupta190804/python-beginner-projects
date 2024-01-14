from geopy.geocoders import Nominatim
import datetime
import requests


api_key = "204839194a9bab1305b974d5136e6660"

class weather:
  def history_weatherforecast():
    try:
      city = input("Enter city name: ")
      year = input ("Enter year: ")
      month = input("Enter month: ")
      date = input("Enter date: ")
      loc = Nominatim(user_agent="getlocation")
      getLoc = loc.geocode(city)
      dt = datetime.datetime(int(year), int(month), int(date))
      dt = int(dt.timestamp())
      url = f"https://api.openweathermap.org/data/2.5/weather?lat={getLoc.latitude}&lon={getLoc.longitude}&dt={dt}&appid={api_key}"
       
      response = requests.get(url).json()
      temp = response["main"]["temp"]
      temp = round(temp - 273.15, 2)
      temp = str(temp) + "°C"
  
      feels = response["main"]["feels_like"]
      feels = round(feels - 273.15, 2)
      feels = str(feels) + "°C"
  
      weather_desc = response["weather"][0]["description"]
  
      wind_speed = response["wind"]["speed"]
  
      humidity = response["main"]["humidity"]
  
      pressure = response["main"]["pressure"]
      pressure = round(pressure * 0.0295, 2)
      print("--------------------------")
      print("Temperature: ", temp)
      print("Feels Like: ", feels)
      print("Weather Description: ", weather_desc)
      print("Wind Speed: ", wind_speed,"m/s")
      print("Humidity: ", humidity)
      print("Pressure: ", pressure,"hg")
    except:
      print("Invalid City")
    
  def weatherforecast():
    city_name = input("Enter city name: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url).json()

    temp = response["main"]["temp"]
    temp = round(temp - 273.15, 2)
    temp = str(temp) + "°C"

    feels = response["main"]["feels_like"]
    feels = round(feels - 273.15, 2)
    feels = str(feels) + "°C"

    weather_desc = response["weather"][0]["description"]

    wind_speed = response["wind"]["speed"]

    humidity = response["main"]["humidity"]

    pressure = response["main"]["pressure"]
    pressure = round(pressure * 0.0295, 2)
    print("--------------------------")
    print("Temperature: ", temp)
    print("Feels Like: ", feels)
    print("Weather Description: ", weather_desc)
    print("Wind Speed: ", wind_speed,"m/s")
    print("Humidity: ", humidity)
    print("Pressure: ", pressure,"hg")
    
