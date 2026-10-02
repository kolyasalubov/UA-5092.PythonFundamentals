import logging
import tkinter as tk

from pyowm import OWM
from pyowm.commons.exceptions import (
    NotFoundError,
    UnauthorizedError,
    APIRequestError,
    TimeoutError,
    ParseAPIResponseError
)

from empty_city_field_error import EmptyCityFieldError


HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
logging.basicConfig(
    level=logging.INFO,
    format="%(process)d - %(levelname)s - %(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("weather.log", mode="w"),
        logging.StreamHandler()
    ]
)


def get_weather(city: str) -> None:
    """Get and display weather information for the specified city.

        Args:
            city: The name of the city to get weather information for.
    """
    try:
        city = city.strip()

        if not city:
            raise EmptyCityFieldError("City field cannot be empty")

        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        temperature = observation.weather.temperature('celsius')
        weather_info = (
                f"Weather: {observation.weather.detailed_status}\n"
                f"Wind: {observation.weather.wind()['speed']} m/s\n"
                f"Humidity: {observation.weather.humidity}%\n"
                f"Temperature: {temperature['temp']} °C\n"
                f"Max temperature: {temperature['temp_max']} °C\n"
                f"Min temperature: {temperature['temp_min']} °C\n"
                f"Feels like: {temperature['feels_like']} °C\n"
                f"Rain: {observation.weather.rain}\n"
                f"Heat index: {observation.weather.heat_index}\n"
                f"Clouds: {observation.weather.clouds}%"
            )
        status.config(text=weather_info)
    except EmptyCityFieldError as error:
        logging.error(str(error))
        status.config(text=str(error))
    except NotFoundError:
        logging.error("City not found: %s", city)
        status.config(text="City not found")
    except UnauthorizedError:
        logging.error("Invalid API key or insufficient permissions")
        status.config(text="Invalid API key or insufficient permissions")
    except TimeoutError:
        logging.error("Request timed out")
        status.config(text="Request timed out")
    except APIRequestError:
        logging.error("Connection error")
        status.config(text="Connection error")
    except ParseAPIResponseError:
        logging.error("Could not process weather data")
        status.config(text="Could not process weather data")
    except Exception as error:
        logging.exception("Unexpected error: %s", error)
        status.config(text=f"Unexpected error: {error}")
    else:
        logging.info("Weather successfully received for city: %s", city)


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


status = tk.Label(lower_frame, font=('Courier', 14))
status.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

