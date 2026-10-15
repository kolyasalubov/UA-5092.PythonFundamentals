import os
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")


def get_weather_report(city: str, api_key: str) -> str:
    """
    Fetch comprehensive weather data for the specified city.
    """
    owm = OWM(api_key)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    status = w.detailed_status
    wind_speed = w.wind().get("speed", 0.0)
    humidity = w.humidity
    temp_dict = w.temperature("celsius")
    temp_current = temp_dict.get("temp")
    temp_max = temp_dict.get("temp_max")
    temp_min = temp_dict.get("temp_min")
    clouds = w.clouds
    rain = w.rain if w.rain else "No rain"

    return (
        f"\n--- Weather Report for '{city}' ---\n"
        f"• Status: {status}\n"
        f"• Current Temperature: {temp_current}°C (Min: {temp_min}°C, Max: {temp_max}°C)\n"
        f"• Wind Speed: {wind_speed} m/s\n"
        f"• Humidity: {humidity}%\n"
        f"• Cloudiness: {clouds}%\n"
        f"• Rain: {rain}\n"
    )


def main() -> None:
    """
    Main interactive entry point.
    """
    if not API_KEY:
        raise ValueError("Error: OWM_API_KEY not found in .env file")

    user_city = input("Enter city name (e.g. Dnipro, Lviv, London): ").strip()
    if not user_city:
        print("Error: City name cannot be empty.")
        return

    try:
        report = get_weather_report(user_city, API_KEY)
        print(report)
    except NotFoundError:
        print(f"\nError: City '{user_city}' not found. Please verify the name.")


if __name__ == "__main__":
    main()
