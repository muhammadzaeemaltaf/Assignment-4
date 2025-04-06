import requests

from pprint import pprint

API_KEY = "PASTE_YOUR_API_HERE"

city = input("Enter the city name: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"

pprint(base_url)
response = requests.get(base_url).json()

pprint(response)