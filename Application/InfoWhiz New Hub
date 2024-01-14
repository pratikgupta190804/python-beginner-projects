import requests
import json
import pycountry

api_key = "077d071b28eb4e8db8f317ad151952d8"

print("Welcome to InfoWhiz News Hub")
print("Please select the category you want to search\n1.Want to know news of any specific topic\n2.Want to know top headlines of any country")
while True:
  try:
    choice = int(input("Enter your choice(1/2): "))
    if choice == 1 or choice == 2:
      break
    else:
      print("Please enter 1 or 2")
    
  except Exception:
    print("Invalid choice. Enter a valid choice")

if choice == 1:
  topic = input("Enter the topic you want to search: ")
  url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
  response = requests.get(url)
  data = json.loads(response.text)
  articles = data["articles"]
  if data["articles"] != []:
    for article in articles:
      print("***********************")
      print("Title: ",article["title"])
      print("------------------------")
      print("Description: ",article["description"])
      print("------------------------")
      print("Author: ",article["author"])
      print("------------------------")
      print("More Info: ",article["url"])
      print("***********************")

  else:
    print(f"No articles found for article {topic}")

if choice == 2:
  while True:
    try:
      country_input = input("Enter the country you want to search: ")
      cc=pycountry.countries.search_fuzzy(country_input)[0].alpha_2
      break
    except Exception:
      print("Invalid Country Name")

  url_2= f"https://newsapi.org/v2/top-headlines?country={cc}&apiKey={api_key}"
  response = requests.get(url_2)
  data = json.loads(response.text)
  articles = data["articles"]
  if data["articles"] != []:
    for article in articles:
      print("***********************")
      print("Title: ",article["title"])
      print("------------------------")
      print("Description: ",article["description"])
      print("------------------------")
      print("Author: ",article["author"])
      print("------------------------")
      print("More Info: ",article["url"])
      print("***********************")

  else:
    print(f"No articles found for article {country_input}")
      
