import tkinter as tk
from pyowm import OWM
from pyowm.commons.exceptions import (
    NotFoundError,
    PyOWMError,
    UnauthorizedError,
)

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather() -> None:
    """
    Fetch weather for the entered city and display it in the window
    """
    city = entry_field.get().strip()

    if not city:
        label.config(text="Введіть назву міста.")
        return

    try:
        observation = mgr.weather_at_place(city)
        weather = observation.weather

        temperature = weather.temperature("celsius")["temp"]
        wind_speed = weather.wind()["speed"]

        result = (
            f"Місто: {city}\n"
            f"Погода: {weather.detailed_status}\n"
            f"Температура: {temperature:.1f} °C\n"
            f"Вологість: {weather.humidity}%\n"
            f"Вітер: {wind_speed} м/с"
        )
        label.config(text=result)

    except NotFoundError:
        label.config(text="Місто не знайдено.")
    except UnauthorizedError:
        label.config(text="Перевірте ваш API-ключ.")
    except PyOWMError:
        label.config(text="Не вдалося отримати погоду.\nСпробуйте пізніше.")


root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.85,
    relheight=0.1,
    anchor="n",
)

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 8),
    command=get_weather,
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(
    relx=0.5,
    rely=0.25,
    relwidth=0.85,
    relheight=0.6,
    anchor="n",
)

label = tk.Label(
    lower_frame,
    text="Введіть місто",
    font=("Courier", 12),
    wraplength=350,
)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


if __name__ == "__main__":
    root.mainloop()
