import requests

city = input("Enter the name of the city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
response = requests.get(url)
weather_data = response.json()
temp = weather_data['main']['temp']
description = weather_data['weather'][0]['description']
print(f"The temperature in {city} is {temp}K and the weather is {description}")
