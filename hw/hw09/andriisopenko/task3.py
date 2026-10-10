import os
import tkinter as tk
from pyowm import OWM
HEIGHT = 350
WIDTH = 450

def get_weather():
    """Get and display weather information for the entered city."""
    city = entry_field.get().strip()
    if not city:
        label.config(text="Please enter a city name.")
        return
    api_key = os.getenv("OWM_API_KEY")

    if not api_key:
        label.config(text="OpenWeatherMap API key is missing.")
        return
    try:
        owm = OWM(api_key)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temperature = weather.temperature("celsius")["temp"]
        status = weather.detailed_status
        humidity = weather.humidity
        wind = weather.wind()["speed"]
        clouds = weather.clouds
        rain = weather.rain
        weather_info = (
            f"City: {city}\n"
            f"Temperature: {temperature} °C\n"
            f"Status: {status}\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind} m/s\n"
            f"Clouds: {clouds}%\n"
            f"Rain: {rain}"
        )
        label.config(text=weather_info)
    except Exception as error:
        label.config(text=f"Error getting weather:\n{error}")

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(
    relx=0.5, rely=0.1,
    relwidth=0.75, relheight=0.1,
    anchor="n"
)
entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 8),
    command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(
    relx=0.5, rely=0.25,
    relwidth=0.75, relheight=0.6,
    anchor="n"
)
label = tk.Label(
    lower_frame,
    font=("Courier", 11),
    justify="left",
    anchor="nw",
    wraplength=300
)
label.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()