import tkinter as tk
from tkinter import font
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather(city: str) -> None:
    """Get and display weather information for the specified city.

    The function retrieves weather data using the OpenWeatherMap API
    and displays it in the application label.

    Args:
        city: The name of the city to get weather information for.

    Returns:
        None.
    """
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)

        weather_information = (
            f"Weather status:{observation.weather.status}\n"
            f"Detailed weather status: {observation.weather.detailed_status}\n"
            f"Wind: {observation.weather.wind()['speed']} m/s\n"
            f"Humidity: {observation.weather.humidity}%\n"
            f"Temperature: {observation.weather.temperature('celsius')['temp']} °C\n"
            f"Rain: {observation.weather.rain}\n"
            f"Heat index: {observation.weather.heat_index}\n"
            f"Clouds: {observation.weather.clouds}%"
                )
        label.config(text = weather_information)

    except  NotFoundError:
        label.config(text = "City not Found")

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
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

