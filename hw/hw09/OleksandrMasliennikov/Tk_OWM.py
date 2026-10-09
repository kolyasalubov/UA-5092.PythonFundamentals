"""Tkinter app that shows the current weather for a city.

The OpenWeatherMap API key is read from the OWM_API_KEY environment variable.
"""

import os
import sys
import tkinter as tk

from pyowm import OWM
from pyowm.commons.exceptions import (
    APIRequestError,
    NotFoundError,
    UnauthorizedError,
)


API_KEY_ENV = 'OWM_API_KEY'

HEIGHT = 350
WIDTH = 450


def format_weather(weather) -> str:
    """Return a multi-line text description of a pyowm Weather object."""
    return (
        f"Weather: {weather.detailed_status}\n"
        f"Wind: {weather.wind()['speed']} m/s\n"
        f"Humidity: {weather.humidity}%\n"
        f"Temperature: {weather.temperature('celsius')['temp']} °C\n"
        f"Rain: {weather.rain}\n"
        f"Heat index: {weather.heat_index}\n"
        f"Clouds: {weather.clouds}%"
    )


class WeatherApp:
    """Main window: a city input field, a button and the weather output."""

    def __init__(self, root: tk.Tk, api_key: str) -> None:
        """Connect to OpenWeatherMap and build the window widgets."""
        self.root = root
        self.mgr = OWM(api_key).weather_manager()
        self._build_ui()

    def _build_ui(self) -> None:
        """Create and place all widgets."""
        self.root.title('Weather Application')

        canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        frame = tk.Frame(self.root, bg='deep sky blue', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,
                    anchor='n')

        self.entry_field = tk.Entry(frame, font=('Courier', 12))
        self.entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        button = tk.Button(frame,
                           text='Get Weather',
                           bg='gray', fg='white',
                           font=('Courier', 8),
                           command=self.get_weather)
        button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        lower_frame = tk.Frame(self.root, bg='gold', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                          relheight=0.6, anchor='n')

        self.label = tk.Label(lower_frame, font=('Courier', 14))
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)

    def get_weather(self) -> None:
        """Read the city from the input field and show its weather."""
        city = self.entry_field.get()
        try:
            weather = self.mgr.weather_at_place(city).weather
        except NotFoundError:
            text = 'No weather data for this city.'
        except UnauthorizedError:
            text = 'Invalid API key.'
        except APIRequestError:
            text = 'Weather service is unavailable.\nTry again later.'
        except Exception:
            text = 'Error getting weather data.'
        else:
            text = format_weather(weather)
        self.label.config(text=text)


def main() -> None:
    """Read the API key from the environment and start the app."""
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        sys.exit(f'Set the {API_KEY_ENV} environment variable '
                 'to your OpenWeatherMap API key.')

    root = tk.Tk()
    WeatherApp(root, api_key)
    root.mainloop()


if __name__ == '__main__':
    main()
