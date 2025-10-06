import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your own OpenWeather API key
API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info.set(
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Weather: {weather_desc.title()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch weather data.\n{e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=5)

weather_info = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_info, justify="left")
weather_label.pack(pady=10)

root.mainloop()
