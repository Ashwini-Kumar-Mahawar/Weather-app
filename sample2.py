import tkinter as tk
from tkinter import messagebox
import requests

Api_key = "5a9d9b0f8f85a58fb9a3a522dd12982c"

def fetch_weather(city):
  weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric")

  if weather_data.json()["cod"] == 200:
        city_name = weather_data.json()["name"]
        weather = weather_data.json()["weather"][0]["description"]
        clouds = weather_data.json()["clouds"]["all"]
        coord = weather_data.json()["coord"]["lon"]
        sys = weather_data.json()["sys"]["country"]
        temperature = weather_data.json()["main"]["temp"]
        humidity = weather_data.json()["main"]["humidity"]
        wind_speed = weather_data.json()["wind"]["speed"]

        weather_info = f"City: {city_name}\nWeather: {weather}\nClouds:{clouds}\ncoord: {coord}\nSys: {sys}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        messagebox.showinfo("Weather Details", weather_info)
  else:
        messagebox.showerror("Error", "City not found.")

def weather_information():
    city = city_entry.get()
    fetch_weather(city)

root = tk.Tk()
root.title("Tkinter Weather Application")


city_label = tk.Label(root, text="Enter city:")
city_label.grid(row=0, column=0, padx=50, pady=50)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=50, pady=50)

weather_information_button = tk.Button(root, text="Show Weather Information", command=weather_information)
weather_information_button.grid(row=1, column=0, columnspan=2, padx=50, pady=50)


root.mainloop()