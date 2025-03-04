import requests

def get_weather(city):
    API_KEY = "9c6bff748f2ad0042930b8a3a3407e1a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url).json()
        if response.get("cod") != 200:
            return "City not found."

        weather_desc = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]

        weather_report = (f"Weather in {city}: {weather_desc.capitalize()}, "
                          f"Temperature: {temperature}°C, Humidity: {humidity}%, "
                          f"Wind Speed: {wind_speed} m/s")
        return weather_report
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
