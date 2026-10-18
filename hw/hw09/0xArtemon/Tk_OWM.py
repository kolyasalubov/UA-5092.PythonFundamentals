import os
import tkinter as tk
from pyowm import OWM
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OWM_API_KEY')

if not API_KEY:
    raise ValueError("Error: API_KEY not found in the .env file!")

HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(location, label):
    location = location.strip()
    if not location:
        label['text'] = "Error: Please enter a city name."
        return

    try:
        observation = mgr.weather_at_place(location)
        w = observation.weather

        location_name = observation.location.name
        country = observation.location.country

        label['text'] = (
            f"Location: {location_name}, {country}\n"
            f"Status: {w.detailed_status}\n"
            f"Temperature: {w.temperature('celsius')['temp']}°C\n"
            f"Wind: {w.wind()['speed']} m/s\n"
            f"Clouds: {w.clouds}%"
        )           
    except Exception as e:
        label['text'] = f"Error: {e}"             

def main():
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
                    command=lambda: get_weather(entry_field.get(), label))
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Courier', 14), wraplength=310)
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
