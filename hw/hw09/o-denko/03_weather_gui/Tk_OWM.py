import tkinter as tk

from OWM import get_weather_report, API_KEY, NotFoundError

HEIGHT = 350
WIDTH = 450


def get_weather() -> None:
    """
    Fetch weather data for the specified city and update the UI.
    """
    if not API_KEY:
        label.config(text="Error: OWM_API_KEY not found in .env file")
        return

    city = entry_field.get().strip()
    if not city:
        label.config(text="Error: City name cannot be empty.")
        return

    try:
        report = get_weather_report(city, API_KEY)
        label.config(text=report)
    except NotFoundError:
        label.config(text=f"Error:\nCity '{city}' not found.\nPlease verify the name.")
    except Exception as e:
        label.config(text=f"Unexpected error:\n{e}")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.bind('<Return>', lambda event: get_weather())

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="black",
    font=('Courier', 8),
    command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 8), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
