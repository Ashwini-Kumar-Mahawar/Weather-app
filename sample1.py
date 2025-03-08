import requests
import json
import win32com.client as wincom

city = input("Enter city name: \n")

url = f"http://api.weatherapi.com/v1/current.json?key=747744847f244457b2d104129242108&q={city}"

r = requests.get(url)
print(r.text)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]
s = weatherdic["current"]["wind_kph"]
h = weatherdic["current"]["humidity"]
speak = wincom.Dispatch("SAPI.SpVoice")

text = f"'the current weather in {city} is {w} degrees and wind speed is {s} kph or the humidity is {h} %'"
print(text)
speak.Speak(text)