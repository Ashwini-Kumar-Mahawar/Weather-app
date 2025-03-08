import tkinter as tk
from tkinter import messagebox
import requests
import win32com.client as wincom

# Use the API key from WeatherAPI
Api_key = "747744847f244457b2d104129242108"


def fetch_weather(city):
    # Fetch weather data from WeatherAPI
    url = f"http://api.weatherapi.com/v1/current.json?key={Api_key}&q={city}"
    weather_data = requests.get(url)

    if weather_data.status_code == 200:
        weatherdic = weather_data.json()
        city_name = weatherdic["location"]["name"]
        country = weatherdic["location"]["country"]
        temperature = weatherdic["current"]["temp_c"]
        humidity = weatherdic["current"]["humidity"]
        wind_speed = weatherdic["current"]["wind_kph"]
        weather = weatherdic["current"]["condition"]["text"]

        # Display the weather info in a messagebox
        weather_info = f"City: {city_name}\nCountry: {country}\nWeather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} kph"
        messagebox.showinfo("Weather Details", weather_info)

        # Prepare text-to-speech content
        speak_text = f"The current weather in {city_name}, {country}, is {weather}. The temperature is {temperature} degrees Celsius, with a humidity of {humidity} percent, and wind speed of {wind_speed} kilometers per hour."

        # Initialize text-to-speech engine
        speak = wincom.Dispatch("SAPI.SpVoice")
        print(speak_text)
        speak.Speak(speak_text)

    else:
        messagebox.showerror("Error", "City not found or invalid request.")


def weather_information():
    city = city_entry.get()
    fetch_weather(city)


# GUI setup
root = tk.Tk()
root.title("Tkinter Weather Application")

city_label = tk.Label(root, text="Enter city:")
city_label.grid(row=0, column=0, padx=50, pady=50)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=50, pady=50)

weather_information_button = tk.Button(root, text="Show Weather Information", command=weather_information)
weather_information_button.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

root.mainloop()
