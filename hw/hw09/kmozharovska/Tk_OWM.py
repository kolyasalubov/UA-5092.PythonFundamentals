import tkinter as tk
from tkinter import font
from pyowm import OWM

"""
A GUI weather application that retrieves and displays
current weather information for
user-specified city using OpenWeatherMap API.
"""

API_KEY = '6aea334bac23426cd392a1379bae2809'
HEIGHT = 350
WIDTH = 450


def get_weather() -> None:
    """
    Get weather for the city entered by the user.
    Args: None
    Returns: None
    """
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    city = entry_field.get()

    try:
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        weather_text = (
            f"Weather: {weather.detailed_status}\n"
            f"Wind: {weather.wind()['speed']} m/s\n"
            f"Humidity: {weather.humidity}%\n"
            f"Temperature: {weather.temperature('celsius')['temp']} °C\n"
            f"Rain: {weather.rain}\n"
            f"Heat index: {weather.heat_index}\n"
            f"Clouds: {weather.clouds}%"
        )
        label.config(text=weather_text)

    except Exception:
        label.config(text="Could not find weather for this city.")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
