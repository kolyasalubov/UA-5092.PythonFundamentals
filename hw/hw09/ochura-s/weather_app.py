"""Task 3. A weather application: a tkinter window plus the OpenWeatherMap API.

The user types the name of a city ("London" or "London,GB"), presses
"Get Weather" or Enter, and the application shows the current weather
received from OpenWeatherMap through the pyowm library.
"""

import os
import tkinter as tk

from pyowm import OWM
from pyowm.commons.exceptions import (APIRequestError, NotFoundError,
                                      TimeoutError, UnauthorizedError)

# The free key from the task; it can be replaced with your own one
# through the OWM_API_KEY environment variable.
API_KEY = os.environ.get("OWM_API_KEY", "ef2206ff5da67de63306d0b143e20872")

HEIGHT = 350
WIDTH = 450


def format_weather(place: str, weather) -> str:
    """Build the text with the current weather for the given place."""
    temperature = weather.temperature("celsius")
    wind = weather.wind()

    return (
        f"{place}\n\n"
        f"{weather.detailed_status.capitalize()}\n"
        f"Temperature: {temperature['temp']:.1f} C\n"
        f"(from {temperature['temp_min']:.1f} to {temperature['temp_max']:.1f})\n"
        f"Feels like: {temperature['feels_like']:.1f} C\n"
        f"Humidity: {weather.humidity} %\n"
        f"Wind: {wind['speed']} m/s\n"
        f"Clouds: {weather.clouds} %"
    )


def get_weather(weather_manager, city: str) -> str:
    """Return the weather report for the city or a message about the problem."""
    city = city.strip()

    if not city:
        return "Enter the name of a city."

    try:
        observation = weather_manager.weather_at_place(city)
    except NotFoundError:
        return f"City '{city}' was not found."
    except UnauthorizedError:
        return "The API key is invalid or has expired."
    except (APIRequestError, TimeoutError):
        return "No connection to the weather service."

    place = observation.location.name
    country = observation.location.country

    return format_weather(f"{place}, {country}", observation.weather)


def show_weather(weather_manager, entry_field: tk.Entry, label: tk.Label) -> None:
    """Read the city from the entry field and print the result in the label."""
    label["text"] = "Loading..."
    label.update_idletasks()
    label["text"] = get_weather(weather_manager, entry_field.get())


def build_window(weather_manager) -> tk.Tk:
    """Create the application window with all its widgets."""
    root = tk.Tk()
    root.title("Weather Application")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    entry_field = tk.Entry(frame, font=("Courier", 12))
    entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
    entry_field.focus()

    lower_frame = tk.Frame(root, bg="gold", bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

    label = tk.Label(lower_frame, font=("Courier", 12), justify="left")
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    button = tk.Button(frame,
                       text="Get Weather",
                       bg="gray", fg="white",
                       font=("Courier", 8),
                       command=lambda: show_weather(weather_manager,
                                                    entry_field, label))
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    # The Enter key works the same way as the button.
    entry_field.bind("<Return>",
                     lambda event: show_weather(weather_manager, entry_field, label))

    return root


def main() -> None:
    """Connect to OpenWeatherMap and run the application."""
    weather_manager = OWM(API_KEY).weather_manager()
    build_window(weather_manager).mainloop()


if __name__ == "__main__":
    main()
