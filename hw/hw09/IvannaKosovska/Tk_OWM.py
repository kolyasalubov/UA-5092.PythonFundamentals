import tkinter as tk
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

def get_weather(city, label):
    city = city.strip()
    if not city:
        label.config(text="Please enter a city name.")
        return
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        label.config(text=f"Temperature: {w.temperature('celsius').get('temp')}°C\n"
                     f"Status: {w.detailed_status}\n"
                     f"Clouds: {w.clouds}\n"
                     f"Wind Speed: {w.wind().get('speed')}\n"
                     f"Humidity: {w.humidity}")
    except NotFoundError:
        label.config(text="City not found.\nPlease enter a correct city name.")
    except Exception:
        label.config(text="Something went wrong. Please try again.")
   
def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title("Weather Application")
    canvas.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry_field = tk.Entry(frame, font=('Courier', 12))
    entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Courier', 14))
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    button = tk.Button(
        frame,
        text="Get Weather",
        bg="gray", fg="white",
        font=('Courier', 8),
        command=lambda: get_weather(entry_field.get(), label)
    )
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    root.mainloop()


if __name__ == '__main__':
    main()





